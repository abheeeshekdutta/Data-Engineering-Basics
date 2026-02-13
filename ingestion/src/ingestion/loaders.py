from __future__ import annotations

import csv
from pathlib import Path
from typing import Any

import requests


def load_csv_source(source: dict[str, Any]) -> list[dict[str, Any]]:
    path = Path(source["path"])
    rows: list[dict[str, Any]] = []
    with path.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def load_api_source(source: dict[str, Any]) -> list[dict[str, Any]]:
    response = requests.get(source["url"], timeout=30)
    response.raise_for_status()
    payload = response.json()
    if isinstance(payload, list):
        return payload
    if isinstance(payload, dict) and "data" in payload and isinstance(payload["data"], list):
        return payload["data"]
    raise ValueError("Unsupported API payload format")
