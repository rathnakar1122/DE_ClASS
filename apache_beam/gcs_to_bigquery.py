from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.gcp.bigquery import WriteToBigQuery, BigQueryDisposition
import apache_beam as beam
import os
import logging 
logging.getLogger().setLevel(logging.INFO)

# Set the path to your GCP credentials JSON file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\ENV\rathnakar-18m85a0320-hiscox-0d1ad7b79faf.json"
# Define pipeline options
options = PipelineOptions(
    runner='DataflowRunner',  # Use 'DataflowRunner' when deploying to GCP
    project='rathnakar-18m85a0320-hiscox',  # Replace with your GCP project ID
    temp_location='gs://fusion-data-1st/temp/',  # GCS bucket for temp files
    region='us-central1',  # Specify the region
    job_name='etl-1',  # Specify the Dataflow job name
    max_num_workers=5,  # Maximum number of workers for the Dataflow job
    subnet='regons/europe-west2/subnets/dataflow-europe-west',  # Specify the subnet if required
    no_public_ips=True,  # Disable public IPs for workers
    #dataflow_kms_key='your-kms-key',  # Specify the KMS key if needed
    process_date='2025-01-16',  # Process date, can be dynamic as required
    process_name='assets'  # Name of the process for tracking
)


class MyPipelineOptions(PipelineOptions):
    @classmethod
    def _add_argparse_args(cls, parser):
        parser.add_argument('--logging_mode',default='INFO')
        parser.add_argument('--process_name',help=' assets')

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    my_pipeline_options = PipelineOptions().view_as(MyPipelineOptions)
# Define the BigQuery schema
schema = {
    "fields": [
        {"name": "Year", "type": "INTEGER", "mode": "NULLABLE"},
        {"name": "Month", "type": "INTEGER", "mode": "NULLABLE"},
        {"name": "LossYear", "type": "INTEGER", "mode": "NULLABLE"},
        {"name": "PolicyYear", "type": "INTEGER", "mode": "NULLABLE"},
        {"name": "StateNum", "type": "INTEGER", "mode": "NULLABLE"},
        {"name": "CompanyNum", "type": "INTEGER", "mode": "NULLABLE"},
        {"name": "ProductCode", "type": "STRING", "mode": "NULLABLE"},
        {"name": "LineCode", "type": "STRING", "mode": "NULLABLE"},
        {"name": "KindCode", "type": "STRING", "mode": "NULLABLE"},
        {"name": "TransactionCode", "type": "STRING", "mode": "NULLABLE"},
        {"name": "Type", "type": "STRING", "mode": "NULLABLE"},
        {"name": "Count", "type": "INTEGER", "mode": "NULLABLE"},
        {"name": "Amount", "type": "FLOAT", "mode": "NULLABLE"},
        {"name": "AfterClosureCode", "type": "STRING", "mode": "NULLABLE"},
        {"name": "AfterClosureTransactions", "type": "STRING", "mode": "NULLABLE"}
    ]
}

# Define the CSV parsing function
def parse_csv(line):
    import csv
    from io import StringIO

    # Parse the CSV line
    fields = list(csv.reader([line]))[0]
    
    # Map the fields to a dictionary based on schema
    return {
        'Year': int(fields[0]) if fields[0].isdigit() else None,
        'Month': int(fields[1]) if fields[1].isdigit() else None,
        'LossYear': int(fields[2]) if fields[2].isdigit() else None,
        'PolicyYear': int(fields[3]) if fields[3].isdigit() else None,
        'StateNum': int(fields[4]) if fields[4].isdigit() else None,
        'CompanyNum': int(fields[5]) if fields[5].isdigit() else None,
        'ProductCode': fields[6],
        'LineCode': fields[7],
        'KindCode': fields[8],
        'TransactionCode': fields[9],
        'Type': fields[10],
        'Count': int(fields[11]) if fields[11].isdigit() else None,
        'Amount': float(fields[12]) if fields[12] else None,
        'AfterClosureCode': fields[13],
        'AfterClosureTransactions': fields[14]
    }

# Build the pipeline
with beam.Pipeline(options=options) as p:
    (
        p
        | "Read from GCS" >> beam.io.ReadFromText('gs://crf-event/runder_dataflow.csv', skip_header_lines=1)
        | "Parse CSV" >> beam.Map(parse_csv)
        | "Write to BigQuery" >> WriteToBigQuery(
            table='rathnakar-18m85a0320-hiscox.MAIN.docx',
            schema=schema,
            write_disposition=BigQueryDisposition.WRITE_APPEND,
            create_disposition=BigQueryDisposition.CREATE_IF_NEEDED
        )
    )

