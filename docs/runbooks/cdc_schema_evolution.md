# CDC Schema Evolution Runbook

## Scenario
A nullable column is added to a source table streamed via Debezium.

## Procedure

1. Confirm source DDL change and nullability.
2. Verify connector still healthy in Kafka Connect.
3. Update downstream contract file and dbt model.
4. Add or adjust quality checks for the new field.
5. Re-run transformation and reconciliation queries.
6. Validate lineage graph reflects new column propagation.

## Rollback Plan

- If downstream break occurs, isolate field usage in transforms.
- Keep connector running; defer model consumption of new field.
