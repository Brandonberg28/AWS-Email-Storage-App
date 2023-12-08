#Brandon Bergado 11/30/2023

#Main program that calls function to read in client emails from .csv file


from readInEmails import read_emails

def main():
    filePath = 'RechargeEmailList.csv'          #set file path 
    emailsDictionary = read_emails(filePath)    #call function to read in emails

    #Print  dictionary
    for email, data in emailsDictionary.items():
        print(f"Email: {email}, FirstName: {data['FirstName']}, LastName: {data['LastName']}")

main()

