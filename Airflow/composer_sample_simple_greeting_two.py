from airflow import models
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import datetime

# Default arguments
default_dag_args = {
    'start_date': datetime.datetime(2021, 1, 1),
}

# Define the DAG
with models.DAG(
    'composer_sample_simple_greeting_two',
    schedule_interval=datetime.timedelta(days=1),
    default_args=default_dag_args,
) as dag:

    # Python task: Greeting
    def greeting():
        import logging
        logging.info('Hello World!')

    hello_python = PythonOperator(
        task_id='hello',
        python_callable=greeting,
    )

    # Bash task: Goodbye
    goodbye_bash = BashOperator(
        task_id='bye',
        bash_command='echo goodbye',
    )

    # Define task dependencies
    hello_python >> goodbye_bash
