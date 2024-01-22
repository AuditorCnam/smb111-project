import logging
import requests
import azure.functions as func
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import base64
import uuid
import os

IA_SERVICE_URL = os.environ.get("IA_SERVICE_URL")
# Configuration du client Azure Blob Storage
CONNECTION_STRING = os.environ.get("CONNECTION_STRING")
CONTAINER_NAME = os.environ.get("CONTAINER_NAME")
blob_name = ""+str(uuid.uuid4())+".jpg"

print(blob_name,CONNECTION_STRING,CONTAINER_NAME)

# Créer un client de service blob
blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob_name)



def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    img = req.params.get('img')
    if not img:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            img = req_body.get('img')

    if img:
        base64_string = img
        image_data = base64.b64decode(base64_string)
        blob_client.upload_blob(image_data)
        return func.HttpResponse(f"Hello, {blob_name} are upload on blob storage from {base64_string}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. But image are not received",
             status_code=200
        )