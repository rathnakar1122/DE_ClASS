++++++++++++++++++
7:45 AM 10.29.2024
++++++++++++++++++

*******************
 GCP Data Engineer
******************* 
____________
<-AGENDA->  
------------

1. DE UseCase

2. GCS - Uniform/FineGrained 

Choose how to control object access in this bucket.


Uniform:
Ensure uniform access to all objects in the bucket by using only bucket-level permissions (IAM). This option becomes permanent after 90 days.



Fine-grained
Specify access to individual objects by using object-level permissions (ACLs) in addition to your bucket-level permissions (IAM).


Uniform - School(bucket) - Access(Dress) - object(student) - level - 

FineGrained - Moderen - Drees -- 

Access - Uniform Bucket - sai@gmail.com, charan@tcs.com 

Uniform Bucket: salesbucket: 
    bucket - level - Access - grant 
    
    sai - read -- all objects - read - 
    
    charan - write -- all object - write and read 
    
FineGrained: salesbucket2: 
    object level - granting - 
    some objects - write, some objects - read - sai@gmail.com, charan@tcs.com 
    
3. Cloud Functions/Cloud Run Functions:

Services - Serverless --> Server exists - on datacentres - provided by Cloud Platforms.
on-prem - you will not be having servers -

BigQuery - TCS -- 
GCS - TCS / Accenture -- Cloud Provider 


Event-driven serverless functions

Cloud Services -- 

GCS -- Bucket Creation, Deletion, Object Creation, Deletion, updation/overwriting

gcs - file - load --> 

object - process - bigquery load -->

 bigquery - table - delete --> notifincation should be sent --
 
 scheduleing - cloud - two types - known shchedule - 2am - 1pm 
                                   unknown schedule - guest  - biryan - event - 

Run your code with zero server management using scalable pay-as-you-go functions as a service (FaaS)


function_one1 -> 

object - csv file - process - bigquery load

1 - container - run - pod 
1,1 - two - thred - 2 simul

1, 2,3,4,5 - 5 process - function - seconds - billing -- 

9 minutes -- seconds -- charge - function code - application - run - seconds - 

airflow - 24/7 - workflow archestration - pay - gke cluster - 

cloud function - 1 mintue - 2$

200$ 2$ -- 202$




Task1/Assignment:
------------------
1. Work on Fine-grained Access Permissions Granting.

VMS - create - 

container - small application 

vms -- gkes -- 

small - big machines - portions of machine - micro servers - 

networking - 

7 layers - share - container - application - microservers --


udf - no of times call 

Micro services - dependencies - individual job 

Container - store - application

container - closed one - disturb -- 

Python(Application) - csv file(gcs) -read - sales - output - (Gcs)