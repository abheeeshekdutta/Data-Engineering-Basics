# User Guide (Living Document)

Last updated: 2026-02-13

This guide is the single entrypoint for using this repository. It summarizes what has already been implemented and how to execute the 32-week roadmap step by step.

## 1) What Is Already Implemented

This repository already contains a complete scaffold for the open-source analytics engineering roadmap:

- Roadmap and planning docs (`docs/roadmap/`)
- Architecture, governance, ADRs, runbooks, postmortems (`docs/architecture/`, `docs/governance/`, `docs/adrs/`, `docs/runbooks/`, `docs/postmortems/`)
- Source data contracts (`contracts/raw/`)
- Ingestion framework (`ingestion/`)
- dbt project (`analytics_dbt/`)
- Airflow DAGs (`airflow/dags/`)
- Soda checks (`soda/checks/`)
- CDC starter config (`cdc/connect/`)
- OpenLineage/Marquez config (`lineage/`)
- Superset dashboard spec (`superset/dashboards/`)
- Local infra (`docker-compose.yml`)
- CI baseline (`.github/workflows/ci.yml`)

## 2) Start Here (Fast Path)

1. Read the roadmap:
   - `docs/roadmap/32_week_learning_roadmap.md`
2. Set up your environment:
   - `docs/roadmap/setup_local.md`
3. Execute phases in order:
   - `docs/roadmap/phase_execution_steps.md`
4. Track weekly progress:
   - `docs/roadmap/weekly_tracker.md`
5. Validate readiness:
   - `docs/roadmap/assessment_rubric.md`

## 3) Local Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
docker compose up -d
```

Optional helper:

```bash
scripts/bootstrap.sh
```

Initialize warehouse schemas/tables:

```bash
psql -h localhost -U postgres -d analytics -f sql/init_warehouse.sql
```

## 4) Command Guide

Validate contracts:

```bash
python3 scripts/verify_contracts.py
```

Run ingestion:

```bash
export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/analytics
PYTHONPATH=ingestion/src python -m ingestion.pipeline --config ingestion/src/ingestion/sources.yml --state-file ingestion/state.json
```

Run dbt:

```bash
cd analytics_dbt
dbt deps
dbt build
dbt test
dbt docs generate
cd ..
```

Run quality gate:

```bash
scripts/run_quality_gate.sh
```

## 5) Phase-by-Phase Execution Map

- Phase 1 (Weeks 1-4): `learning/phase1/`, `sql/init_warehouse.sql`
- Phase 2 (Weeks 5-10): `analytics_dbt/`, `learning/phase2/`
- Phase 3 (Weeks 11-16): `airflow/dags/`, `learning/phase3/`
- Phase 4 (Weeks 17-22): `ingestion/`, `cdc/`, `learning/phase4/`
- Phase 5 (Weeks 23-27): `contracts/`, `soda/`, `lineage/`, `learning/phase5/`
- Phase 6 (Weeks 28-32): `superset/`, `docs/postmortems/`, `learning/phase6/`

## 6) Weekly Operating Routine

Use this sequence each week:

1. Plan the week in `docs/roadmap/weekly_tracker.md`.
2. Implement tasks for the current phase.
3. Run validations (contracts, tests, quality gate).
4. Update docs/runbooks with what changed.
5. Record risks and next actions in tracker.

## 7) Current Validation Status

Validated in this repository setup:

- Python source compile check passed (`compileall`)
- Contract validation passed (`scripts/verify_contracts.py`)

Not validated in this environment:

- `pytest` (depends on local package install availability)
- Full `dbt` execution against running Postgres
- Full Airflow/Soda/CDC runtime execution

## 8) Troubleshooting

- `ModuleNotFoundError: ingestion`
  - Use `PYTHONPATH=ingestion/src` when running ingestion from repo root.
- `pip install` fails in system Python
  - Use a virtual environment (`python3 -m venv .venv`).
- dbt profile not found
  - Copy `analytics_dbt/profiles/profiles.yml.example` into your dbt profiles path and adjust credentials.
- Soda scan fails to connect
  - Confirm Postgres container is running and credentials in `soda/configuration.yml` are correct.

## 9) How To Maintain This Guide

When you add or change roadmap assets, update this file in the same commit:

1. Update `Last updated` date.
2. Update section `1) What Is Already Implemented` if structure changed.
3. Update section `4) Command Guide` if commands changed.
4. Append one row to the change log below.

## 10) Change Log

| Date | Change | Updated By |
|---|---|---|
| 2026-02-13 | Initial living user guide created with setup, execution map, command cookbook, and maintenance process. | Codex |
