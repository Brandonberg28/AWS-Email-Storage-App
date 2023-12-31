"""
* File: main.py
* Author: Brandon Bergado 
* Date created: 11/30/2023

* Main script that:
* reads a .csv file into a dictionary, converts that into JSON data,
* creates an AWS S3 client, and then sends the data to an S3 bucket.
"""

from readInEmails import read_emails
from S3AccessManager import createClient
from writeToS3Bucket import writeToS3Bucket

def main():
    filePath = 'RechargeEmailList.csv'          #set file path 
    emailsDictionary = read_emails(filePath)    #call function to read in emails

    s3client = createClient()                 #create S3 client variable to connect to Bucket
    writeToS3Bucket(s3client, emailsDictionary) #write to S3 bucket with AWS S3 client

    #Print  dictionary for debugging purposes
    #for email, data in emailsDictionary.items():
    #    print(f"Email: {email}, FirstName: {data['FirstName']}, LastName: {data['LastName']}")

main()

