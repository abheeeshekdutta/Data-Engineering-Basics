# Phase 3 Lab Tasks (Airflow)

1. Run Airflow locally and load DAGs.
2. Trigger `ecommerce_batch_ingest_dag` and confirm raw table writes.
3. Trigger `ecommerce_transform_dbt_dag` via dataset dependency.
4. Trigger `ecommerce_quality_publish_dag` and enforce pass/fail gate.
5. Inject transient failure and validate retries.
6. Run backfill scenario and validate no duplicate rows.
7. Measure task durations and document bottlenecks.
8. Update incident triage runbook based on findings.
