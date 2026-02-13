from __future__ import annotations

import argparse
import os
from datetime import UTC, datetime
from typing import Any

import psycopg

from ingestion.config import load_config
from ingestion.loaders import load_api_source, load_csv_source
from ingestion.state import load_state, save_state


def _filter_incremental(
    rows: list[dict[str, Any]],
    cursor_field: str | None,
    last_value: str | None,
) -> list[dict[str, Any]]:
    if not cursor_field or not last_value:
        return rows
    filtered: list[dict[str, Any]] = []
    for row in rows:
        row_value = str(row.get(cursor_field, ""))
        if row_value > last_value:
            filtered.append(row)
    return filtered


def _insert_rows(
    conn: psycopg.Connection,
    target_table: str,
    rows: list[dict[str, Any]],
    ingestion_ts: str,
) -> int:
    if not rows:
        return 0

    keys = sorted(rows[0].keys())
    columns = keys + ["ingested_at"]
    placeholders = ", ".join(["%s"] * len(columns))
    cols_sql = ", ".join(columns)
    sql = f"INSERT INTO {target_table} ({cols_sql}) VALUES ({placeholders})"  # noqa: S608

    values = []
    for row in rows:
        values.append([row.get(k) for k in keys] + [ingestion_ts])

    with conn.cursor() as cur:
        cur.executemany(sql, values)
    return len(values)


def run_pipeline(config_path: str, state_path: str) -> None:
    cfg = load_config(config_path)
    state = load_state(state_path)
    db_url = os.environ.get("DATABASE_URL")
    if not db_url:
        raise RuntimeError("DATABASE_URL is not set")

    with psycopg.connect(db_url) as conn:
        for source in cfg.get("sources", []):
            name = source["name"]
            source_type = source["type"]
            target_table = source["target_table"]
            cursor_field = source.get("cursor_field")
            mode = source.get("mode", "append")

            if source_type == "csv":
                rows = load_csv_source(source)
            elif source_type == "api":
                rows = load_api_source(source)
            else:
                raise ValueError(f"Unsupported source type: {source_type}")

            last_value = state.get(name, {}).get("last_cursor")
            if mode == "incremental":
                rows = _filter_incremental(rows, cursor_field, last_value)

            ingestion_ts = datetime.now(UTC).isoformat()
            inserted = _insert_rows(conn, target_table, rows, ingestion_ts)

            if inserted > 0 and cursor_field:
                max_cursor = max(str(r.get(cursor_field, "")) for r in rows)
                state[name] = {
                    "last_cursor": max_cursor,
                    "last_run_at": ingestion_ts,
                    "inserted_rows": inserted,
                }
            else:
                state[name] = {
                    "last_cursor": last_value,
                    "last_run_at": ingestion_ts,
                    "inserted_rows": inserted,
                }
            print(f"{name}: inserted={inserted}")

        conn.commit()
    save_state(state_path, state)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run batch ingestion")
    parser.add_argument("--config", required=True, help="Path to sources YAML")
    parser.add_argument("--state-file", required=True, help="Path to state json")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    run_pipeline(args.config, args.state_file)
