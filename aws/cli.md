
# JQ Examples 

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
