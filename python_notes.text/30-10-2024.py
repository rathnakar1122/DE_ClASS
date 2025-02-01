++++++++++++++++++
7:45 AM 10.30.2024
++++++++++++++++++

*******************
 GCP Data Engineer
******************* 

Cloud Run Functions:(Gen1, Gen2)

Develop and Deployment:

Develop:
--------
1. Console - Inline Editor:

Cloud Run Functions:
    1. Create Functions
        1. Configuration:
            Basics: Environement, Function_name, Region - we need to provide
            Trigger: Trigger Type --> [Http, Event-Based(Different Products/Services)]
            Runtime, build, connections and security settings:
            RunTime:
                RunTime-Memory allocated:[128 mb to 32 gb - by default we get 256 mb]
                vCPUS:[0.083 to 8 vCPUS - by default we get 0.167 ]
                TimeOut:[Http Trigger - 60 minutes - 3600 seconds, Event-Based - 9 mins - 540 seconds]
                Concurancy: The maximum number of concurrent requests that can reach each container instance.
                Runtime service account: compute engine default seviceaccunt. By default Cloud Functions uses the automatically created Default Compute Engine Service Account.
        2. Code:
            Runtime: Runtime for the function. Can be changed after deployment.
                     [python , java, ruby, go, .net, php, nodejs]
            EntryPoint: Entry point to your code, e.g. the exported function name.
                        In the below source code - hello_http is the entry point for function.
                        
                        import functions_framework

                        @functions_framework.http
                        def hello_http(request):
                            pass
                            
            Source Code: [Inline Editor - console, ZIP from GCS]
                main.py
                requirements.txt
                
            
        
        
2. Local IDE - SDK Support:
You can view your function in the Cloud Console here: https://console.cloud.google.com/functions/details/us-central1/bigquerytogsheets?project=woven-name-434311-i8

buildConfig:
  automaticUpdatePolicy: {}
  build: projects/840233991363/locations/us-central1/builds/2a4c254b-6ede-4edc-bb1d-80ee70bc3bae
  dockerRegistry: ARTIFACT_REGISTRY
  dockerRepository: projects/woven-name-434311-i8/locations/us-central1/repositories/gcf-artifacts
  entryPoint: bq_to_gsheets_cloud_func
  runtime: python311
  serviceAccount: projects/woven-name-434311-i8/serviceAccounts/840233991363-compute@developer.gserviceaccount.com
  source:
    storageSource:
      bucket: gcf-v2-sources-840233991363-us-central1
      generation: '1730257029575070' # object versioning
      object: bigquerytogsheets/function-source.zip
  sourceProvenance:
    resolvedStorageSource:
      bucket: gcf-v2-sources-840233991363-us-central1
      generation: '1730257029575070'
      object: bigquerytogsheets/function-source.zip
createTime: '2024-10-30T02:57:09.855313887Z'
environment: GEN_2
labels:
  deployment-tool: cli-gcloud
name: projects/woven-name-434311-i8/locations/us-central1/functions/bigquerytogsheets
serviceConfig:
  allTrafficOnLatestRevision: true
  availableCpu: '0.1666'
  availableMemory: 256M
  environmentVariables:
    LOG_EXECUTION_ID: 'true'
  ingressSettings: ALLOW_ALL
  maxInstanceCount: 100
  maxInstanceRequestConcurrency: 1
  revision: bigquerytogsheets-00001-rum
  service: projects/woven-name-434311-i8/locations/us-central1/services/bigquerytogsheets
  serviceAccountEmail: 840233991363-compute@developer.gserviceaccount.com
labels:
  deployment-tool: cli-gcloud
name: projects/woven-name-434311-i8/locations/us-central1/functions/bigquerytogsheets
serviceConfig:
  allTrafficOnLatestRevision: true
  availableCpu: '0.1666'
  availableMemory: 256M
  environmentVariables:
    LOG_EXECUTION_ID: 'true'
  ingressSettings: ALLOW_ALL
  maxInstanceCount: 100
  maxInstanceRequestConcurrency: 1
  revision: bigquerytogsheets-00001-rum
  service: projects/woven-name-434311-i8/locations/us-central1/services/bigquerytogsheets
  serviceAccountEmail: 840233991363-compute@developer.gserviceaccount.com
name: projects/woven-name-434311-i8/locations/us-central1/functions/bigquerytogsheets
serviceConfig:
  allTrafficOnLatestRevision: true
  availableCpu: '0.1666'
  availableMemory: 256M
  environmentVariables:
    LOG_EXECUTION_ID: 'true'
  ingressSettings: ALLOW_ALL
  maxInstanceCount: 100
  maxInstanceRequestConcurrency: 1
  revision: bigquerytogsheets-00001-rum
  service: projects/woven-name-434311-i8/locations/us-central1/services/bigquerytogsheets
  serviceAccountEmail: 840233991363-compute@developer.gserviceaccount.com
serviceConfig:
  allTrafficOnLatestRevision: true
  availableCpu: '0.1666'
  availableMemory: 256M
  environmentVariables:
    LOG_EXECUTION_ID: 'true'
  ingressSettings: ALLOW_ALL
  maxInstanceCount: 100
  maxInstanceRequestConcurrency: 1
  revision: bigquerytogsheets-00001-rum
  service: projects/woven-name-434311-i8/locations/us-central1/services/bigquerytogsheets
  serviceAccountEmail: 840233991363-compute@developer.gserviceaccount.com
  availableMemory: 256M
  environmentVariables:
    LOG_EXECUTION_ID: 'true'
  ingressSettings: ALLOW_ALL
  maxInstanceCount: 100
  maxInstanceRequestConcurrency: 1
  revision: bigquerytogsheets-00001-rum
  service: projects/woven-name-434311-i8/locations/us-central1/services/bigquerytogsheets
  serviceAccountEmail: 840233991363-compute@developer.gserviceaccount.com
  environmentVariables:
    LOG_EXECUTION_ID: 'true'
  ingressSettings: ALLOW_ALL
  maxInstanceCount: 100
  maxInstanceRequestConcurrency: 1
  revision: bigquerytogsheets-00001-rum
  service: projects/woven-name-434311-i8/locations/us-central1/services/bigquerytogsheets
  serviceAccountEmail: 840233991363-compute@developer.gserviceaccount.com
  ingressSettings: ALLOW_ALL
  maxInstanceCount: 100
  maxInstanceRequestConcurrency: 1
  revision: bigquerytogsheets-00001-rum
  service: projects/woven-name-434311-i8/locations/us-central1/services/bigquerytogsheets
  serviceAccountEmail: 840233991363-compute@developer.gserviceaccount.com
  maxInstanceCount: 100
  maxInstanceRequestConcurrency: 1
  revision: bigquerytogsheets-00001-rum
  service: projects/woven-name-434311-i8/locations/us-central1/services/bigquerytogsheets
  serviceAccountEmail: 840233991363-compute@developer.gserviceaccount.com
  revision: bigquerytogsheets-00001-rum
  service: projects/woven-name-434311-i8/locations/us-central1/services/bigquerytogsheets
  serviceAccountEmail: 840233991363-compute@developer.gserviceaccount.com
  timeoutSeconds: 60
  serviceAccountEmail: 840233991363-compute@developer.gserviceaccount.com
  timeoutSeconds: 60
  uri: https://bigquerytogsheets-erxabs66kq-uc.a.run.app
state: ACTIVE
  timeoutSeconds: 60
  uri: https://bigquerytogsheets-erxabs66kq-uc.a.run.app
state: ACTIVE
  uri: https://bigquerytogsheets-erxabs66kq-uc.a.run.app
state: ACTIVE
updateTime: '2024-10-30T02:58:53.878209892Z'
url: https://us-central1-woven-name-434311-i8.cloudfunctions.net/bigquerytogsheets
PS C:\GCP-DE\SuperGCP\Cloud-Run-Functions\bigquery-to-gsheets>


Deployment:
-----------
1. Console
2. Test and Deployment from Locally* Yes


Trigger:
---------
1. Cloud Scheduler
2. Workflows
3. Event Base/Http Trigger 



Scenario-Based Question:
--------------------------
1. You provided all the resource allocation for your GCRF. But It is an Event-Based Triggering. It is failing to run that cloud function within the time limit/timeout - 540 seconds. Then, What is your next step should be?

Ans: We need  to go with further deployments - means - we need to go with other processing tools like: Pyspark, Beam - along with Airflow -
