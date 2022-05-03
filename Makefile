CURRENT_DIR = $(shell pwd)
PYTHON_VERSION := 3.7
AIRFLOW_VERSION := 2.2.4
CONSTRAINT_URL := https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt

.ONESHELL:

.PHONY: install
install:
	virtualenv -p /usr/local/opt/python@3.7/Frameworks/Python.framework/Versions/3.7/bin/python3 airflow_env
	. airflow_env/bin/activate
	pip install -r requierments.txt
	export AIRFLOW_HOME=$(CURRENT_DIR)
	pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

.PHONY: buid_webserver
buid_webserver:
	. airflow_env/bin/activate
	python3 --version
	airflow db init
	airflow users create --role Admin --username udesahackers --email udesahackers --firstname udesahackers --lastname udesahackers --password udesahackers
	airflow webserver --port 8080

.PHONY: start_scheduler
start_scheduler:
	. airflow_env/bin/activate
	airflow scheduler