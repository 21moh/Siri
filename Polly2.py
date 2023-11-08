import boto3
from botocore.credentials import AssumeRoleCredentials
from os import environ

# Get the access keys from environment variables
aws_access_key_id = environ["AWS_ACCESS_KEY_ID"]
aws_secret_access_key = environ["AWS_SECRET_ACCESS_KEY"]

# Create a session object that assumes the IAM role
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    assumed_role_arn="ARN:aws:iam::123456789012:role/my-role",
)

# Create a client object for the Amazon Polly service using the assumed role
polly_client = session.client('polly')

# Set the text to synthesize
text = "Hello, world!"

# Set the voice to use
voice_id = "Joanna"

# Synthesize the speech
response = polly_client.synthesize_speech(Text=text, VoiceId=voice_id)

# Save the synthesized speech to an audio file
with open("output.mp3", "wb") as output:
    output.write(response.AudioStream.read())