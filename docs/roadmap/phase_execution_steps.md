# Phase Execution Steps

## Phase 1

1. Apply warehouse DDL: `psql -f sql/init_warehouse.sql`
2. Complete SQL tasks in `learning/phase1/sql_exercises.sql`
3. Record tuning outcomes in `learning/phase1/query_tuning_template.md`

## Phase 2

1. Configure dbt profile from `analytics_dbt/profiles/profiles.yml.example`
2. Run `dbt deps`, `dbt build`, `dbt test`
3. Update tracker and evidence links

## Phase 3

1. Start Airflow and place DAGs from `airflow/dags/`
2. Trigger ingestion DAG and validate raw loads
3. Trigger transform and quality/publish DAGs

## Phase 4

1. Run ingestion framework with `PYTHONPATH=ingestion/src`
2. Start CDC stack (`postgres`, `kafka`, `connect`)
3. Register Debezium connector config

## Phase 5

1. Validate contracts: `python3 scripts/verify_contracts.py`
2. Run quality gate script: `scripts/run_quality_gate.sh`
3. Validate lineage visibility in Marquez

## Phase 6

1. Build Superset dashboard from metrics spec
2. Execute all acceptance scenarios in rubric
3. Package portfolio artifacts and capstone narrative
