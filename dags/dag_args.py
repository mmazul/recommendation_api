""" Common args for  """

from airflow.utils.dates import days_ago
from datetime import timedelta


default_args = {
    'owner': 'team-hackers-udesa',
    'start_date': days_ago(7),
    'email': ['teamhackersudesa@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=1),

}