with orders as (
    select * from {{ ref('stg_orders') }}
),
customers as (
    select * from {{ ref('stg_customers') }}
)
select
    o.order_id,
    o.customer_id,
    c.email,
    c.country_code,
    o.order_created_at,
    date_trunc('day', o.order_created_at) as order_date,
    o.order_status,
    o.order_amount,
    o.ingested_at
from orders o
left join customers c on o.customer_id = c.customer_id
