# Change Management

## Required for every change

- PR includes impact summary and rollback notes.
- Contract updates are versioned and reviewed.
- Downstream impact checked via lineage graph.
- Data quality checks updated before merge.

## Breaking Change Policy

- Introduce additive schema first.
- Deprecate old fields with migration notice.
- Remove fields only after consumer confirmation.
