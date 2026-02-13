# Local Setup Guide

## 1) Environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 2) Start Services

```bash
docker compose up -d
```

## 3) Validate Contracts

```bash
python scripts/verify_contracts.py
```

## 4) Run Ingestion

```bash
export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/analytics
PYTHONPATH=ingestion/src python -m ingestion.pipeline --config ingestion/src/ingestion/sources.yml --state-file ingestion/state.json
```

## 5) Run dbt

```bash
cd analytics_dbt
dbt deps
dbt build
dbt test
```

## 6) Run Airflow DAGs

Run DAGs in order: ingest -> transform -> quality/publish (dataset scheduling will chain them).
