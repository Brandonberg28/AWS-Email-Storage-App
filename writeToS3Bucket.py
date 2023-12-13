"""
* File: writeToS3Bucket.py
* Author: Brandon Bergado 
* Date created: 12/10/2023

* This script converts a dictionary into JSON data and pushes it up to an AWS S3 bucket.
"""

import json
import botocore.exceptions 

#create and specific bucket name variable
bucketName = "clientemailsbucket"

def writeToS3Bucket(s3client, emailsDictionary):

    try:
        #convert dictionary to JSON format for data transfer
        emailsJSON =  json.dumps(emailsDictionary)

        #create object key 
        objectKey = "your_object_key.json"

        #upload the data to S3 bucket
        s3client.put_object(Body=emailsJSON, Bucket=bucketName, Key=objectKey)

        #Debugging purposes
        print(f"Data sent to S3 Bucket: {bucketName} - {objectKey}")
    
    except json.JSONDecodeError as json_error:
        print(f"ERROR: {json_error} converting dictionary to JSON")
    except botocore.exceptions.ClientError as s3_error:
        error_code = s3_error.response['Error']['Code']
        if error_code == 'NoSuchBucket':
            print(f"ERROR: couldn't locate bucket {bucketName}")
        else:
            print(f"ERROR: upload error ({error_code}): {s3_error}")
    except Exception as e:
        print(f"ERROR: {e} error occured")