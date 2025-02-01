

Share


You said:
 import apache_beam as beam 
from apache_beam.options.pipeline_options import PipelineOptions

gcs_inputpath = 'gs://gcp35batch/texfile.csv'
gcs_outputpath = 'gs://gcp35batch/output/output.csv'

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