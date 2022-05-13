""" Dag for recommendation models """

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from dag_args import default_args
from files.TopProduct import TopProducts
from files.TopCTR import TopCTR
from files.FiltrarDatos import FiltrarDatos

dag = DAG(
    'recommendation_models',
    default_args=default_args,
    description='How to use the Python Operator?',
    schedule_interval='@daily',
    catchup=True,
    max_active_runs=1,
    concurrency=1
)

filtrardatos_task = PythonOperator(
    task_id='FiltrarDatos',
    python_callable=create_datasets,
    dag=dag,
)

topctr_task = PythonOperator(
    task_id='TopCTR',
    python_callable=TopCTR,
    dag=dag,
)

topproduct_task = PythonOperator(
    task_id='Top_products',
    python_callable=TopProducts,
    dag=dag,
)

filtrardatos_task >> topctr_task
filtrardatos_task >> topproduct_task
