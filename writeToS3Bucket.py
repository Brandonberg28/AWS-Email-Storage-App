import json

#create and specific bucket name variable
bucketName = "bucket name"

def writeToS3Bucket(s3client, emailsDictionary):

    #convert dictionary to JSON format for data transfer
    emailsJSON =  json.dumps(emailsDictionary)

    #create object key 
    objectKey = "your_object_key.json"

    #upload the data to S3 bucket
    s3client.put_object(Body=emailsJSON, Bucket=bucketName, Key=objectKey)

    #Debugging purposes
    print(f"Data sent to S3 Bucket: {bucketName} - {objectKey}")