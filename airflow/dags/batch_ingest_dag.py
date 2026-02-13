from __future__ import annotations

from datetime import datetime, timedelta

from airflow import DAG
from airflow.datasets import Dataset
from airflow.operators.bash import BashOperator

RAW_DATASET = Dataset("dataset://raw_ingestion_complete")

with DAG(
    dag_id="ecommerce_batch_ingest_dag",
    start_date=datetime(2026, 1, 1),
    schedule="@hourly",
    catchup=False,
    default_args={
        "owner": "data_eng",
        "retries": 3,
        "retry_delay": timedelta(minutes=5),
    },
    tags=["ingestion", "batch"],
) as dag:
    load_raw_orders = BashOperator(
        task_id="load_raw_orders",
        bash_command=(
            "PYTHONPATH=ingestion/src python -m ingestion.pipeline "
            "--config ingestion/src/ingestion/sources.yml "
            "--state-file ingestion/state.json"
        ),
        outlets=[RAW_DATASET],
    )

    load_raw_orders
