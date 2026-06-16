from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def task_1():
    print("Task 1: Read CSV")

def task_2():
    print("Task 2: Process Data")

def task_3():
    print("Task 3: Save Result")

with DAG(
    dag_id="demo_dag",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id="read_csv",
        python_callable=task_1
    )

    t2 = PythonOperator(
        task_id="process_data",
        python_callable=task_2
    )

    t3 = PythonOperator(
        task_id="save_result",
        python_callable=task_3
    )

    t1 >> t2 >> t3