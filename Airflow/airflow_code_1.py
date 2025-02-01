from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 1, 6),
    "email_on_failure": False,
    "email_on_retry": False,
    "email": ["airflow@airflow.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG("tutorial", default_args=default_args, schedule_interval=timedelta(days=1))

# Task 1: Print date
t1 = BashOperator(
    task_id="print_date",
    bash_command="date",
    dag=dag
)

# Task 2: Sleep for 5 seconds
t2 = BashOperator(
    task_id="sleep",
    bash_command="sleep 5",  # Fixed typo in 'bash_command'
    retries=3,
    dag=dag
)

# Task 3: Use a templated command
templated_command = """
{% for i in range(5) %}
echo "{{ ds }}"
echo "{{ macros.ds_add(ds, 7) }}"
echo "{{ params.my_param }}"
{% endfor %}
"""

t3 = BashOperator(
    task_id="templated",
    bash_command=templated_command,  # Fixed typo in 'bash_command'
    params={"my_param": "parameter 1 passed in"},  # Fixed syntax
    dag=dag
)

# Set task dependencies
t1.set_downstream(t2)
t2.set_downstream(t3)

# with DAG ()
# with DAG(
#     "example_dag",  # Name of the DAG
#     default_args=default_args,
#     description="An example DAG",
#     schedule_interval=timedelta(days=1),  # Run once a day
#     catchup=False,  # Don't backfill past runs
# ) as dag:
#     # Define tasks
#     task1 = BashOperator(
#         task_id="print_date",
#         bash_command="date",
#     )

#     task2 = BashOperator(
#         task_id="echo_hello",
#         bash_command="echo 'Hello, World!'",
#     )

#     # Set task dependencies
#     task1 >> task2
