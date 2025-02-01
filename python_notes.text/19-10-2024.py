#####################
 Date: 19-10-2024
#####################
+++++++++++++++++++++++++++ 
GCP Cloud Data Engineering:
+++++++++++++++++++++++++++
#################################
  Topic: (Apache Beam[Dataflow])
#################################  


<Python>
-----------
Variable
DataTypes
Variable Declaration
Iterable Objects - string, list, tuple - methods
def <python functions>
lambda - map,reduce, filter
in-built functions
file handling
if, for, 
try exception

<dataflow>[apche-beam]
-----------------------
Pcollection
Ptransformation
Pipeline
Runners[DirectRunner, DataflowRunner]
SDK - Python

L1:
import apache_beam as beam

with beam.Pipeline() as pipeline:
    pass
    
L2:

import apache_beam as beam

list = [2000,3000,4000,5000]

with beam.Pipeline() as pipeline:
    pcoll = pipeline | 'Input pcollection creation' >> beam.Create(list)
    output = pcoll | 'Printing' >> beam.Map(print)
    
    
L3:

import apache_beam as beam

list = [2000,3000,4000,5000]

def Print_Udf(element):
    print(element)
    
with beam.Pipeline() as pipeline:
    pcoll = pipeline | 'Input pcollection creation' >> beam.Create(list)
    output = pcoll | 'Printing' >> beam.Map(Print_Udf)
       

L4:

import apache_beam as beam

list = [2000,3000,4000,5000] # inmemory data source - 

def Increment_func(element):
    return element * 2

def Print_Udf(element):
    print(element)
    
with beam.Pipeline() as pipeline:
    pcoll = pipeline | 'Input pcollection creation' >> beam.Create(list)
    transformation = pcoll | 'Incrementing the values' >> beam.Map(Increment_func)
    output = transformation | 'Printing' >> beam.Map(Print_Udf)
       

L5:

import apache_beam as beam


input_filepath = 'D:/user/UserName/foderName/textfile.csv'

def Increment_func(element):
    return element * 2

def Print_Udf(element):
    print(element)
    
with beam.Pipeline() as pipeline:
    pcoll = pipeline | 'Input pcollection creation' >> beam.io.ReadFromText(input_filepath)
    transformation = pcoll | 'Incrementing the values' >> beam.Map(Increment_func)
    output = transformation | 'Printing' >> beam.Map(Print_Udf)
    
    
    
L6:

import apache_beam as beam


input_filepath = 'D:/user/UserName/input_folderName/textfile.csv'
output_filepath = 'D:/user/UserName/output_folderName/tranformed_textfile.csv'

def Increment_func(element):
    return element * 2

def Print_Udf(element):
    print(element)
    
with beam.Pipeline() as pipeline:
    pcoll = pipeline | 'Input pcollection creation' >> beam.io.ReadFromText(input_filepath)
    transformation = pcoll | 'Incrementing the values' >> beam.Map(Increment_func)
    output = pcoll | 'Printing' >> beam.io.WriteToText(output_filepath)
    
    
    
L7:

import apache_beam as beam


input_gcspath = 'gs://bucket_name/input_folderName/textfile.csv'
output_gcspath = 'gs://bucket_name/output_folderName/tranformed_textfile.csv'

def Increment_func(element):
    return element * 2

def Print_Udf(element):
    print(element)
    
with beam.Pipeline() as pipeline:
    pcoll = pipeline | 'Input pcollection creation' >> beam.io.ReadFromText(input_gcspath)
    transformation = pcoll | 'Incrementing the values' >> beam.Map(Increment_func)
    output = pcoll | 'Printing' >> beam.io.WriteToText(output_gcspath)
    
    
L8:

import apache_beam as beam


input_gcspath = 'gs://bucket_name/input_folderName/textfile.csv'
output_gcspath = 'gs://bucket_name/output_folderName/tranformed_textfile.csv'

def Increment_func(element):
    return element * 2

def Print_Udf(element):
    print(element)
    
with beam.Pipeline(runner='DirectRunner') as pipeline:
    pcoll = pipeline | 'Input pcollection creation' >> beam.io.ReadFromText(input_gcspath)
    transformation = pcoll | 'Incrementing the values' >> beam.Map(Increment_func)
    output = pcoll | 'Printing' >> beam.io.WriteToText(output_gcspath)
    
    
L9:

import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions


input_gcspath = 'gs://bucket_name/input_folderName/textfile.csv'
output_gcspath = 'gs://bucket_name/output_folderName/tranformed_textfile.csv'

options = PipelineOptions(
    project='project_id',
    runner='DataflowRunner',
    region='Region',
    stage_location = 'gs://bucketname/stage'
    temp_location = 'gs://bucketname/temp'
    job_name='etljob'
)


def Increment_func(element):
    return element * 2

def Print_Udf(element):
    print(element)
    
with beam.Pipeline(options=options) as pipeline:
    pcoll = pipeline | 'Input pcollection creation' >> beam.io.ReadFromText(input_gcspath)
    transformation = pcoll | 'Incrementing the values' >> beam.Map(Increment_func)
    output = pcoll | 'Printing' >> beam.io.WriteToText(output_gcspath)
    
    
L10:

import apache_beam as beam 
from apache_beam.options.pipeline_options import PipelineOptions

gcs_inputpath = 'gs://gcp35batch/texfile.csv' # hardcoded
gcs_outputpath = 'gs://gcp35batch/output/output.csv' # hardcoded

options = PipelineOptions(
        project='woven-name-434311-i8',
        region='us-central1',
        temp_location='gs://gcp35batch/temp_folder',
        stage_location='gs://gcp35batch/stage_folder',
        runner='DataflowRunner',
        job_name='example-dataflow-job',
        num_workers=2,  # Minimum number of workers
        max_num_workers=3,  # Maximum number of workers
        worker_machine_type='n1-standard-1',  # Use n1-standard-1 machine type
        worker_disk_type='pd-ssd',
        worker_disk_size_gb=100,  # Worker disk size
        # machine_type='n1-standard-1',  # Ensure the main machine type is also n1-standard-1

    ) 

def uppercase(element):
     # print(type(element)) # it is to identify the type of the object passed to the udf
     # print(element.split()) # if you apply the split() function on a string object - it will split the stirng into different itesms 
     # and then it will convert them into a list of elements by using space a delimeter 
     row = element.split()
     emptylist = []
     
     for col in range(len(row)-1):
         if col == 1:
              emptylist.append(row[col][:len(row[col])-1].upper()) 
         else:
              emptylist.append(row[col][:len(row[col])-1])
     emptylist.append(row[len(row)-1])
     output = ",".join(emptylist)
     return output
              
          

with beam.Pipeline(options=options) as pipeline:
     pcollection = pipeline | 'Input Pcollection' >> beam.io.ReadFromText(gcs_inputpath, skip_header_lines=1) 
     transformation1 = pcollection | 'Make Name columns vlaues to be uppercased' >> beam.Map(uppercase) 
     output = transformation1 | 'Storing to GCS' >> beam.io.WriteToText(gcs_outputpath)
     
     
L11: Argument Passing:
-------------------------
(class) PipelineOptions
This class and subclasses are used as containers for command line options.

These classes are wrappers over the standard argparse Python module (see https://docs.python.org/3/library/argparse.html). To define one option or a group of options, create a subclass from PipelineOptions.

Example Usage:

  class XyzOptions(PipelineOptions):

    @classmethod
    def _add_argparse_args(cls, parser):
      parser.add_argument('--abc', default='start')
      parser.add_argument('--xyz', default='end')
      
The arguments for the add_argument() method are exactly the ones described in the argparse public documentation.

Pipeline objects require an options object during initialization. This is obtained simply by initializing an options class as defined above.


Real Usage:

  class CustomOptions(PipelineOptions):

    @classmethod
    def _add_argparse_args(cls, parser):
      parser.add_argument('--input', default='gs://bucket_name/textfile.csv')
      parser.add_argument('--output', default='gs://bucket_name/outputtextfile.csv')
      
The arguments for the add_argument() method are exactly the ones described in the argparse public documentation.

Pipeline objects require an options object during initialization. This is obtained simply by initializing an options class as defined above.

# Simple UDF with hardcoded inputs:

# Task:: a + b = total

a = int(input('Eneter the first value: '))
b = int(input('Eneter the first value: '))

def addition(a,b):
    return a + b
    
result = addition(a, b)
print(result)


Working Code:
-------------
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions 

# Define custom pipeline options to accept input and output paths
class CustomOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_value_provider_argument('--input', type=str, help='Input file path')
        parser.add_value_provider_argument('--output', type=str, help='Output file path')

# Function to convert name columns to uppercase
def uppercase(element):
    row = element.split()
    emptylist = []
    
    for col in range(len(row)-1):
        if col == 1:
            emptylist.append(row[col][:len(row[col])-1].upper())
        else:
            emptylist.append(row[col][:len(row[col])-1])
    emptylist.append(row[len(row)-1])
    
    output = ",".join(emptylist)
    return output

# Main pipeline function
def run():
    # Create pipeline options
    options = PipelineOptions()
    custom_options = options.view_as(CustomOptions)
    
    # Ensure the job can be scaled with temp and stage locations
    pipeline_options = PipelineOptions(
        project='woven-name-434311-i8',
        region='us-central1',
        temp_location='gs://gcp35batch/temp_folder',
        stage_location='gs://gcp35batch/stage_folder',
        runner='DataflowRunner',
        job_name='example-dataflow-job2',
        num_workers=2,
        max_num_workers=3,
        worker_machine_type='n1-standard-1',
        worker_disk_type='pd-ssd',
        worker_disk_size_gb=100,
    )
    
    # Start the pipeline
    with beam.Pipeline(options=pipeline_options) as pipeline:
        # Read the input file from GCS
        pcollection = pipeline | 'Input Pcollection' >> beam.io.ReadFromText(custom_options.input, skip_header_lines=1)
        
        # Apply transformation to uppercase the name columns
        transformation1 = pcollection | 'Make Name columns values uppercased' >> beam.Map(uppercase)
        
        # Write the output to GCS
        transformation1 | 'Storing to GCS' >> beam.io.WriteToText(custom_options.output)

if __name__ == '__main__':
    run()


Dataflow job Submit Command:
-----------------------------


Shell Cript: linux machines, cloud shell

python basic_beam4.py \
    --runner=DataflowRunner \
    --project=woven-name-434311-i8 \
    --region=us-central1 \
    --temp_location=gs://gcp35batch/temp_folder \
    --stage_location=gs://gcp35batch/stage_folder \
    --input=gs://gcp35batch/texfile.csv \
    --output=gs://gcp35batch/output/output.csv

 

Windows Powershell

python basic_beam4.py 
    --runner=DataflowRunner 
    --project=woven-name-434311-i8 
    --region=us-central1 
    --temp_location=gs://gcp35batch/temp_folder 
    --stage_location=gs://gcp35batch/stage_folder 
    --input=gs://gcp35batch/texfile.csv 
    --output=gs://gcp35batch/output/output.csv

     
     
     
GCS and AWS - buckets...