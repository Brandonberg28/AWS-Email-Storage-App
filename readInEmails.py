#Brandon Bergado 11/30/2023

#Program that reads in a .csv file containing the emails of clients and stores them in a dictionary

import csv

def read_emails(filePath):
    emailsDictionary = {}  #create the dictionary to store data

    with open(filePath, 'r') as file:
        fileReader = csv.reader(file)

        #Read in header row and then move on to data
        headers = next(fileReader)

        for row in fileReader:  #iterates through each row in .csv file
            #This format works assuming columns are ordered: [Email, FirstName, LastName]
            email, firstName, lastName = row  #Tuple Unpacking: row [email, firstName, lastName] into corresponding variables
            
            if email not in emailsDictionary: #bounds check for email duplicates 
                emailsDictionary[email] = {'FirstName': firstName, 'LastName': lastName}  #loads dictionary with data
            else:
                print(f"{email} is a duplicate. Not adding to dictionary.")

    return emailsDictionary #return the dictionary of emails 