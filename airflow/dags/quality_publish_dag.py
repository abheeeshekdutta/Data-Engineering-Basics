from __future__ import annotations

from datetime import datetime, timedelta

from airflow import DAG
from airflow.datasets import Dataset
from airflow.operators.bash import BashOperator

TRANSFORMED_DATASET = Dataset("dataset://dbt_transform_complete")

with DAG(
    dag_id="ecommerce_quality_publish_dag",
    start_date=datetime(2026, 1, 1),
    schedule=[TRANSFORMED_DATASET],
    catchup=False,
    default_args={
        "owner": "analytics_eng",
        "retries": 2,
        "retry_delay": timedelta(minutes=10),
    },
    tags=["quality", "publish"],
) as dag:
    run_soda_scan = BashOperator(
        task_id="run_soda_scan",
        bash_command="scripts/run_quality_gate.sh",
    )

    publish_curated_marts = BashOperator(
        task_id="publish_curated_marts",
        bash_command="echo 'Publishing curated marts after quality gate passed'",
    )

    run_soda_scan >> publish_curated_marts
