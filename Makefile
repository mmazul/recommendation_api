CURRENT_DIR = $(shell pwd)
#PYTHON_VERSION := 3.7
PYTHON_VERSION := 3.10
#AIRFLOW_VERSION := 2.2.4
AIRFLOW_VERSION := 2.3.0
CONSTRAINT_URL := https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt

.ONESHELL:

.PHONY: airflow_install
airflow_install:
	#virtualenv -p /usr/local/opt/python@3.7/Frameworks/Python.framework/Versions/3.7/bin/python3 airflow_env
	virtualenv airflow_env --python=python3
	( \
		source airflow_env/bin/activate; \
		pip install -r requirements.txt; \
		export AIRFLOW_HOME=$(CURRENT_DIR); \
		pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"; \
	)

.PHONY: airflow_db
airflow_db:
	( \
		source airflow_env/bin/activate; \
		airflow db init; \
		airflow users create --role Admin --username udesahackers --email udesahackers --firstname udesahackers --lastname udesahackers --password udesahackers; \
	)

.PHONY: build_webserver
buid_webserver:
	( \
		source airflow_env/bin/activate; \
		airflow webserver --port 8080 -D; \
	)

.PHONY: start_scheduler
start_scheduler:
	( \
		source airflow_env/bin/activate; \
		airflow scheduler -D; \
	)

