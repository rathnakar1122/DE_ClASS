from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator

# Sample Python callable function
def data_cleaner():
    print("Cleaning raw CSV data...")

# Default arguments for the DAG
default_args = {
    "owner": "airflow",
    "start_date": datetime(2021, 1, 1),
    "retries": 1,  # Removed extra space
    "retry_delay": timedelta(minutes=5),
}

# Define the DAG
dag = DAG(
    "store_dag",
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
)

# Task 1: Check if the file exists
t1 = BashOperator(
    task_id="check_file_exists",
    bash_command="gsutil ls gs://task_hiscox_use_cases/raw_store_transactions.csv",
    retries=3,
    retry_delay=timedelta(seconds=10),
    dag=dag,
)

# Task 2: Clean the raw CSV file
t2 = PythonOperator(
    task_id="clean_raw_csv",
    python_callable=data_cleaner,
    dag=dag,
)

# Task 3: Create a MySQL table
t3 = MySqlOperator(
    task_id="create_table",
    mysql_conn_id="mysql_conn",
    sql="""
        CREATE TABLE IF NOT EXISTS store_transactions (
            transaction_id INT AUTO_INCREMENT PRIMARY KEY,
            store_id INT NOT NULL,
            product_id INT NOT NULL,
            quantity INT NOT NULL,
            transaction_date DATE NOT NULL
        );
    """,
    dag=dag,
)

# Task dependencies
t1 >> t2 >> t3
