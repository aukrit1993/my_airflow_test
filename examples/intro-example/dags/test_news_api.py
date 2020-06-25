# -*- coding: utf-8 -*-

"""
### Tutorial Documentation
Documentation that goes along with the Airflow tutorial located
[here](https://airflow.incubator.apache.org/tutorial.html)
"""
from datetime import timedelta, datetime
import requests

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2019, 3, 30),
    "email": ["airflow@airflow.com"],
    "retries": 0,
    "retry_delay": timedelta(minutes=2),
}

dag = DAG(
    "print_dag",
    default_args=default_args,
    description="Test Print",
    schedule_interval="0 * * * *",
    catchup=False,
    # schedule_interval=timedelta(days=1),
)

def test_print(test_print):
    return print(test_print)

def post_news():
    url = "http://newsapi.org/v2/everything?q=bitcoin&from=2020-03-01&sortBy=publishedAt&apiKey=9bb05ce2fe96482ba995c6709bb8648a"
    response = requests.request("GET", url)
    return print(response.text)

# t1, t2 and t3 are examples of tasks created by instantiating operators
t1 = BashOperator(
    task_id="print_date",
    bash_command="date",
    dag=dag,
)

t2 = PythonOperator(
    task_id="test_print", 
    python_callable=test_print,
    op_args=['TEST PRINT PYTHON'],
    # provide_context=True,
    dag=dag,
)

t3 = PythonOperator(
    task_id="post_news", 
    python_callable=post_news,
    # provide_context=True,
    dag=dag,
)

t1 >> t2
# t2 >> t3
