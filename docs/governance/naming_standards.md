# Naming Standards

## Table Prefixes

- `stg_`: source-aligned cleaned tables
- `int_`: reusable intermediate logic
- `dim_`: dimensions
- `fct_`: facts

## Column Conventions

- Primary keys: `<entity>_id`
- Timestamps in UTC: `<event>_at`
- Boolean flags: `is_<state>`
- Monetary amounts: `<metric>_amount`

## DAG and Task Naming

- DAG: `<domain>_<purpose>_dag`
- Task: verb-first, snake_case (`load_raw_orders`, `run_dbt_build`)
