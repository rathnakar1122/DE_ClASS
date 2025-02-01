import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import datetime

# Function to add the process_date
def add_process_date(element):
    id, name, age = element.split(',')
    process_date = datetime.datetime.now().strftime('%Y-%m-%d')
    return f'{id},{name},{age},{process_date}'

# Define the pipeline options
pipeline_options = PipelineOptions(
    runner='DataflowRunner',  # Use 'DirectRunner' for local execution, 'DataflowRunner' for running on Dataflow
    project='your-gcp-project-id',  # Replace with your project ID
    temp_location='gs://your-temp-bucket/temp/',  # Replace with your temp GCS bucket
    region='your-gcp-region',  # Replace with your GCP region (e.g., us-central1)
    staging_location='gs://your-temp-bucket/staging/'  # Replace with your staging GCS bucket
)

# Input and output file paths
input_file = 'gs://your-bucket-name/test_table'  # Replace with your input file
output_file = 'gs://your-bucket-name/test2_table'  # Replace with your output file

# Create and run the pipeline
with beam.Pipeline(options=pipeline_options) as p:
    (
        p
        | 'Read CSV Data' >> beam.io.ReadFromText(input_file, skip_header_lines=1)
        | 'Add Process Date' >> beam.Map(add_process_date)
        | 'Write Transformed Data' >> beam.io.WriteToText(output_file, file_name_suffix='.csv', header='id,name,age,process_date')
    )
