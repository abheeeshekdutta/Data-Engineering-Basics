from __future__ import annotations

from pathlib import Path
import re
import sys

REQUIRED_TOP_LEVEL = {"source", "owner", "freshness_sla_minutes", "primary_key", "columns"}
REQUIRED_COLUMN_FIELDS = {"name", "type", "nullable"}


def _load_with_yaml(path: Path) -> dict:
    import yaml  # type: ignore

    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError("contract root must be a map")
    return payload


def _load_without_yaml(path: Path) -> dict:
    payload: dict = {}
    columns: list[dict[str, str]] = []
    in_columns = False
    current_column: dict[str, str] | None = None

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.split("#", 1)[0].rstrip()
        if not line.strip():
            continue

        indent = len(line) - len(line.lstrip(" "))
        stripped = line.strip()

        if indent == 0:
            top_key_match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:(.*)$", stripped)
            if top_key_match:
                key = top_key_match.group(1)
                value = top_key_match.group(2).strip()
                in_columns = key == "columns"
                if key != "columns":
                    payload[key] = value if value else None
                continue

        if in_columns:
            if stripped.startswith("- "):
                if current_column:
                    columns.append(current_column)
                current_column = {}
                field_match = re.match(r"^- ([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$", stripped)
                if field_match:
                    current_column[field_match.group(1)] = field_match.group(2).strip()
            elif current_column:
                field_match = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$", stripped)
                if field_match:
                    current_column[field_match.group(1)] = field_match.group(2).strip()

    if current_column:
        columns.append(current_column)
    payload["columns"] = columns
    return payload


def load_contract(path: Path) -> dict:
    try:
        return _load_with_yaml(path)
    except Exception:
        return _load_without_yaml(path)


def validate_contract(path: Path) -> list[str]:
    errors: list[str] = []
    payload = load_contract(path)

    missing = REQUIRED_TOP_LEVEL - set(payload.keys())
    if missing:
        errors.append(f"{path}: missing top-level keys: {sorted(missing)}")

    columns = payload.get("columns", [])
    if not isinstance(columns, list) or not columns:
        errors.append(f"{path}: columns must be a non-empty list")
        return errors

    for idx, column in enumerate(columns):
        if not isinstance(column, dict):
            errors.append(f"{path}: column[{idx}] must be a map")
            continue
        missing_col = REQUIRED_COLUMN_FIELDS - set(column.keys())
        if missing_col:
            errors.append(f"{path}: column[{idx}] missing keys: {sorted(missing_col)}")

    return errors


def main() -> int:
    contract_dir = Path("contracts/raw")
    if not contract_dir.exists():
        print("contracts/raw not found")
        return 1

    all_errors: list[str] = []
    for path in sorted(contract_dir.glob("*.yml")):
        all_errors.extend(validate_contract(path))

    if all_errors:
        for err in all_errors:
            print(err)
        return 1

    print(f"Validated {len(list(contract_dir.glob('*.yml')))} contract files successfully")
    return 0


if __name__ == "__main__":
    sys.exit(main())
