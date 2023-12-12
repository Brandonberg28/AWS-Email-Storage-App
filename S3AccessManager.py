#Brandon Bergado 12/08/2023

#This script creates the AWS S3 Access Manager

import boto3
import json

# create and set up AWS credentials variables
aws_access_key_id = "AKIAZNOC3QSSK6VV7R4J"
aws_secret_access_key = "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"

def createClient():
    # create the S3 client
    s3client = boto3.client('s3',
                            aws_access_key_id=aws_access_key_id,
                            aws_secret_access_key=aws_secret_access_key
                            )

    return s3client
