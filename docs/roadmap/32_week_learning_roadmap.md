# 32-Week Learning Roadmap

## Goal
Transition from Data Scientist to Analytics Engineer with production-style, open-source data systems.

## Phase 1 (Weeks 1-4): Modeling and Advanced SQL

### Week 1
- Define business entities and table grain for orders, customers, products, events.
- Draft star schema (`staging`, `intermediate`, `marts`).
- Run SQL profiling queries and document data caveats.

### Week 2
- Implement schema v1 in Postgres.
- Solve 8 advanced SQL exercises.
- Add baseline indexes and capture query plans.

### Week 3
- Implement late-arriving data handling patterns.
- Solve 8 advanced SQL exercises.
- Benchmark before/after query performance.

### Week 4
- Solve remaining SQL exercises (25+ total).
- Defend design decisions (grain, keys, SCD choice).
- Finalize Phase 1 artifacts and retrospective.

## Phase 2 (Weeks 5-10): dbt Core Deep Dive

### Week 5
- Initialize dbt project and profiles.
- Build `stg_*` models with source tests.

### Week 6
- Build `int_*` transformation layer.
- Add reusable macros and model docs.

### Week 7
- Build marts (`dim_customers`, `dim_products`, `fct_orders`).
- Add schema tests and constraints.

### Week 8
- Add snapshots for SCD handling.
- Add exposures and business metric documentation.

### Week 9
- Harden tests, refactor SQL, and improve naming consistency.
- Add CI checks for `dbt build`.

### Week 10
- Perform fresh-clone run-through.
- Validate reproducibility and close Phase 2 gaps.

## Phase 3 (Weeks 11-16): Airflow Orchestration

### Week 11
- Bootstrap local Airflow environment.
- Implement batch ingestion DAG skeleton.

### Week 12
- Add retries, idempotency guards, and SLA config.
- Add transform DAG for dbt tasks.

### Week 13
- Add quality-and-publish DAG and dependency chaining.
- Add logging and failure categorization.

### Week 14
- Run controlled failure drills and retry validation.
- Tune scheduling intervals and backfill behavior.

### Week 15
- Add run-duration monitoring and operational metadata.
- Document triage playbooks.

### Week 16
- Validate manual recovery procedures.
- Complete orchestration exit criteria.

## Phase 4 (Weeks 17-22): Ingestion and CDC

### Week 17
- Implement config-driven batch ingestion framework.
- Add source config contracts and incremental state tracking.

### Week 18
- Add API/file adapters and retry strategy.
- Land data into raw tables with audit columns.

### Week 19
- Study Postgres logical replication and Debezium architecture.
- Stand up Kafka + Connect + Debezium locally.

### Week 20
- Implement CDC connector for key source table.
- Validate change propagation into analytics path.

### Week 21
- Simulate schema evolution and compatibility checks.
- Document batch vs CDC tradeoffs.

### Week 22
- Finalize CDC proof-of-concept and operational notes.

## Phase 5 (Weeks 23-27): Quality, Contracts, Lineage, Governance

### Week 23
- Create contract files for all raw sources.
- Add schema, freshness, and ownership rules.

### Week 24
- Add Soda Core checks and integrate into DAG runtime.
- Implement contract gate in CI.

### Week 25
- Integrate OpenLineage emission and Marquez graph checks.
- Add impact analysis playbook.

### Week 26
- Finalize naming standards and ownership metadata.
- Add change management checklist.

### Week 27
- Run governance review and close all policy gaps.

## Phase 6 (Weeks 28-32): Capstone and Job Readiness

### Week 28
- Define capstone architecture and success metrics.
- Prepare local compose stack and seed data.

### Week 29
- Implement ingestion + dbt + orchestration end-to-end.
- Verify quality checks and lineage flow.

### Week 30
- Build Superset dashboard and metric reconciliation checks.
- Add architecture diagrams and ADR updates.

### Week 31
- Run incident simulations and write 3 postmortems.
- Tune reliability and re-run acceptance tests.

### Week 32
- Perform final demo run and portfolio packaging.
- Publish README and interview narrative assets.

## Weekly Checklist

For every week:
- Plan: define scope and target deliverables.
- Build: complete core implementation tasks.
- Validate: run tests and scenario checks.
- Document: update runbooks and decision logs.
- Retrospective: capture lessons and next risks.
