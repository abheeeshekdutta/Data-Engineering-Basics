# Incident Triage Runbook

## Severity Levels

- SEV1: data unavailable for business-critical dashboard.
- SEV2: delayed or partial data availability.
- SEV3: non-critical quality issue.

## Triage Sequence

1. Identify failing DAG/task and first error timestamp.
2. Classify issue: source, transform, quality gate, infra.
3. Check idempotency before retry or backfill.
4. Validate downstream table freshness and completeness.
5. Communicate status and ETA.
6. Execute remediation and verify reconciliation query.
7. Log postmortem actions.

## Recovery Guardrails

- Never run destructive delete without scoped backup.
- Prefer replay/backfill over manual row edits.
- Validate metrics after recovery with signed reconciliation query.
