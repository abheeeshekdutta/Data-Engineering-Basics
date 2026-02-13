# Postmortem 003: CDC Consumer Failed on New Column

## Summary
Downstream parser expected fixed payload schema and crashed after source column addition.

## Root Cause
Consumer deserialization logic was not forward-compatible.

## Fix
Enabled schema-tolerant parsing and conditional mapping.

## Prevention
Schema evolution test added to release checklist.
