# CDC Proof-of-Concept

This folder contains starter configuration for Postgres CDC with Debezium and Kafka Connect.

## Steps

1. Start stack: `docker compose up -d postgres zookeeper kafka connect`
2. Ensure source table has replica identity and primary key.
3. Register connector with the JSON payload in `connect/register-postgres-source.json`.
4. Consume topic and validate event stream.
