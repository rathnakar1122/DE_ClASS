import datetime
from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from airflow.providers.google.cloud.transfers.bigquery_to_gcs import BigQueryToGCSOperator
from airflow.utils.dates import days_ago


default_dag_args = {
    'start_date': days_ago(1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=5),
}

output_files = 'gs://task_hiscox_use_cases/transfer.csv'

with DAG(
    dag_id='demo_bigquery_gcs_dag',
    schedule_interval=datetime.timedelta(days=1),
    default_args=default_dag_args,
) as dag:
    bq_airflow_commits_query = BigQueryInsertJobOperator(
        task_id='bq_airflow_commits_query',
        configuration={
            "query": {
                "query": "SELECT * FROM `rathnakar-18m85a0320-hiscox.MAIN.TEACHER` LIMIT 100",
                "useLegacySql": False,
            }
        },
    )

    export_commit_to_gcs = BigQueryToGCSOperator(
        task_id='export_airflow_commits_to_gcs',
        source_project_dataset_table='rathnakar-18m85a0320-hiscox.MAIN.TEACHER',
        destination_cloud_storage_uris=[output_files],
        export_format='CSV',
    )

    bq_airflow_commits_query >> export_commit_to_gcs
