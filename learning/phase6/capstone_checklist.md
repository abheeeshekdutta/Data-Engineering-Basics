# Phase 6 Capstone Checklist

## Build

- [ ] Ingestion pipeline runs from config and writes raw tables.
- [ ] dbt builds all staging/intermediate/mart models.
- [ ] Airflow orchestrates ingest -> transform -> quality -> publish.
- [ ] Soda and dbt tests run as quality gate.
- [ ] OpenLineage events visible in Marquez.
- [ ] Superset dashboard uses curated marts only.

## Validation

- [ ] Late-arriving order scenario passes.
- [ ] Duplicate handling scenario passes.
- [ ] 90-day backfill scenario passes.
- [ ] CDC schema evolution scenario passes.
- [ ] Dashboard reconciliation checks pass.

## Portfolio

- [ ] Architecture doc updated.
- [ ] ADR list updated.
- [ ] 3 postmortems completed.
- [ ] README includes run/demo instructions.
