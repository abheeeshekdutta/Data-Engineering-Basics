select
  cast(product_id as bigint) as product_id,
  cast(sku as text) as sku,
  cast(category as text) as category,
  cast(unit_price as numeric(10, 2)) as unit_price,
  cast(updated_at as timestamp) as updated_at
from {{ source('raw', 'products') }}
