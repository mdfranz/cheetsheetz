# Use Cases 

See [Use Cases](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/IntroductionUseCases.html) such as
[Programmable CDN](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/IntroductionUseCases.html#IntroductionUseCasesProgrammableCDN)[Lambda@Edge]([https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html](Lambda@Edge) such as [Sample Function](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html)

# What is it?

## Distribution

Has xxx.cloudfront.net cdmain name

```aws cloudfront list-distributions```

List domain names &  ARN

```jq -r '.DistributionList.Items[] | [ .DomainName, .ARN ] |@csv '```

### Certificates

ACM Certs

### Logging

To S3 bucket 


# References

[Serverless Architecture Patterns in AWS](https://medium.com/@waswani/serverless-architecture-patterns-in-aws-edeab0e46a32) - Nov 2020
