++++++++++++++++++
7:45 AM 10.23.2024
++++++++++++++++++

*******************
 GCP Data Engineer
******************* 
____________
AGENDA-> GCS
------------

1. Python Interview Questions[LeetCode]
list_of_numbers = [1,2,3,4,5,6,7,8,9]

total = 11 

Requirement: We need to create sets having the values - when we add them it should return 11 - 

example: (2,9), (4,7),(5,6)


2. GCS - Bucket Creation
   1. Console
   2. Command Line(Cloud Shell, Local Shell(PS, CMD))
   3. Terraform:
       terraform init
       terraform fmt
       terraform validate
       terraform plan
       terraform apply
       terraform destroy
   4. Client Libraries(Python)
   
from google.cloud import storage
from google.cloud import bigquery


def create_bucket_class_location(bucket_name):
    """
    Create a new bucket in the US region with the coldline storage
    class
    """
    bucket_name = bucket_name

    storage_client = storage.Client(project='woven-name-434311-i8')

    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "COLDLINE"
    new_bucket = storage_client.create_bucket(bucket, location="us")

    print(
        "Created bucket {} in {} with storage class {}".format(
            new_bucket.name, new_bucket.location, new_bucket.storage_class
        )
    )
    return new_bucket

result = create_bucket_class_location(bucket_name='cnn-project-prod-bucket') 
print(result)
  
3. SQL*
4. Cloud Functions*
5. Mandatory Tasks
   1. Running Dataflow job from Cloud Shell and Local Shell
   2. CommandLine - Creating Buckets
      gcloud storage create bucket gs://bucketname --location='us'
   3. Terraform - Creating GCP Resources(GCS Bucket*, BQ, Cloud SQL, VMs, DFlow Jobs)
   5. ClientLibrary: Creating Buckets
   
   
Explanation:
+++++++++++++

IaaS
PaaS
SaaS
FaaS

Rejoin pls -- 

Infrastructure:(GCP, Azure, AWS):
----------------------------------
Network, Systems(VMS,GKES), 
Cloud SQL - Servers
GCS - Buckets
BQ - Datasets, Tables


TCS - Project Manager:
    
CNN project:
    
BigData Processing:
    
100 machines -- indent - network - required software installation - 10 - 
network
sql- admin
software
data
platform/infrastructure/DevOps



BigQuery/SQL:
    
    Table:
        Select * from table;
        
python scripts:
    main.py
        code - run - schedule -- 
        
terraform scripts:
    main.tf
        code(HCL) - run - schedule - provisioning the resources - infrastructure
        
    These files describe the desired state of your infrastructure.
    
    bucket create - update - delete - actions - state 