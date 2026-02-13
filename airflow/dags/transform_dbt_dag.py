from __future__ import annotations

from datetime import datetime, timedelta

from airflow import DAG
from airflow.datasets import Dataset
from airflow.operators.bash import BashOperator

RAW_DATASET = Dataset("dataset://raw_ingestion_complete")
TRANSFORMED_DATASET = Dataset("dataset://dbt_transform_complete")

with DAG(
    dag_id="ecommerce_transform_dbt_dag",
    start_date=datetime(2026, 1, 1),
    schedule=[RAW_DATASET],
    catchup=False,
    default_args={
        "owner": "analytics_eng",
        "retries": 2,
        "retry_delay": timedelta(minutes=10),
    },
    tags=["transform", "dbt"],
) as dag:
    run_dbt_build = BashOperator(
        task_id="run_dbt_build",
        bash_command="cd analytics_dbt && dbt deps && dbt build",
    )

    build_docs = BashOperator(
        task_id="build_docs",
        bash_command="cd analytics_dbt && dbt docs generate",
        outlets=[TRANSFORMED_DATASET],
    )

    run_dbt_build >> build_docs
