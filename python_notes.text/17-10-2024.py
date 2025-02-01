#####################
 Date: 17-10-2024
#####################
+++++++++++++++++++++++++++ 
GCP Cloud Data Engineering:
+++++++++++++++++++++++++++
#################################
  Topic: (Apache Beam[Dataflow])
#################################  




Apache Beam - 


pipeline

p ---> Parallel
pcollection - input - 10 records - 10 lakhs - 1m -- 10m records  input -- 

Parallel processing is a (dataflow runner)
	>> computing/claculation/transformation method that uses 
			>> multiple processors/multiple machines/compute engines/ec2 machines to simultaneously process tasks.
pcollection >> 1 first ptransformation >> output1
output1 >> 2nd ptransformation >> output2
output2 >> 3rd ptransformation	>> finalout - pcollection 

csv - 

10 columns 

age - >= 18 - first ptransformation - filter on age columns
gender == female - 2nd ptransformation

ouptu - gcs 
		
			
Task1:
-------
we have 1 hard copy:
we need to get it xeroxed 300 copies
we have a printer which can produce 50 outputs for an hour
we need to finish doing xeroxes 300 copies with in hour --

6 machines -- 1 hour - cloud - past - worker configuration set - no of machines, ram, storage

*data will be destributed among all the worker-nodes - that is called parallel processing

 
 1. Local Runner/Direct Runner/Dataflow Runner/flink/spark:
 ----------------------------------------------------------
 Clothes - Self, Worker, Washing Machine 
 
 
 Apache Beam is a unified model for defining both batch and streaming data-parallel processing pipelines. To get started with Beam, youâ€™ll need to understand an important set of core concepts:

Pipeline - A pipeline is a user-constructed graph of transformations that defines the desired data processing operations.


PCollection - A PCollection is a data set or data stream. The data that a pipeline processes is part of a PCollection.


PTransform - A PTransform (or transform) represents a data processing operation, or a step, in your pipeline. A transform is applied to zero or more PCollection objects, and produces zero or more PCollection objects.

 
User-defined function (UDF) - Some Beam operations allow you to run user-defined code as a way to configure the transform.
 
SDK - A language-specific library(python, java, go) that lets pipeline authors build transforms, construct their pipelines, and submit them to a runner.


Runner - A runner runs a Beam pipeline using the capabilities of your chosen data processing engine.


# Gcloud Auth Settings:
===========================
PS D:\SuperGCPClasses> gcloud auth list
      Credentialed Accounts
ACTIVE  ACCOUNT
*       bhaskargsbalina@gmail.com
        gcpcloud305@gmail.com
        lavu2018hani@gmail.com

To set the active account, run:
    $ gcloud config set account ACCOUNT



Updates are available for some Google Cloud CLI components.  To install them,
please run:
  $ gcloud components update

PS D:\SuperGCPClasses> 

PS D:\SuperGCPClasses> gcloud config set account gcpcloud305@gmail.com
Updated property [core/account].
PS D:\SuperGCPClasses> gcloud auth list
      Credentialed Accounts
ACTIVE  ACCOUNT
        bhaskargsbalina@gmail.com        
*       gcpcloud305@gmail.com
        lavu2018hani@gmail.com

To set the active account, run:
    $ gcloud config set account ACCOUNT

PS D:\SuperGCPClasses> gcloud auth login

it directs to the gmail account 

You are now logged in as [gcpcloud305@gmail.com].
Your current project is [dev-project-433015].  You can change this setting by running:
  $ gcloud config set project PROJECT_ID
PS D:\SuperGCPClasses>  

gcloud config set project woven-name-434311-i8


gcloud projects list

===========================================================================================================
import apache_beam as beam #  
from apache_beam.options.pipeline_options import PipelineOptions

# EXTERNAL SOURCE
gcs_input_path = 'gs://gcp35batch/texfile.csv' # it is not - in-memory data source - It is an External Source - 
gcs_output_path = 'gs://gcp35batch/output/texfile.csv' # it is not - in-memory data source - It is an External Source 
# Then there is no requirement of exteranl udf creation

options = PipelineOptions(
        project='woven-name-434311-i8',
        region='us-central1',
        temp_location='gs://gcp35batch/temp_folder',
        staging_location='gs://gcp35batch/staging',
        runner='DataflowRunner',
        job_name='example-dataflow-job'
    )

def Eleminating_last_char(element): 
    # print(element.split()[1][0:len(element.split()[1])-1]) 
    row = element.split() # when you split any string object - it will create a list object by following delimeter space
    result = striping_last_unnecessory_character(row)
    output = ",".join(result)
    return output

def striping_last_unnecessory_character(list):
    emptylist = []
    for i in range(len(list)-1): 
        emptylist.append(list[i][:len(list[i])-1])
        
    emptylist.append(list[len(list)-1])
    
    return emptylist



with beam.Pipeline(options=options) as pipeline:
    pcollection = pipeline | 'Creating input Pcollection' >> beam.io.ReadFromText(gcs_input_path, skip_header_lines=1)
    transformation1 = pcollection | 'Name to be uppercased using UDF' >> beam.Map(Eleminating_last_char) 
    result = transformation1 | 'writing to the local path' >> beam.io.WriteToText(gcs_output_path)

'''
class Pipeline(
    runner: str | PipelineRunner | None = None,
    options: PipelineOptions | None = None,
    argv: List[str] | None = None,
    display_data: Dict[str, Any] | None = None
)

'''
There was an error generating a response

