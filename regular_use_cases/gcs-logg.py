from google.cloud import storage
import os
import logging  # This will now refer to the built-in logging module
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# Set the path to your service account key file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/ENV/rathnakar-18m85a0320-hiscox-0d1ad7b79faf.json"

def create_bucket_class_location(bucket_name):
    """
    Create a new bucket in the US region with the Coldline storage class.
    Args:
        bucket_name (str): The name of the bucket to be created.
    Returns:
        google.cloud.storage.bucket.Bucket: The created bucket object.
    """
    # Initialize the Google Cloud Storage client
    storage_client = storage.Client()

    # Create a new bucket object with the specified name
    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = "COLDLINE"  # Set the storage class to COLDLINE

    # Create the bucket in the specified location (US region)
    new_bucket = storage_client.create_bucket(bucket, location="US")

    # Print confirmation message
    print(
        f"Created bucket {new_bucket.name} in {new_bucket.location} with storage class {new_bucket.storage_class}"
    )
    return new_bucket

# Example usage
if __name__ == "__main__":
    bucket_name = "jll-input-file"  # Replace with your desired bucket name
    create_bucket_class_location(bucket_name)
