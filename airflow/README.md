# Airflow DAGs

## DAGs

- `batch_ingest_dag.py`: loads raw sources via ingestion pipeline
- `transform_dbt_dag.py`: runs dbt build/test/docs
- `quality_publish_dag.py`: runs Soda checks and publish gate

## Notes

- DAGs are dataset-aware using Airflow `Dataset` events.
- Tasks are built to be re-runnable and retry-safe.
