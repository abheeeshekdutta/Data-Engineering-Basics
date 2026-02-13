# Assessment Rubric and Exit Gates

## Required Scenarios

1. Late-arriving orders update historical facts correctly.
2. Duplicate source records are deduplicated without data loss.
3. Backfill of 90 days runs without downstream breakage.
4. dbt tests fail fast and block publish on contract violations.
5. Airflow retries recover transient failures safely.
6. CDC pipeline handles one nullable-column schema evolution.
7. Lineage view identifies all impacted downstream assets.
8. Dashboard metrics reconcile with source-of-truth SQL.

## Scoring Model

- `Pass`: criterion met with reproducible evidence.
- `Partial`: criterion met but lacks repeatability or documentation.
- `Fail`: criterion not met or produces inconsistent output.

## Evidence Requirements

- Command or DAG run logs.
- SQL validation output or test results.
- Updated docs/runbooks where relevant.
- Screenshots or exported lineage/dashboard evidence.

## Graduation Criteria

- All 8 scenarios marked `Pass`.
- Capstone runbook can recover from a controlled failure.
- Fresh-clone setup can run end-to-end without undocumented steps.
