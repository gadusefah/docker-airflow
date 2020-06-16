
import datetime
import logging

from airflow import DAG
from airflow.operators.python_operator import PythonOperator



def my_function():
    logging.info("Hello World")

dag = DAG(
        'hello_world', 
        start_date=datetime.datetime.now())

greet_task = PythonOperator(
    task_id='greet_task',
    python_callable=my_function,
    dag=dag
)


