#!/usr/bin/env bash
set -euo pipefail

cp -n .env.example .env || true

echo "Starting core local services..."
docker compose up -d postgres zookeeper kafka connect

echo "Bootstrap complete. Next steps:"
echo "1) Export DATABASE_URL from .env"
echo "2) Run ingestion pipeline with PYTHONPATH=ingestion/src"
echo "3) Run dbt build/test"
echo "4) Start Airflow and execute DAGs"
