# -*- coding: utf-8 -*-

"""
### Tutorial Documentation
Documentation that goes along with the Airflow tutorial located
[here](https://airflow.incubator.apache.org/tutorial.html)
"""
from datetime import timedelta, datetime

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization
# default_args = {
#     'owner': 'airflow',
#     'depends_on_past': False,
#     'start_date': airflow.utils.dates.days_ago(2),
#     'email': ['airflow@example.com'],
#     'email_on_failure': False,
#     'email_on_retry': False,
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5),
#     # 'queue': 'bash_queue',
#     # 'pool': 'backfill',
#     # 'priority_weight': 10,
#     # 'end_date': datetime(2016, 1, 1),
#     # 'wait_for_downstream': False,
#     # 'dag': dag,
#     # 'adhoc':False,
#     # 'sla': timedelta(hours=2),
#     # 'execution_timeout': timedelta(seconds=300),
#     # 'on_failure_callback': some_function,
#     # 'on_success_callback': some_other_function,
#     # 'on_retry_callback': another_function,
#     # 'trigger_rule': u'all_success'
# }

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 3, 30),
    'email': ['airflow@airflow.com'],
    'retries': 0,
    'retry_delay': timedelta(minutes=2),
}

dag = DAG(
    'print_dag',
    default_args=default_args,
    description='Test Print',
    schedule_interval='*/5 * * * *',
    # schedule_interval=timedelta(days=1),
)

def test_print(test_print="TESTTTTTTTTT"):
    return print(test_print)

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag,
)

t2 = PythonOperator(
    task_id="test_print", 
    python_callable=test_print,
    # provide_context=True,
    dag=dag,
)

t1 >> t2
