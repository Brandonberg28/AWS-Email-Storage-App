#Brandon Bergado 11/30/2023

#Main program that calls function to read in client emails from .csv file


from readInEmails import read_emails
from S3AccessManager import createS3client
from writeToS3Bucket import writeToS3Bucket

def main():
    filePath = 'RechargeEmailList.csv'          #set file path 
    emailsDictionary = read_emails(filePath)    #call function to read in emails

    s3client = createS3client()                 #create S3 client variable to connect to Bucket
    writeToS3Bucket(s3client, emailsDictionary) #write to S3 bucket with AWS S3 client

    #Print  dictionary
    for email, data in emailsDictionary.items():
        print(f"Email: {email}, FirstName: {data['FirstName']}, LastName: {data['LastName']}")

main()

