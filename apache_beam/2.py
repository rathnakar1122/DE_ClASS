import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions, StandardOptions
from apache_beam.io import ReadFromText, WriteToBigQuery
import os
import csv
from io import StringIO

# Set environment variables
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/45375853/Documents/cs_data_plotform/service_account/dbsr-pdtest-dev-svc-account.json'
os.environ['http_proxy'] = "http://googleapis-dev.gcp.cloud.uk.hsbc:3128"
os.environ['https_proxy'] = "http://googleapis-dev.gcp.cloud.uk.hsbc:3128"

class TransformData(beam.DoFn):
    def process(self, element):
        # Create a CSV file reader
        reader = csv.DictReader(StringIO(element))
        # Extract data from CSV and yield as dictionary
        for row in reader:
            yield {
                'id': int(row['id']),
                'name': row['name'],
                'age': int(row['age'])
            }

def run(argv=None):
    pipeline_options = PipelineOptions(argv)
    pipeline_options.view_as(StandardOptions).runner = 'DataflowRunner'
    pipeline_options.view_as(StandardOptions).temp_location = 'gs://cs-df-events-poc/tmp/'
    pipeline_options.view_as(StandardOptions).staging_location = 'gs://cs-df-events-poc/staging/'
    pipeline_options.view_as(StandardOptions).project = 'your-project-id'  # Replace with your project ID
    pipeline_options.view_as(StandardOptions).region = 'europe-west2'

    p = beam.Pipeline(options=pipeline_options)  # Use `p` consistently

    # Read CSV from GCS
    lines = (
        p
        | "Read CSV File" >> ReadFromText("gs://cs-df-events-poc/site-map/site_sample.csv")
    )

    # Transform the data
    transformed = (
        lines 
        | 'Transform Data' >> beam.ParDo(TransformData())        
    )

    # Write data to BigQuery
    transformed | 'Write to BigQuery' >> WriteToBigQuery(
        table='your-project-id:your_dataset_name.your_table_name',  # Replace with your dataset and table name
        schema='id:INTEGER, name:STRING, age:INTEGER',
        write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE
    )

    result = p.run()
    result.wait_until_finish()

if __name__ == '__main__':
    run()
