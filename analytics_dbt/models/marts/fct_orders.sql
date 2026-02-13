select
  order_id,
  customer_id,
  order_created_at,
  order_date,
  order_status,
  order_amount,
  email,
  country_code,
  ingested_at
from {{ ref('int_orders_enriched') }}
