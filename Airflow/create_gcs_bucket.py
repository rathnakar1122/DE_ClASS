from datetime import datetime
from airflow import DAG
from airflow.providers.google.cloud.operators.gcs import GoogleCloudStorageCreateBucketOperator

# Define your Google Cloud project and Airflow GCS connection ID
GCP_PROJECT_ID = "rathnakar-18m85a0320-hiscox"
GCS_CONN_ID = "google_cloud_default"

# Define bucket naming pattern with the current date and time
BUCKET_NAME_TEMPLATE = "INCIDENT_{{ ts_nodash }}"  # Use Jinja2 templating for dynamic naming

# Define the DAG
with DAG(
    dag_id="create_gcs_bucket_every_5_min",  # Updated DAG ID
    start_date=datetime(2024, 12, 15),
    schedule_interval="*/5 * * * *",  # Run every 5 minutes
    catchup=False,
    tags=["example", "gcs"],
) as dag:

    # Task to create a GCS bucket
    create_bucket = GoogleCloudStorageCreateBucketOperator(
        task_id="create_gcs_bucket",
        bucket_name=BUCKET_NAME_TEMPLATE,  # Dynamic bucket name using Jinja2 template
        project_id=GCP_PROJECT_ID,
        gcp_conn_id=GCS_CONN_ID,
    )

    create_bucket
