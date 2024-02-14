import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()


@app.blob_trigger(arg_name="myblob", path="blob-container/{name}.png",
                               connection="DefaultEndpointsProtocol=https;AccountName=myresourcesgroupb3b7;AccountKey=LLb3BeU4v/CHedCO3QS3SglPMYygk5dnefSZJXrHqBm1JD30aFIUPG29ooAiQMZMOziP07H8m8KY+ASt/IWk0Q==;EndpointSuffix=core.windows.ne") 
def BlobTrigger(myblob: func.InputStream):
    logging.info(f"Python blob trigger function processed blob"
                f"Name: {myblob.name}"
                f"Blob Size: {myblob.length} bytes"
                f"Blob : {myblob}")
    