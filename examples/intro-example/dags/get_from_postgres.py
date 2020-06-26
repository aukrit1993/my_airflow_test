from datetime import timedelta, datetime
import requests
import psycopg2

import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.hooks.postgres_hook import PostgresHook

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2019, 3, 30),
    "email": ["airflow@airflow.com"],
    "retries": 0,
    "retry_delay": timedelta(minutes=2),
}

dag = DAG(
    "get_data_postgres",
    default_args=default_args,
    description="Get data from postgres",
    schedule_interval="0/1 * * * *",
    catchup=False,
    # schedule_interval=timedelta(days=1),
)

def get_data_source():
    postgres_hook = PostgresHook(postgres_conn_id="postgres_id")
    records = postgres_hook.get_records(sql="select dag_id from dag")
    print(records)
        
t1 = PythonOperator(
    task_id="get_data_source", 
    python_callable=get_data_source,
    # op_args=['TEST PRINT PYTHON'],
    # provide_context=True,
    dag=dag,
)

t1
