# import logging
# import requests
# import azure.functions as func
# from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
# import base64
# import uuid
# import os

# app = func.FunctionApp()

# # Hello changement 

# IA_SERVICE_URL = os.environ.get("IA_SERVICE_URL")
# # Configuration du client Azure Blob Storage
# CONNECTION_STRING = os.environ.get("CONNECTION_STRING")
# CONTAINER_NAME = os.environ.get("CONTAINER_NAME")
# blob_name = ""+str(uuid.uuid4())+".jpg"

# print(blob_name,CONNECTION_STRING,CONTAINER_NAME)

# # Créer un client de service blob
# blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)
# blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=blob_name)



# @app.route(route="blob_push", auth_level=func.AuthLevel.FUNCTION)
# def blob_push(req: func.HttpRequest) -> func.HttpResponse:
#     logging.info('Python HTTP trigger function for push blob processed a request.')

#     img = req.params.get('img')
#     if not img:
#         try:
#             req_body = req.get_json()
#         except ValueError:
#             pass
#         else:
#             img = req_body.get('img')

#     if img:
#         base64_string = img
#         image_data = base64.b64decode(base64_string)
#         blob_client.upload_blob(image_data)
#         return func.HttpResponse(f"Hello, {blob_name} are upload on blob storage from {base64_string}")
#     else:
#         return func.HttpResponse(
#              "This HTTP triggered function executed successfully. But image are not received",
#              status_code=200
#         )


import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="testtrigger", auth_level=func.AuthLevel.FUNCTION)
def testtrigger(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )