"""
* File: readInEmails.py
* Author: Brandon Bergado 
* Date created: 11/30/2023

* This script that reads in a .csv file containing the emails of clients, and stores them in a dictionary
"""

import csv

def read_emails(filePath):
    emailsDictionary = {}  #create the dictionary to store data

    try:
        with open(filePath, 'r') as file:
            fileReader = csv.reader(file)

            headers = next(fileReader) #Read in header row and then move on to data

            for row in fileReader:  #iterates through each row in .csv file
                try: 
                    email, firstName, lastName = row  #Tuple Unpacking: assumes row column order is [email, firstName, lastName]
                    
                    if email not in emailsDictionary: #bounds check for email duplicates 
                        emailsDictionary[email] = {'FirstName': firstName, 'LastName': lastName}  #loads dictionary with data
                    else:
                        print(f"{email} is a duplicate. Not adding to dictionary.")
                except ValueError as e:
                    print(f"ERROR: {e} was unable to be processed due to data format")
    except FileNotFoundError:
        print(f"ERROR: the file was not found with file path {filePath}")
    except Exception as e:
        print(f"ERROR: {e} error occured")

    
    return emailsDictionary #return the dictionary of emails 