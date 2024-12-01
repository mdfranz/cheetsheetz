# Using AWS Credentials

Use the (aws integration)[https://www.windmill.dev/docs/integrations/aws]

```
import os
import wmill
import boto3

# see https://windmill.dev

def main():  # Specify the parameter type as a dictionary
    aws_accounts = []
    aws_accounts.append(wmill.get_resource("u/mdfranz/aws_9431"))
    aws_accounts.append(wmill.get_resource("u/mdfranz/aws_6473"))
    responses = []

    for aws in aws_accounts:
        session = boto3.Session(
            aws_access_key_id=aws['awsAccessKeyId'],
            aws_secret_access_key=aws['awsSecretAccessKey'],
            region_name="us-east-1"
        )

        sts_client = session.client('sts')
        response = sts_client.get_caller_identity()

        print(response)
        responses.append(response)

    return responses
```
