# ADR-0001: Open-Source Local-First Stack

## Status
Accepted

## Context
The learning and capstone environment must be cloud-independent and Spark-free while still reflecting production concerns.

## Decision
Adopt:
- PostgreSQL 18
- DuckDB
- dbt Core
- Airflow
- Soda Core
- Debezium + Kafka Connect
- OpenLineage + Marquez
- Superset

## Consequences
- Pros: low-cost, reproducible, transparent internals, broad portability.
- Cons: more manual local operations than managed cloud services.
- Mitigation: runbooks, compose-based setup, and strict contracts/tests.
