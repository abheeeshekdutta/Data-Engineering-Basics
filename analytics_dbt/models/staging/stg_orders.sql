select
  cast(order_id as bigint) as order_id,
  cast(customer_id as bigint) as customer_id,
  cast(order_created_at as timestamp) as order_created_at,
  cast(order_status as text) as order_status,
  cast(total_amount as numeric(12, 2)) as order_amount,
  cast(ingested_at as timestamp) as ingested_at
from {{ source('raw', 'orders') }}
