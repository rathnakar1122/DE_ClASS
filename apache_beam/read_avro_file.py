import apache_beam as beam
from apache_beam.io import avroio
from apache_beam.io.gcp.bigquery import WriteToBigQuery
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.options.pipeline_options import StandardOptions
from apache_beam.io.gcp.bigquery import BigQueryDisposition
import argparse

class AvroToBigQueryPipeline:
    def __init__(self, bucket_name, avro_path, bq_table):
        self.bucket_name = bucket_name
        self.avro_path = avro_path
        self.bq_table = bq_table

    def run(self):
        # Define the pipeline options
        options = PipelineOptions()
        options.view_as(StandardOptions).runner = 'DirectRunner'  # Use DirectRunner for local execution

        # Define the pipeline
        with beam.Pipeline(options=options) as p:
            (
                p
                # Step 1: Read Avro data from GCS
                | 'ReadAvro' >> avroio.ReadFromAvro(f'gs://{self.bucket_name}/{self.avro_path}')
                
                # Step 2: (Optional) Perform any data transformations if necessary
                | 'ProcessData' >> beam.Map(lambda record: record)  # Customize if needed
                
                # Step 3: Write to BigQuery
                | 'WriteToBigQuery' >> WriteToBigQuery(
                    self.bq_table,
                    schema='SCHEMA_AUTODETECT',  # You can specify the schema here or use auto-detect
                    write_disposition=BigQueryDisposition.WRITE_TRUNCATE,  # Overwrite existing data
                    create_disposition=BigQueryDisposition.CREATE_IF_NEEDED  # Create table if doesn't exist
                )
            )

if __name__ == '__main__':
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Avro to BigQuery Pipeline")
    
    parser.add_argument('--bucket_name', required=True, help='GCS bucket name where the Avro files are stored')
    parser.add_argument('--avro_path', required=True, help='Path within the bucket to the Avro files')
    parser.add_argument('--bq_table', required=True, help='BigQuery table to write data (format: project:dataset.table)')

    args = parser.parse_args()

    # Run the pipeline
    avro_to_bq = AvroToBigQueryPipeline(args.bucket_name, args.avro_path, args.bq_table)
    avro_to_bq.run()
