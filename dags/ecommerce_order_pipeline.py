from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import time


def extract_orders():
    print("Đọc dữ liệu đơn hàng...")
    time.sleep(3)


def validate_payment():
    print("Kiểm tra thanh toán...")
    time.sleep(3)


def update_inventory():
    print("Cập nhật tồn kho...")
    time.sleep(3)


def generate_invoice():
    print("Tạo hóa đơn...")
    time.sleep(3)


with DAG(
    dag_id="ecommerce_order_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    t1 = PythonOperator(
        task_id="extract_orders",
        python_callable=extract_orders
    )

    t2 = PythonOperator(
        task_id="validate_payment",
        python_callable=validate_payment
    )

    t3 = PythonOperator(
        task_id="update_inventory",
        python_callable=update_inventory
    )

    t4 = PythonOperator(
        task_id="generate_invoice",
        python_callable=generate_invoice
    )

    t1 >> t2 >> t3 >> t4