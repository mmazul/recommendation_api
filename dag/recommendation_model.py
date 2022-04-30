""" Dag for recommendation models """

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from dag_args import default_args
from files.TopProduct import Top_products
from files.TopCTR import TopCTR

dag = DAG(
    'recommendation_models',
    default_args=default_args,
    description='How to use the Python Operator?',
    schedule_interval='@daily',
    catchup=True,
    max_active_runs=1
)

datasets_task = PythonOperator(
    task_id='TopCTR',
    python_callable=TopCTR,
    dag=dag,
)

model1_task = PythonOperator(
    task_id='TopCTR',
    python_callable=TopCTR,
    dag=dag,
)

model2_task = PythonOperator(
    task_id='Top_products',
    python_callable=Top_products,
    dag=dag,
)

datasets_task >> model1_task
datasets_task >> model2_task
