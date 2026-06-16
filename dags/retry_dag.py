from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

count = 0

def fail_then_success():
    global count

    count += 1

    print(f"Lan chay: {count}")

    if count < 3:
        raise Exception("Task bi loi")

    print("Thanh cong")

with DAG(
    dag_id="retry_dag",
    start_date=datetime(2025,1,1),
    schedule=None,
    catchup=False,
    default_args={
        "retries": 3,
        "retry_delay": timedelta(seconds=10)
    }
) as dag:

    task = PythonOperator(
        task_id="retry_task",
        python_callable=fail_then_success
    )