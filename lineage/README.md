# OpenLineage and Marquez

## Objective
Capture lineage from Airflow/dbt runs and inspect graph in Marquez.

## Setup Notes

- Point OpenLineage transport to Marquez API endpoint.
- Ensure Airflow has OpenLineage provider installed.
- Verify lineage events for ingest, transform, and publish tasks.

## Validation

Run one full DAG cycle and confirm upstream/downstream graph for `marts.fct_orders`.
