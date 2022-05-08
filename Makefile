CURRENT_DIR = $(shell pwd)
PYTHON_VERSION := 3.10
AIRFLOW_VERSION := 2.3.0
CONSTRAINT_URL := https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt

.ONESHELL:

.PHONY: airflow_install
airflow_install:
	virtualenv airflow_env --python=python3
	( \
		source airflow_env/bin/activate; \
		pip install -r requirements.txt; \
		export AIRFLOW_HOME=$(CURRENT_DIR); \
		export AIRFLOW__CORE__SQL_ALCHEMY_CONN="postgresql://postgres@localhost:5432/my_database?options=-csearch_path%3Dairflow"
		export AIRFLOW__CORE__SQL_ALCHEMY_SCHEMA="airflow"
		pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"; \
	)

.PHONY: airflow_launch
airflow_launch:
	( \
		source airflow_env/bin/activate; \
		export AIRFLOW_HOME=$(CURRENT_DIR); \
		airflow db init; \
		airflow users create --role Admin --username udesahackers --email udesahackers --firstname udesahackers --lastname udesahackers --password udesahackers; \
		airflow webserver --port 8080 -D; \
		airflow scheduler -D; \
	)

