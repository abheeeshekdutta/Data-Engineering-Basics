select
  customer_id,
  email,
  first_name,
  last_name,
  country_code,
  updated_at
from {{ ref('stg_customers') }}
