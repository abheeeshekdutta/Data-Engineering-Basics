select
  cast(customer_id as bigint) as customer_id,
  cast(email as text) as email,
  cast(first_name as text) as first_name,
  cast(last_name as text) as last_name,
  cast(country_code as text) as country_code,
  cast(updated_at as timestamp) as updated_at
from {{ source('raw', 'customers') }}
