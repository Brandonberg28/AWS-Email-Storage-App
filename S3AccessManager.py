#Brandon Bergado 12/08/2023

#This script is the S3 Bucket Access Manager

#import the required dependencies from AWS

def writeToBucket(bucketName, keyName):
    #maybe need a file path variable?


    #JAVA CODE FOR EXAMPLE

    #client variable that connects to AWS, like an API messenger
    final AmazonS3 s3 = AmazonS3ClientBuilder.standard().withRegion("us-east-1").build();

    #trying to put the object in the bucket
    try {
        s3.putObject(bucket_name, key_name, new File(file_path));
    } 
    catch (AmazonServiceException e) {
        System.err.println(e.getErrorMessage());
        System.exit(1);
    }