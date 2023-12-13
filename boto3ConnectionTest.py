import boto3
from botocore.exceptions import NoCredentialsError

def connect_to_s3(bucket_name, aws_access_key_id, aws_secret_access_key, aws_session_token=None, region_name='us-east-1'):
    """
    Connect to an S3 bucket using the provided credentials.

    Parameters:
    - bucket_name: The name of the S3 bucket.
    - aws_access_key_id: The AWS access key ID.
    - aws_secret_access_key: The AWS secret access key.
    - aws_session_token: The AWS session token (optional for temporary credentials).
    - region_name: The AWS region (default is 'us-east-1').

    Returns:
    - A boto3 S3 client.
    """
    try:
        # Create an S3 client
        s3 = boto3.client('s3', region_name=region_name,
                          aws_access_key_id=aws_access_key_id,
                          aws_secret_access_key=aws_secret_access_key,
                          aws_session_token=aws_session_token)

        # Test the connection by listing buckets
        response = s3.list_buckets()

        print("Connected to S3 successfully. Buckets:")
        for bucket in response['Buckets']:
            print(f"- {bucket['Name']}")

        return s3

    except NoCredentialsError:
        print("Credentials not available.")
        return None

# Example Usage:
# Replace 'your_bucket_name', 'your_access_key', and 'your_secret_key' with your actual values.
s3_client = connect_to_s3('clientemailsbucket', 'xxxxxxxxxxxxxxxxxxxx', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

if s3_client:
    # Now you can perform S3 operations using the 's3_client' object.
    # Example: List objects in a bucket
    bucket_name = 'clientemailsbucket'
    objects = s3_client.list_objects(Bucket=bucket_name)

    print(f"Objects in '{bucket_name}':")
    for obj in objects.get('Contents', []):
        print(f"- {obj['Key']}")
