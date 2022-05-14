""" Dag for recommendation models """

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from dag_args import default_args
from files.TopProduct import TopProducts
from files.TopCTR import TopCTR
from files.FiltrarDatos import FiltrarDatos
from files.DBWriting import DBWriting

dag = DAG(
    'recommendation_models',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=True,
    max_active_runs=1,
    concurrency=1
)

filtrardatos_task = PythonOperator(
    task_id='FiltrarDatos',
    python_callable=FiltrarDatos,
    dag=dag,
    op_kwargs={'date': '{{ ds }}'}
)

topctr_task = PythonOperator(
    task_id='TopCTR',
    python_callable=TopCTR,
    dag=dag,
    op_kwargs={'date': '{{ ds }}'}
)

topproduct_task = PythonOperator(
    task_id='TopProducts',
    python_callable=TopProducts,
    dag=dag,
    op_kwargs={'date': '{{ ds }}'}
)

dbwriting_task = PythonOperator(
    task_id='DBWriting',
    python_callable=DBWriting,
    dag=dag,
    op_kwargs={'date': '{{ ds }}'}
)

filtrardatos_task >> topctr_task >> dbwriting_task
filtrardatos_task >> topproduct_task >> dbwriting_task
