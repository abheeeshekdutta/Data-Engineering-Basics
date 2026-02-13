#!/usr/bin/env bash
set -euo pipefail

# dbt tests are the first gate.
(
  cd analytics_dbt
  dbt test
)

# Soda checks are the runtime gate.
soda scan -c soda/configuration.yml soda/checks/staging.yml
soda scan -c soda/configuration.yml soda/checks/marts.yml
