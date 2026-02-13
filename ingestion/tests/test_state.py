from __future__ import annotations

from pathlib import Path

from ingestion.state import load_state, save_state


def test_load_state_returns_empty_for_missing_file(tmp_path: Path) -> None:
    state_file = tmp_path / "missing.json"
    assert load_state(state_file) == {}


def test_save_and_load_state_roundtrip(tmp_path: Path) -> None:
    state_file = tmp_path / "state.json"
    state = {"orders": {"last_cursor": "2026-01-01T00:00:00Z"}}
    save_state(state_file, state)
    loaded = load_state(state_file)
    assert loaded == state
