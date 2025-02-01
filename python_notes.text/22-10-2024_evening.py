# Different Ways of Bucekt Creation:

# 1. Console:
# 2. Command Line:
# 	--> Cloud Shell
# 		<> gsutil ls or gcloud storage ls(Wider Scope)
# 		<> gcloud storage buckets create gs://batch37gcp --location=us
# 	--> Local Shell
# 		<> gcloud storage buckets create gs://batch37gcp --location=us
# 3. Terraform:

# terraform {
#   required_providers {
#     google = {
#       source  = "hashicorp/google"
#       version = "4.51.0"
#     }
#   }
# }

# provider "google" {
#   project = "woven-name-434311-i8"
# }

# # Create new storage bucket in the US multi-region
# # with coldline storage 

# resource "google_storage_bucket" "static" {
#   name          = "gcstocloudsqldemo-new-bucket"
#   location      = "US"
#   storage_class = "COLDLINE"

#   uniform_bucket_level_access = true
# }
	
	
# Terraform installation:
# -----------------------
# # terraform download for windows - search it in google
# # https://developer.hashicorp.com/terraform/install#windows(amd64)
# # Extract All: C:\terraform
# # system environemnt variable - C:\terraform\
# Check:
# cmd:
# C:\Users\hanvi>terraform --version
# Terraform v1.9.8
# on windows_amd64 

# PS:
# PS C:\GCP-DE> terraform --version
# Terraform v1.9.8
# on windows_amd64
# PS C:\GCP-DE> 

# # Terraform Link:
# https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/google-cloud-platform-build#set-up-gcp

# mkdir learn-terraform-gcp

# cd learn-terraform-gcp

# mkdir gcp_gcs_service
# mkdir gcp_bigquery_service


# terraform {
#   required_providers {
#     google = {
#       source = "hashicorp/google"
#       version = "4.51.0"
#     }
#   }
# }

# provider "google" {
#   project = "woven-name-434311-i8"
# }

# # Create new storage bucket in the US multi-region
# # with coldline storage
# resource "random_id" "bucket_prefix" {
#   byte_length = 8
# }

# resource "google_storage_bucket" "static" {
#   name          = "${random_id.bucket_prefix.hex}-new-bucket"
#   location      = "US"
#   storage_class = "COLDLINE"

#   uniform_bucket_level_access = true
# }


# terraform init

# terraform validate

# terraform apply

# yes - yes