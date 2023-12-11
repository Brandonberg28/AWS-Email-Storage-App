#Brandon Bergado 12/08/2023

#This script creates the AWS S3 Access Manager


import boto3
import json

#create and set up AWS credentials variables
awsAccessKeyId = "xxxxxxxxxxxxxxxxxxxx"
awsSecretAccessKey = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

def createS3client():
    #create the S3 client
    s3client = boto3.client('s3client',
                                awsAccessKeyId =  awsAccessKeyId,
                                awsSecretAccessKey = awsSecretAccessKey
                                )

    return s3client