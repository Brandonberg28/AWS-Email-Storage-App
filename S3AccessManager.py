#Brandon Bergado 12/08/2023

#This script creates the AWS S3 Access Manager


import boto3
import json

#create and set up AWS credentials variables
aws_access_key_id = "AKIAZNOC3QSSJQARFJFS"
aws_secret_access_key = "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"

def createS3client():
    #create the S3 client
    s3client = boto3.client('s3client',
                                aws_access_key_id =  aws_access_key_id,
                                aws_secret_access_key = aws_secret_access_key
                                )

    return s3client