# AWS Docs
- See [pricing](https://aws.amazon.com/bedrock/pricing/)
- [Agents for Bedrock](https://aws.amazon.com/bedrock/agents/)

# AWS Commands

Getting the models in your region
```
aws bedrock list-foundation-models | jq '.modelSummaries.[].modelId'
```

# Blogs
- [Generative AI: Amazon Bedrock using the CLI](https://sbstjn.com/blog/ai-generative-ai-aws-bedrock-cli-text-generation/) - Oct 2023
- [Basic Information about Amazon Bedrock with API Examples - Model Features, Pricing, How to Use, Explanation of Tokens and Inference Parameters](https://hidekazu-konishi.com/entry/amazon_bedrock_basic_info_and_api_examples.html) - Mar 2024

# Boto
- [Bedrock Client](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock.html) and [BedRock Runtime](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/bedrock-runtime.html) which is what you should be using to interact with the APIs
- https://docs.aws.amazon.com/code-library/latest/ug/python_3_bedrock_code_examples.html

# Infrastructure 
## CloudFormation
- [enable-bedrock-logging-using-cloudformation](https://github.com/aws-samples/enable-bedrock-logging-using-cloudformation) and [blog](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/configure-bedrock-invocation-logging-cloudformation.html)

## CDK 
- https://github.com/awslabs/generative-ai-cdk-constructs/
- [aws_cdk.aws_bedrock](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_bedrock.html)

## Terraform
- [Data Source: aws_bedrock_foundation_model](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/bedrock_foundation_model)


# Example Solutions
- https://github.com/aws-samples/aws-bedrock-langchain-python-cdk
- https://aws.amazon.com/blogs/mobile/create-a-fullstack-sample-web-app-powered-by-amazon-bedrock/
- [Build a Serverless GenAI image creator - Amazon Bedrock model deployed with AWS CDK](https://community.aws/content/2b6vVO87SMvy1cY70GeinjH5ZX3/multimodal?lang=en) - Jan 2024
- https://github.com/aws-samples/amazon-bedrock-workshop
- https://github.com/aws-samples/bedrock-serverless-workshop/
