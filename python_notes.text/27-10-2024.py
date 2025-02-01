++++++++++++++++++
7:45 AM 10.26.2024
++++++++++++++++++

*******************
 GCP Data Engineer
******************* 
____________
<-AGENDA->  
------------
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
    
    
Protection:
    Soft delete policy - 7 days
    Object versioning - Off
    Bucket retention policy - None
    Object retention - Disabled
    -- 5th - Combination of Bucket and Object Retention
    
Object lifecycle:
    Lifecycle rules - 2 rules:
                    1st rule: max. number of versions per object.
                    2nd rule: Expire non-current versions after
    
Soft delete policy - 7 days:(Data Recovery):
    @ When enabled, this bucket and its objects will be kept for a specified period after they're deleted and can be restored during this time.
    @ I need to raise a ticket for gcp support team - I need to get it back.
    
    1. Use default retention duration:
        All buckets have a 7 day soft delete duration by default, unless this default has been customized by your organization administrator.
    2. Set custom retention duration:
        Specify how long this bucket and its objects should be retained after they're deleted. Setting a "0" duration disables soft delete, meaning any deleted objects will be permanently deleted.
        
        The Provided Granularity for retaining objects:
            .seconds
            .days
            .months
            .Years


Object versioning:
    - Pushpa1, Pushap2
# Obejct Versioning       
        @ Object versioning (For version control)
            For restoring deleted or overwritten objects. To minimize the cost of storing versions, we recommend limiting the number of noncurrent versions per object and scheduling them to expire after a number of days. 
            
        Object - USA_Orders_8:07 PM 10/26/2024.csv - non-current - 'Hellow World' - 1gb - $1 - non-current
                 USA_Orders_8:07 PM 10/26/2024.csv - non-current -  'Hellow something' - 2gb - $2
                 USA_Orders_8:07 PM 10/26/2024.csv - non-current -  'Hellow something'  - 500mb - $0.50
                 USA_Orders_8:07 PM 10/26/2024.csv - Current -  'Hellow something'
                 USA_Orders_8:07 PM 10/26/2024.csv
                 USA_Orders_8:07 PM 10/26/2024.csv
                 USA_Orders_8:07 PM 10/26/2024.csv
                 USA_Orders_8:07 PM 10/26/2024.csv
                 USA_Orders_8:07 PM 10/26/2024.csv
                 USA_Orders_8:07 PM 10/26/2024.csv 
                 
        * the current1 version will be overwriting the prev1
        
        @ limiting the number of noncurrent versions per object can be achieved by setting or selecting the option 
        - max. number of versions per object.  -4- (mandatory selection)
            # If you want overwrite protection, increase the count to at least 2 versions per object. Version count includes live and noncurrent versions.
        
        @ scheduling them to expire after a number of days. can be achieved by setting or selecting the option - 
        - Expire non-current versions after. -2- (mandatory selection)
        7 days recommended for Standard storage class
        
Note: When you select the otions like - object versioning for a bucket creation, it creates two life cycle rules for the objects stored in that bucket.

Object lifecycle:
    Lifecycle rules - 2 rules:
                    1st rule: max. number of versions per object.
                    2nd rule: Expire non-current versions after
                    
Lifecycle actions:
    
A lifecycle rule specifies exactly one of the following actions:

    Delete
    SetStorageClass
    AbortIncompleteMultipartUpload
        Only the following lifecycle conditions can be used with this action:
            age
            matchesPrefix
            matchesSuffix
    
Lifecycle conditions:
A lifecycle rule includes conditions which an object must meet before the action defined in the rule occurs on the object. Lifecycle rules support the following conditions:

    age
    createdBefore
    customTimeBefore
    daysSinceCustomTime
    daysSinceNoncurrentTime
    isLive
    matchesStorageClass
    matchesPrefix and matchesSuffix
    noncurrentTimeBefore
    numNewerVersions
    
    
Ref Link:
---------
https://cloud.google.com/storage/docs/lifecycle?_gl=1*cnj9yl*_ga*MjE0NjM0MjgzMy4xNzI5Nzc3OTEw*_ga_WH2QY8WWF5*MTcyOTk5NzUxOS43LjEuMTcyOTk5OTY2Mi41OS4wLjA.


Extracting - connect - Source:
    -- 
Transformation - Built-in Functions:

Loading - Target: bq, sql, gcs, 