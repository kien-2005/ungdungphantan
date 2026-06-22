1	Thiết lập cài đặt và kết quả
1.1	Môi trường
Môi trường triển khai gồm:
-	Windows 11.
-	Docker Desktop.
-	Docker Compose.
-	Python 3.13.
-	Apache Airflow 2.9.1.
-	PostgreSQL.
-	Redis.
1.2	Cài đặt
Cấu trúc project được tổ chức như sau:
airflow-project/ |
+-- dags/
|	+-- demo_dag.py
|	+-- parallel_dag.py
|	+-- retry_dag.py
|	+-- ecommerce_order_pipeline.py
|	+-- ecommerce_analytics_parallel.py
|
+-- docker-compose.yaml Khởi động hệ thống bằng lệnh:
docker compose up -d
Sau khi các container chạy thành công, truy cập giao diện Airflow tại:
http://localhost:8080
1.3	Kết quả
Hệ thống khởi động thành công với các dịch vụ chính:
-	Webserver Running.
-	Scheduler Running.
-	Redis Running.
-	PostgreSQL Running.
-	Worker Running.
Giao diện Airflow hiển thị đầy đủ các DAG đã xây dựng. Từ giao diện này, người dùng có thể trigger DAG, theo dõi trạng thái task, xem log và kiểm tra lịch sử chạy.

link demo :https://youtu.be/3kzeFM5zoCc
