# Definition of Done for Pipelines and Models

A pipeline/model is done only if all items pass:

- Contract exists with schema, ownership, freshness SLA, and key constraints.
- dbt model has tests and documentation.
- Soda checks exist for critical quality conditions.
- Airflow task is idempotent and has retry policy.
- Lineage is visible in Marquez.
- Runbook includes failure triage and rollback/backfill guidance.
- Change is reviewed and linked to an ADR or issue.
