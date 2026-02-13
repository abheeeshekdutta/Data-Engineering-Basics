# Postmortem 002: Contract Violation Broke Publish Step

## Summary
Unexpected null primary key values reached marts and blocked quality gate.

## Root Cause
Source API payload changed and null handling in ingestion adapter was incomplete.

## Fix
Added strict null-key reject path and dead-letter capture.

## Prevention
Contract validation now runs before raw table write.
