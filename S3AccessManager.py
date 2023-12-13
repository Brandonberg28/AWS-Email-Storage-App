"""
* File: S3AccessManager.py
* Author: Brandon Bergado 
* Date created: 12/10/2023

* This script creates the client to connect to AWS
"""

import boto3
import json

# create and set up AWS credentials variables
aws_access_key_id = "xxxxxxxxxxxxxxxxxxxx"
aws_secret_access_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

def createClient():
    # create the S3 client
    s3client = boto3.client('s3',
                            aws_access_key_id=aws_access_key_id,
                            aws_secret_access_key=aws_secret_access_key
                            )

    return s3client
