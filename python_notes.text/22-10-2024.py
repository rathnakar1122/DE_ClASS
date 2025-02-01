 ++++++++++++++++++
7:45 AM 10/22/2024
++++++++++++++++++

*******************
 GCP Data Engineer
*******************

____________
AGENDA-> GCS
------------

1. Python Interview Questions[LeetCode]
2. GCS
3. SQL*
4. Cloud Functions*
5. Mandatory Tasks

Contenet:
---------
1. Python Interview Questions[LeetCode]
# a list of dictionaries
# Input:
cars = [
    {
        "make": "Toyota",
        "model": "Camry",
        "year": 2020,
        "price": 24000
    },
    {
        "make": "Honda",
        "model": "Civic",
        "year": 2021,
        "price": 22000
    },
    {
        "make": "Tesla",
        "model": "Model 3",
        "year": 2022,
        "price": 40000
    }
]

#Output:
list_of_car_makers = [ "Toyota","Honda","Tesla"]
:Hints:
Inner object --> Dict
   deep_inner --> String
Outer object --> List
< use both list, dict and str methods along with slicing >

2. GCS[Real Time Project]
Step 1: Create a Google Cloud Storage Bucket
1.	Go to the GCP Console.
2.	Navigate to Storage > Browser.
3.	Click on Create Bucket.
4.	Follow the prompts to set up your bucket, including naming it and choosing the appropriate location and storage class.

Step 2: Enable Cloud SQL API
1.	In the GCP Console, go to APIs & Services > Library.
2.	Search for and enable the Cloud SQL Admin API if itâ€™s not already enabled.
This is already enabled for our project

Step 3: Create a Service Account
1.	Go to IAM & Admin > Service Accounts.
2.	Click on Create Service Account.
3.	Name the account and assign it the necessary roles (e.g., Cloud SQL Admin and Storage Object Admin).
4.	Create a key for the service account and save it securely.




Interview Questions:
--------------------
1. What is IAM?
2. What is a Service Account(SA)?
A service account represents a Google Cloud service identity, such as code running on Compute Engine VMs, App Engine apps, or systems running outside Google.
3. What is a Principal?
4. What is the difference between SA and User Account?
5. What is a string slicing?
6. What is the difference between List and Dictionary?
7. Can you please break the emailid(given below) down?
Email address: sqltogcsexport@woven-name-434311-i8.iam.gserviceaccount.com
8. What is a SA key? What format it could be?
9. What is prime most alternative that we see of late in lieu of SA keys?
10. What is a json object in Python?
11. What is the difference between json and dict objects in python?


Project/Assignment:
-------------------
Storage Classes[4][Access Priority]

Standard[daily]
Best for short-term storage and frequently accessed data:
    --> 1 day, 2 days - Landing Zone - Eevery Day Business -- delete

Nearline[monthly once]
Best for backups and data accessed less than once a month

Coldline[once a quarter]
Best for disaster recovery and data accessed less than once a quarter

Archive[once a year]
Best for long-term digital preservation of data accessed less than once a year

Explanation:
Ref Link:
---------
https://cloud.google.com/storage/docs/storage-classes?_gl=1*1lh32rh*_ga*ODgzNjMzOTc0LjE3Mjc2ODg5NTg.*_ga_WH2QY8WWF5*MTcyOTU2Mzg1MC4yMS4xLjE3Mjk1NjU1OTIuNTkuMC4w#key-concepts
