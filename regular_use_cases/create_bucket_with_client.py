# from google.cloud import storage
# def create_bucket_class_location(bucket_name):
#     """Create a new bucket in the US region with the Coldline storage class."""    
#     # Initialize the Cloud Storage client
#     storage_client = storage.Client()
#     # Create a new bucket object
#     bucket = storage_client.bucket(bucket_name)
#     # Set the storage class to Coldline
#     bucket.storage_class = "COLDLINE"
#     # Create the bucket in the US region
#     new_bucket = storage_client.create_bucket(bucket, location="US")
#     # Corrected the print statement to display all the values
#     print(
#         "Created bucket {} in {} with storage class {}".format(
#             new_bucket.name, new_bucket.location, new_bucket.storage_class
#         ))
#     return new_bucket

from google.cloud import storage

def create_bucket_class_location(bucket_name):
    storage_Client = storage.Client()
    bucket=storage_client.bucket(bucket_name)
    bucket.storage_class="coldLine"
    new_bucket =storage_client.create_bucket(bucket, location="us")
    print(f(new_bucket.name, new_bucket.location,new_bucket.storage_class))