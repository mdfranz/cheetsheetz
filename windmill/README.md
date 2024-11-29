# Articles
- [Long-running tasks done easy](https://invak.id/long-running-tasks)

# Important Features & Concepts
- [Caching](https://www.windmill.dev/docs/core_concepts/caching)
- [States](https://www.windmill.dev/docs/core_concepts/resources_and_types#states) - 
- [Webhooks](https://www.windmill.dev/docs/core_concepts/webhooks)
- [Preprocessors](https://www.windmill.dev/docs/core_concepts/preprocessors)
- [Data Pipelines](https://www.windmill.dev/docs/core_concepts/data_pipelines)
- [Workflows as Code](https://www.windmill.dev/docs/core_concepts/workflows_as_code)

# CLI

You need Nodejs installed (deno is gone) via 

```
npm install -g windmill-cli
```

## Add Instance

```
mfranz@cros-acer516ge:~/windmill/rog$ wmill workspace add rog rog http://100.83.76.59:8000/
? How do you want to login › Browser
Login by going to http://100.83.76.59:8000/user/cli?port=25843
Opened browser for you
```

## Local Development Tips

See (recommended setup)[https://www.windmill.dev/docs/advanced/local_development#local-development-recommended-setup] which suggests using the following when using within CI/CD

```
wmill sync pull --skip-variables --skip-secrets --skip-resources
```

# Using AWS

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
