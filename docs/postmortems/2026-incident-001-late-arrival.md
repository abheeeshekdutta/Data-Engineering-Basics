# Postmortem 001: Late-Arriving Orders Caused Revenue Drift

## Summary
Orders arriving after daily cutoff were excluded from fact refresh.

## Root Cause
Incremental filter used ingestion time only; business event time was ignored.

## Fix
Dual watermark logic added (`ingested_at` and `order_created_at`) with 3-day lookback.

## Prevention
Add late-arrival scenario test to pre-merge checks.
