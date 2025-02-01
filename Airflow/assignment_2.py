from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator  # Corrected import path and typo in "BashOperator"
from airflow.operators.dummy import DummyOperator  # Correct import path
from airflow.operators.python import PythonOperator  # Correct import path
from airflow.providers.mysql.operators.mysql import MySqlOperator  # Corrected import path for MySqlOperator

default_args = {
    "owner" : "airflow",
    "start_date" : datetime(2021, 1, 1),
    "retries " : 1, 
    "retry_delay" : timedelta(minutes=5)

}

#dag=DAG ("store_dag",default_args = default_args, schedule_interval='@daily', catchup=False)
dag = DAG("store_dag", default_args= default_args, schedule_interval= '@daily', catchup=False)

t1 = BashOperator(task_id = 'check_file_exists,'
                  bash_cammand= 'gs://task_hiscox_use_cases/raw_store_transactions.csv',
                  retries=3,
                  retries_delay=timedelta(seconds=10),
                  dag=dag)

t2 = PythonOperator (task_id='clean_raw_csv', 
                     python_callable='gs://task_hiscox_use_cases/datacleaner.py', 
                     dag=dag)
t3 = MySqlOperator (task_id='create_table',
                    mysql_conn_id='mysql_conn',
                    sql='create_table.sql',
                    dag=dag)

t1>>t2>>t3