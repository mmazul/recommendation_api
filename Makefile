CURRENT_DIR = $(shell pwd)
PYTHON_VERSION := 3.10
AIRFLOW_VERSION := 2.3.0
CONSTRAINT_URL := https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt

.ONESHELL:

.PHONY: airflow_launch2
airflow_launch2:
	virtualenv airflow_env --python=python3
	( \
        . airflow_env/bin/activate; \
        pip install -r requirements.txt; \
        export AIRFLOW_HOME=$(CURRENT_DIR); \
        export AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://$(PS_USER):$(PS_PASS)@$(PS_DB); \
        export AIRFLOW__CORE__EXECUTOR=LocalExecutor; \
        export AIRFLOW__CORE__PARALLELISM=2; \
        export AIRFLOW__CORE__LOAD_EXAMPLES=False; \
        export AIRFLOW__WEBSERVER__WORKERS=1; \
        pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"; \
        #airflow db init; \
        #airflow users create --role Admin --username udesahackers --email udesahackers --firstname udesahackers --lastname udesahackers --password udesahackers; \
        #airflow webserver --port 8080 -D; \
        #airflow scheduler -D; \
    )

prepare_ec2:
	sudo apt update
	sudo apt install python3-pip
	sudo apt install python3-virtualenv

airflow_create_env:
	virtualenv airflow_env --python=python3

airflow_launch:
	pip install -r requirements.txt
	export AIRFLOW_HOME=$(CURRENT_DIR)
	export AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://$(PS_USER):$(PS_PASS)@$(PS_DB)
	export AIRFLOW__CORE__EXECUTOR=LocalExecutor
	export AIRFLOW__CORE__PARALLELISM=2
	export AIRFLOW__CORE__LOAD_EXAMPLES=False
	export AIRFLOW__WEBSERVER__WORKERS=1
	pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
	airflow db init
	airflow users create --role Admin --username udesahackers --email udesahackers --firstname udesahackers --lastname udesahackers --password udesahackers
	#airflow webserver --port 8080 -D
	#sleep 60
	#airflow scheduler -D

airflow_relaunch:
	export AIRFLOW_HOME=$(CURRENT_DIR)
	export AIRFLOW__DATABASE__SQL_ALCHEMY_CONN=postgresql+psycopg2://$(PS_USER):$(PS_PASS)@$(PS_DB)
	export AIRFLOW__CORE__EXECUTOR=LocalExecutor
	export AIRFLOW__CORE__PARALLELISM=2
	export AIRFLOW__CORE__LOAD_EXAMPLES=False
	export AIRFLOW__WEBSERVER__WORKERS=1
	#airflow webserver --port 8080 -D
	#sleep 60
	#airflow scheduler -D
