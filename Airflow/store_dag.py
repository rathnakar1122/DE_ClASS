from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.operators.mysql import MySqlOperator
from airflow.operators.email import EmailOperator

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

# Define the DAG
dag = DAG(
    "store_dag",
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
)

# Define a Python callable (example placeholder for your data cleaner script)
def data_cleaner():
    # Add your data cleaning logic here
    print("Cleaning data...")

# Define tasks
t1 = BashOperator(
    task_id='check_file_exists',
    bash_command='gsutil ls gs://task_hiscox_use_cases/raw_store_transactions.csv',
    retries=3,
    retry_delay=timedelta(seconds=15),
    dag=dag
)

t2 = PythonOperator(
    task_id='clear_raw_data',
    python_callable=data_cleaner,
    dag=dag
)

t3 = MySqlOperator(
    task_id='create_table',
    mysql_conn_id='mysql_conn',
    sql='create_table.sql',
    dag=dag
)

t4 = MySqlOperator(
    task_id='insert_data',
    mysql_conn_id='mysql_conn',
    sql='insert_data.sql',
    dag=dag
)

t5 = MySqlOperator(
    task_id='check_data',
    mysql_conn_id='mysql_conn',
    sql='SELECT * FROM store_transactions',
    dag=dag
)

t6 = BashOperator(
    task_id='move_file_raw_to_processed',
    bash_command='gsutil mv gs://task_hiscox_use_cases/raw_store_transactions.csv '
                 'gs://task_hiscox_use_cases/processed_store_transactions.csv',
    dag=dag
)

t7 = BashOperator(
    task_id='move_file_clean_to_processed',
    bash_command='gsutil mv gs://task_hiscox_use_cases/clean_store_transactions.csv '
                 'gs://task_hiscox_use_cases/processed_store_transactions.csv',
    dag=dag
)

t8 = EmailOperator(
    task_id="send_email",
    to="example@gmail.com",
    subject="Daily report generated",
    html_content="<h1>Congrats! Your daily report is ready.</h1>",
    dag=dag
)

# Set task dependencies
t1 >> t2 >> t3 >> t4 >> t5 >> t6 >> t7 >> t8
