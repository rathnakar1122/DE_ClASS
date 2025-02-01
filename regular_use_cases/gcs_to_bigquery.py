import os
import re
import uuid
import logging
import pandas as pd
from datetime import datetime
from google.cloud import storage, bigquery
from modules import read_config_yaml as config

# Define configuration
CONFIG = {
    "EXEC_DATETIME": datetime.now(),
    "LOG_FORMAT": "%(asctime)s - %(levelname)s - %(message)s",
    "LOG_LEVEL": logging.INFO,
}

# Set up logging
logging.basicConfig(level=CONFIG["LOG_LEVEL"], format=CONFIG["LOG_FORMAT"])
logger = logging.getLogger(__name__)

def file_process(file_content, schema=None, skiprows=None, separator=","):
    """
    Process the file content and return a Pandas DataFrame after applying schema validations.
    
    :param file_content: File content as a string.
    :param schema: A dictionary containing column names and their data types.
    :param skiprows: Number of rows to skip at the start of the file.
    :param separator: Column separator in the file (default is ',').
    :return: A Pandas DataFrame.
    """
    try:
        content_lines = file_content.splitlines()
        cols = list(schema.keys()) if schema else None

        logger.info(f"Separator is: {separator}")
        logger.info(f"Skip rows is: {skiprows}")

        df = pd.read_csv(
            pd.compat.StringIO('\n'.join(content_lines)),
            names=cols,
            sep=separator,
            on_bad_lines="warn",
            low_memory=False,
            header=None,
            skiprows=skiprows,
        )

        for col_name, d_type in schema.items():
            if d_type == "date":
                df[col_name] = pd.to_datetime(df[col_name], errors='coerce')
            elif d_type == "numeric":
                df[col_name] = pd.to_numeric(df[col_name], errors='coerce')
            else:
                df[col_name] = df[col_name].astype(d_type)

        df["FILE_BATCH_ID"] = str(uuid.uuid1())
        df["INSERTED_TS"] = pd.to_datetime(datetime.now())

        logger.info("Schema after typecasting:")
        df.info(verbose=True)

        return df

    except Exception as e:
        logger.error(f"Error processing file: {str(e)}")
        raise RuntimeError(str(e))

def load_file_to_bq(df, dest_dataset_id, dest_table_id, disposition):
    """
    Load a Pandas DataFrame into a BigQuery table.

    :param df: Pandas DataFrame to load.
    :param dest_dataset_id: Destination BigQuery dataset ID.
    :param dest_table_id: Destination BigQuery table ID.
    :param disposition: Write disposition (e.g., WRITE_APPEND, WRITE_TRUNCATE).
    """
    try:
        bigquery_client = bigquery.Client()
        table = bigquery_client.dataset(dest_dataset_id).table(dest_table_id)
        job_config = bigquery.LoadJobConfig(write_disposition=disposition)

        job = bigquery_client.load_table_from_dataframe(df, table, job_config=job_config)
        job.result()

        logger.info(f"Data successfully loaded into table: {table}")
    except Exception as e:
        logger.error(f"Error loading data into BigQuery: {str(e)}")
        raise RuntimeError(str(e))

def archive_data_file(filename, gcs_bucket, gcs_archive_folder):
    """
    Archive a file in Google Cloud Storage (GCS).

    :param filename: Name of the file to archive.
    :param gcs_bucket: Name of the GCS bucket.
    :param gcs_archive_folder: Name of the folder in GCS where the file will be archived.
    """
    try:
        gcs_client = storage.Client()
        source_bucket = gcs_client.bucket(gcs_bucket)
        source_blob = source_bucket.blob(filename)
        destination_blob_name = f"{gcs_archive_folder}/{filename}_{CONFIG['EXEC_DATETIME'].strftime('%Y%m%d%H%M%S')}"

        source_bucket.copy_blob(source_blob, source_bucket, destination_blob_name)
        source_blob.delete()

        logger.info(f"File '{filename}' archived to '{destination_blob_name}' in bucket '{gcs_bucket}'")
    except Exception as e:
        logger.error(f"Error archiving file: {str(e)}")
        raise RuntimeError(str(e))

def process_files_from_gcs(gcs_client, gcs_read_bucket, gcs_read_bucket_path, schema, separator, skipheaderrows, bq_dataset_name, bq_table_name, load_disposition, gcs_archive_bucket, gcs_archive_folder):
    """
    Process files from GCS bucket, filter qualified files, and perform ETL operations.

    :param gcs_client: Google Cloud Storage client.
    :param gcs_read_bucket: Name of the GCS bucket.
    :param gcs_read_bucket_path: Path inside the GCS bucket to read files from.
    :param schema: Table schema for processing.
    :param separator: Separator for file parsing.
    :param skipheaderrows: Number of rows to skip in files.
    :param bq_dataset_name: BigQuery dataset name.
    :param bq_table_name: BigQuery table name.
    :param load_disposition: BigQuery load disposition.
    :param gcs_archive_bucket: Name of the archive bucket.
    :param gcs_archive_folder: Path for archiving files in GCS.
    """
    try:
        folder_path = f"{gcs_read_bucket_path}/"
        logger.info(f"Folder path is: {folder_path}")

        files = gcs_client.list_blobs(gcs_read_bucket, prefix=folder_path)
        qualified_files = []

        for file_obj in files:
            file_name = file_obj.name.split('/')[-1]
            logger.info(f"Processing file: {file_name}")
            qualified_files.append(file_obj)

        if qualified_files:
            for file_obj in qualified_files:
                file_content = file_obj.download_as_text()
                df = file_process(file_content, schema=schema, skiprows=skipheaderrows, separator=separator)
                load_file_to_bq(df, bq_dataset_name, bq_table_name, load_disposition)
                archive_data_file(file_obj.name, gcs_archive_bucket, gcs_archive_folder)

        logger.info("All files processed successfully.")
    except Exception as e:
        logger.error(f"Error processing files from GCS: {str(e)}")
        raise RuntimeError(str(e))

def main(args):
    """
    Main function to execute the ETL process.

    :param args: Parsed arguments containing configuration details.
    """
    try:
        logger.info("Main execution begins.")
        environment = args.Environment
        config_file_name = args.cf
        schema_file_name = args.tf

        config_data = config.read_configuration(environment, config_file_name)
        schema = config.read_table_definition(schema_file_name)

        gcs_client = storage.Client()

        process_files_from_gcs(
            gcs_client=gcs_client,
            gcs_read_bucket=config_data['gcs_config']['gcs_read_bucket'],
            gcs_read_bucket_path=config_data['gcs_config']['gcs_read_bucket_path'],
            schema=schema['table_schema'],
            separator=config_data['gcs_config'].get('separator', ','),
            skipheaderrows=int(config_data['gcs_config'].get('skipheaderrows', 0)),
            bq_dataset_name=config_data['datasets']['discovery'],
            bq_table_name=schema['table_name'],
            load_disposition="WRITE_APPEND",
            gcs_archive_bucket=config_data['gcs_config']['gcs_archive_bucket'],
            gcs_archive_folder=config_data['gcs_config']['gcs_archive_bucket_path'],
        )

        logger.info("Main execution completed successfully.")
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")
        raise RuntimeError(str(e))

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="ETL Process")
    parser.add_argument("--Environment", required=True, help="Environment name (e.g., dev, prod)")
    parser.add_argument("--cf", required=True, help="Configuration file path")
    parser.add_argument("--tf", required=True, help="Schema file path")

    args = parser.parse_args()
    main(args)