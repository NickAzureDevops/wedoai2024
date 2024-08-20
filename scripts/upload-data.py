import os
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Azure Blob Storage configuration
connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container_name = 'build-data'
blob_name = 'build_data.csv'
local_file_path = 'build_data.csv'

# Ensure the connection string is set
if not connection_string:
    raise ValueError("Please set the AZURE_STORAGE_CONNECTION_STRING environment variable")

# Create the BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

def upload_to_blob():
    try:
        # Create a blob client
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
        
        # Upload the file
        with open(local_file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)
        print(f"File {local_file_path} uploaded to Azure Blob Storage as {blob_name} in container {container_name}.")
    except Exception as e:
        print(f"Error uploading file to Azure Blob Storage: {e}")

# Call the function to upload the file
upload_to_blob()