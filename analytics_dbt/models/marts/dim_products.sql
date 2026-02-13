select
  product_id,
  sku,
  category,
  unit_price,
  updated_at
from {{ ref('stg_products') }}
