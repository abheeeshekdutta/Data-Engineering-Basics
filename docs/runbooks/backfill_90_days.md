# 90-Day Backfill Runbook

## Preconditions

- Confirm target date window and partition keys.
- Confirm downstream dependencies and maintenance window.
- Pause publish task if required.

## Steps

1. Trigger Airflow backfill for ingestion DAG (90 days).
2. Run dbt with date-scoped selectors.
3. Execute quality checks for affected partitions.
4. Run reconciliation SQL for key business metrics.
5. Re-enable publish tasks and monitor first full cycle.

## Validation

- Row counts match expected source range.
- No duplicate keys in fact tables.
- Freshness SLA restored.
