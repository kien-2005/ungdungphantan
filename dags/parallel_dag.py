from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import time


def process_1():
    time.sleep(20)
    print("Worker 1")


def process_2():
    time.sleep(20)
    print("Worker 2")


def process_3():
    time.sleep(20)
    print("Worker 3")


with DAG(
    dag_id="parallel_dag",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id="task_1",
        python_callable=process_1
    )

    t2 = PythonOperator(
        task_id="task_2",
        python_callable=process_2
    )

    t3 = PythonOperator(
        task_id="task_3",
        python_callable=process_3
    )

    [t1, t2, t3]