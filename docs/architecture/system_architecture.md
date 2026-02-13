# System Architecture (Local, Open Source)

## Logical Flow

Source Systems -> Ingestion (Python) -> Postgres Raw -> dbt Models -> Curated Marts -> Superset Dashboards

Parallel flow:
- Postgres logical replication -> Debezium -> Kafka -> downstream CDC consumers

Cross-cutting:
- Airflow orchestration
- Soda and dbt tests for data quality
- OpenLineage events to Marquez

## Components

- **PostgreSQL 18**: primary warehouse and CDC source.
- **DuckDB**: local analytical prototyping and validation.
- **dbt Core**: transformation and semantic modeling.
- **Airflow**: orchestration with retries, backfill, and SLAs.
- **Soda Core**: quality checks in runtime gates.
- **Debezium + Kafka Connect**: CDC proof-of-concept.
- **OpenLineage + Marquez**: lineage and impact analysis.
- **Superset**: metrics consumption.

## Design Constraints

- Must run locally and be reproducible via containerized setup.
- No managed cloud dependencies.
- No Spark/PySpark.
- All public data interfaces documented and versioned.
