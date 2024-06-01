# Installation 
- https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html 
- https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-completion.html 

## SSH Session Manager Plugin

See https://docs.aws.amazon.com/systems-manager/latest/userguide/install-plugin-debian-and-ubuntu.html

# JQ Examples 

## IAM

*Determine current account*

```
aws sts get-caller-identity
```

## CloudFormation
```
aws --region us-east-2 cloudformation list-stacks | jq -r '.StackSummaries[] | [ .StackId, .StackStatus ] | @csv'
```

## IAM
```
aws iam list-roles | jq -r '.Roles[] | [ .Arn, .CreateDate ] | @csv'
```

##  S3
```
aws s3api list-buckets | jq -r '.Buckets[] | [ .Name, .CreationDate ] | @csv'
```
