++++++++++++++++++
7:54 AM 10/21/2024
++++++++++++++++++

*******************
 GCP Data Engineer
*******************

____________
AGENDA-> GCS
------------

30 days - Python Programmes


1. Integers -- Any given integer should be reversed - using UDF. Please take the user input

# input # :: age = 23
# output # :: age = 32

2. What is UDF in Python?

1. Python Prigramme:
2. GCS(GCP) - S3(AWS)
3. Cloud Functions(GCP) - Lamda Functions(AWS) - Python
4. Cloud SQL 


10/21/2024:
------------

GCS - Google Cloud Storage:

Best - Learing While Doing

GCS - Bucket(Container)

What we can do with the GCS?

>> 1. Bucekt Creation
>> 2. Objects Uploading
>> 3. Objects Moving
>> 4. Objects Removing/Deleting
>> 5. Bucekt Deletion



@ While Creating a Bucket, What points/things to be considered?

Ans:
1. Naming to a Bucket:

Pick a globally unique, permanent name. 

Naming guidelines 

Ex. â€˜exampleâ€™, â€˜example_bucket-1â€™, or â€˜example.comâ€™
Tip: Donâ€™t include any sensitive information

Bucket_name : gcsbucketforbatch36

gs:// - 
s3:// -

2. Choose where to store your data
	Location: us (multiple regions in United States)
	Location type: Multi-region
	[there are 3 types of location: MR, DR, SR]

3. Choose a storage class for your data
	Default storage class: Standard
	[There are 4 types of classes :[Standard, Nearline, ColdLine, Archival]
	
4. Choose how to control access to objects
	Public access prevention: On
	Access control: Uniform/Finegrained

5. Choose how to protect object data
	Soft delete policy: Default
	Object versioning: Disabled
	Bucket retention policy: Disabled
	Object retention: Disabled
	Encryption type: Google-managed



Mandotory Task1:
----------------
Running Apache_beam Script for DataflowRunner:
Job: GCS to GCS Movement 

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


https://storage.googleapis.com/gcp35batch/trendcart-images/laptop.jpg

gs://gcp35batch/trendcart-images/laptop.jpg

https://storage.cloud.google.com/gcp35batch/trendcart-images/laptop.jpg
















