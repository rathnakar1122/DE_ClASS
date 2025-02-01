"++++++++++++++++++
7:45 AM 10.25.2024
++++++++++++++++++

*******************
 GCP Data Engineer
******************* 
____________
AGENDA-> GCS
------------

1. Python Interview Questions[LeetCode]

Test1:
    
input_string = 'ccccc'

output_largest_substring = 'c'

Test1:
    
input_string = 'ccabcccc'

output_largest_substring = 'abc' or 'cab'

Note: Write A Python Function which can take in user's input as string formate and returns largest substring with non repeated characters.



2. GCS -  Bucket Creation - Done

Methods: Console, CLI, Terraform, Client Libraries

Airflow DAG:
    ClientLibrary - PythonOperator
    CLI - BashOperator

from airflow import DAG
from airflow.operators.python import PythonOperator # Client Library
from airflow.operators.bash import BashOperator # Command Line
from google.cloud import storage
from datetime import datetime

# Define the Python function to create a GCS bucket
def create_bucket(bucket_name):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    if not bucket.exists():
        bucket = client.create_bucket(bucket_name)
        print(f"Bucket {bucket_name} created.")
    else:
        print(f"Bucket {bucket_name} already exists.")

# Define the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 10, 1),
}

with DAG(
    dag_id='create_gcs_bucket_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag:

    # Task 1: Create GCS bucket using PythonOperator
    create_bucket_python_task = PythonOperator(
        task_id='create_gcs_bucket_python',
        python_callable=create_bucket, # we are calling the function
        op_kwargs={'bucket_name': '<you can give your bucket name here>'},  # Bucket name set to 'dag-bucket'
    )

    # Task 2: Create GCS bucket using BashOperator (gsutil command)
    create_bucket_bash_task = BashOperator(
        task_id='create_gcs_bucket_bash',
        bash_command='gsutil mb <you can give your bucket name here>'  # Bucket name set to 'dag-bucket'
    )

    # Define the task execution order
    create_bucket_python_task >> create_bucket_bash_task    

2. S3 - Bucket Creation - 

Methods: Console, Cloud Shell
  

3. Cloud SQL*(GCP)

Methods: Console, CLI, Terraform, ClientLibrary

# we can create 3 types of instance - 

Postgres - OLTP
MSSQL - OLTP
MySQL - OLTP


@ Steps in Creation of 'Cloud SQL instance for MySQL Server' from Console:

Choose a Cloud SQL edition:
    Enterprise Plus
    Enterprise
@ Steps in Creation of 'Cloud SQL instance for MySQL Server' from CLI:
    
gcloud sql instances create my-sql-server-instance \
    --database-version=MYSQL_8_0 \
    --tier=db-n1-standard-1 \
    --region=us-central1 \
    --root-password=mysecretpassword
    
@ Steps in Creation of 'Cloud SQL instance for MySQL Server' from Terraform:   
    
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  project = "woven-name-434311-i8"
}

# Create a new MySQL 8.0 instance in the US multi-region
resource "google_sql_database_instance" "main" {
  name             = "e-commerce"
  database_version = "MYSQL_8_0"
  region           = "us-central1"

  settings {
    # Second-generation instance tiers are based on the machine
    # type. See argument reference below.
    tier = "db-f1-micro"
  }
}


terraform init, validate, plan, apply

Questions:
----------
1. What is OLTP?
2. What is OLAP Server?
3. Difference between Both of them?
4. What is SLA?
5. IO Ops?
IOPS are input/output operations per second: the number of read or write operations your disk can handle per second.
6. What is resoring point in windows?

Flipkart - Product - 3 business - SLA - 
         - Refund - 10 days - return - SLA 
         



4. Cloud Functions*

5. Mandatory Tasks
   1. Running Dataflow job from Cloud Shell and Local Shell
   2. CommandLine - Creating Buckets, SQL server
      gcloud storage create bucket gs://bucketname --location='us'
   3. Terraform - Creating GCP Resources(GCS Bucket*, BQ, Cloud SQL*, VMs, DFlow Jobs)
   5. ClientLibrary: Creating Buckets
   



IaaS -- Compute Engine[machine maintance]
PaaS -- Platform - MySQL Server[maintaince] - Database, Tables 
Cloud SQL uses Compute Engine virtual machines with persistent storage disks



"
 content://com.whatsapp.provider.media/item/0d00fa1d-a01b-4df5-93b7-18608c854168#:~:text=%2B%2B%2B%2B%2B%2B%2B%2B%2B%2B%2B%2B%2B%2B%2B%2B%2B%2B%0A7%3A45%20AM,persistent%20storage%20disks