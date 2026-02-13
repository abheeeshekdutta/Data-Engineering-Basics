create schema if not exists raw;
create schema if not exists staging;
create schema if not exists intermediate;
create schema if not exists marts;

create table if not exists raw.orders (
  order_id bigint primary key,
  customer_id bigint not null,
  order_created_at timestamp not null,
  order_status text not null,
  total_amount numeric(12,2) not null,
  ingested_at timestamp not null
);

create table if not exists raw.customers (
  customer_id bigint primary key,
  email text not null,
  first_name text,
  last_name text,
  country_code text,
  updated_at timestamp not null
);

create table if not exists raw.products (
  product_id bigint primary key,
  sku text unique not null,
  category text,
  unit_price numeric(10,2) not null,
  updated_at timestamp not null
);

create table if not exists raw.events (
  event_id text primary key,
  customer_id bigint,
  session_id text,
  event_name text not null,
  event_time timestamp not null,
  payload_json jsonb
);
