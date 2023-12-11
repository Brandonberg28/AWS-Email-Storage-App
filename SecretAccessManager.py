#Brandon Bergado 12/08/2023

#This script is the Secret Access Manager


#import the required dependencies from AWS

def SecretAccessManager():
    secretName = "name of secret or access key"
    region = "us-east-1"
    secret = ""

    #create a Secrets Manager Client (JAVA CODE FOR EXAMPLE)
    client = AWSSecretsManagerClientBuilder.standard().withRegion(region).build()
    getSecretValueRequest = GetSecretValueRequest().withSecretId(secretName);
    getSecretValueResult = null

    try:
        getSecretValueResult = client.getSecretValue(getSecretValueRequest)
    except DecryptionFailureException as e:
        print(f"{e} could not decript result")


    #decrypt secret using the associated key
    if getSecretValueResult.getSecretString() != null:
        secret = getSecretValueResult.getSecretString()
    else:
        decodedBinarySecret = new String(Base64.getDecoder().decode(getSecretValueResult.getSecretBinary()).array());
        secret = "it is not working";

    return secret

