# Open-Source Analytics Engineering Roadmap (2026+)

This repository implements a full 32-week, open-source-only roadmap to become industry-ready in analytics engineering.

## Primary Entry Point

- Start with `USER_GUIDE.md` for setup, execution order, commands, and maintenance workflow.

## Scope

- No cloud platform dependency
- No Spark/PySpark
- Stack: PostgreSQL, DuckDB, dbt Core, Airflow, Soda Core, Debezium/Kafka, OpenLineage/Marquez, Superset
- Domain: e-commerce analytics

## Repository Layout

- `docs/`: roadmap, architecture, runbooks, ADRs, postmortems, governance
- `learning/`: phase-by-phase assignments and exercises
- `contracts/`: source-to-warehouse YAML contracts
- `ingestion/`: config-driven incremental ingestion scaffold (Python)
- `analytics_dbt/`: dbt project skeleton (`stg_`, `int_`, `dim_`, `fct_`, snapshots, tests)
- `airflow/`: DAGs for ingest, transform, and quality/publish
- `soda/`: data quality checks
- `cdc/`: Debezium and Kafka Connect local setup assets
- `lineage/`: OpenLineage/Marquez integration notes
- `superset/`: dashboard specification
- `scripts/`: utility scripts and quality gates

## Quick Start

1. Read `USER_GUIDE.md`.
2. Read `docs/roadmap/32_week_learning_roadmap.md`.
3. Start Phase 1 tasks in `learning/phase1/`.
4. Use `docs/roadmap/weekly_tracker.md` to track progress.
5. Build the capstone incrementally from Phases 2-6.

## Local Toolchain

- Python 3.11+
- Docker + Docker Compose
- `psql` client
- `dbt-core` + `dbt-postgres`

## Suggested Weekly Cadence (8-12 hrs)

- 2h: official docs + concept study
- 4-6h: implementation
- 2h: debugging, tests, documentation
- 1-2h: retrospective and backlog grooming

## Completion Definition

Completion means every scenario in `docs/roadmap/assessment_rubric.md` passes, and your capstone runs end-to-end with reproducible local setup.
