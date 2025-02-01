++++++++++++++++++
7:45 AM 10.26.2024
++++++++++++++++++

*******************
 GCP Data Engineer
******************* 
____________
<-AGENDA->  
------------

1. Python Interview Questions[LeetCode]

Problem: Group Anagrams
Difficulty: Medium

Description:
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]



2. GCS -  Bucket Creation - Done

Resource Higerachy:

GCP: 
    Organisation:
        Folders:
            Projects:
                Services/Products:[gcs, bigquery, cloud sql, pubsub, dataflow]:
                
GCP: 
    Organisation:
        Folders:
            Projects:
                Services/Products:[gcs]:
                    Buckets:
                        Folders/Obejcts:

Container: in the form of objects - We do call them objects or blobs


Methods: Console, CLI, Terraform, Client Libraries, airflow dag

Airflow DAG:
    ClientLibrary - PythonOperator
    CLI - BashOperator 
    
Choosing A Location:
--------------------
1. Multi-region Bucket:
    @ Highest availability across largest area[no guaranty]

2. Dual-region:
    @ High availability and low latency across 2 regions
    
3. Region: 
    @ Lowest latency within a single region
   
Choose a storage class for your data:
-------------------------------------
It depends on the object's usage predictability:

Standard, Nearline, Coldline, Archival:

Standard: Highest Cost
@ Best for short-term storage and frequently accessed data
Business: Flipkart: Daily Orders Raw Data - Regular Storage - Retrival UseCase 

Nearline:
@ Best for backups and data accessed less than once a month
Business: Flipkart: Daily Orders RDBMS Data - Backup Storage - Retrival UseCase 

Coldline:
Best for disaster recovery and data accessed less than once a quarter

Archival: Loweset Cost
@ Best for long-term digital preservation of data accessed less than once a year
Business: Flipkart: Daily Orders Raw Data - Historical/Archival Storage - Retrival UseCase

Applies to all objects in your bucket unless you manually modify the class per object or set object lifecycle rules. Best when your usage is highly predictable.


Pricing:

@ A storage class sets costs for (1) storage, 5GB - Free
                                 (2) retrieval, 
                                 (3) and operations(Class A, Class B and Free Operation)
                                 , with minimal differences in uptime. 

Link:
-----
https://cloud.google.com/storage/pricing?_gl=1*1yzpe0t*_up*MQ..&gclid=CjwKCAjwg-24BhB_EiwA1ZOx8kPe3VlICfmJCJfkZDTldgKHKdBqQZl8Vxl_ATgHFMkQwTB5uF0iBBoCBl4QAvD_BwE&gclsrc=aw.ds#multi-regions

gcloud storage ls --> Class A:

Autoclass manages your objects in the following ways:
    @ All data is stored in Standard class for the first 30 days
    @ Data that hasn't been accessed for 30 days will transition to colder storage classes
    @ Colder data that gets accessed will transition to Standard class
    @ Objects smaller than 128KB will be excluded from Autoclass management and will always remain in Standard class
    @ All operations for Autoclass buckets will be charged at Standard class rates

Rsync:

gcs-bucket - gs://my-gs-bucket
    object1.csv
    object2.json*
    
    
s3-bucket - s3://my-s3-bucket 
    object2.json*
    object1.csv
    
gcloud storage rsync gs://my-gs-bucket s3://my-s3-bucket --recursive --delete-unmatched-destination-objects  


Interesting:
Rsync:

gcs-bucket - gs://my-gs-bucket 
    
    
s3-bucket - s3://my-s3-bucket 
    object2.json 
    object1.csv
    
gcloud storage rsync gs://my-gs-bucket s3://my-s3-bucket --recursive --delete-unmatched-destination-objects  


2. S3 - Bucket Creation - 

Methods: Console, Cloud Shell
  

3. Cloud SQL*(GCP)

Methods: Console, CLI, Terraform, ClientLibrary

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


4. Cloud Functions*[FaaS]

5. Mandatory Tasks
   1. Running Dataflow job from Cloud Shell and Local Shell
   2. CommandLine - Creating Buckets, SQL server
      gcloud storage create bucket gs://bucketname --location='us'
   3. Terraform - Creating GCP Resources(GCS Bucket*, BQ, Cloud SQL*, VMs, DFlow Jobs)
   5. ClientLibrary: Creating Buckets
   