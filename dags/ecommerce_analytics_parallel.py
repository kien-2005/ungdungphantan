from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import time


def sales_report():
    print("Phân tích doanh thu...")
    time.sleep(10)


def customer_report():
    print("Phân tích khách hàng...")
    time.sleep(10)


def product_report():
    print("Phân tích sản phẩm...")
    time.sleep(10)


def summary_report():
    print("Tổng hợp báo cáo...")
    time.sleep(3)


with DAG(
    dag_id="ecommerce_analytics_parallel",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    start_sales = PythonOperator(
        task_id="sales_report",
        python_callable=sales_report
    )

    start_customer = PythonOperator(
        task_id="customer_report",
        python_callable=customer_report
    )

    start_product = PythonOperator(
        task_id="product_report",
        python_callable=product_report
    )

    summary = PythonOperator(
        task_id="summary_report",
        python_callable=summary_report
    )

    [start_sales, start_customer, start_product] >> summary