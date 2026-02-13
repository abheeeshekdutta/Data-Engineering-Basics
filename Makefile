.PHONY: contracts py-compile

contracts:
	python scripts/verify_contracts.py

py-compile:
	python -m compileall ingestion/src airflow/dags scripts
