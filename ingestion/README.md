# Ingestion Framework (Phase 4)

Config-driven ingestion scaffold for batch loads.

## Features

- YAML-defined sources
- Incremental state tracking (`state.json`)
- CSV and API source adapters
- Append/upsert loading pattern for raw tables

## Run

```bash
PYTHONPATH=ingestion/src python -m ingestion.pipeline --config ingestion/src/ingestion/sources.yml --state-file ingestion/state.json
```

Set `DATABASE_URL` first, for example:

```bash
export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/analytics
```
