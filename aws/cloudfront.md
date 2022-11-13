
# Use Cases 
- [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/IntroductionUseCases.html](Use Cases)
- [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/IntroductionUseCases.html#IntroductionUseCasesProgrammableCDN](Programmable CDN) with [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html](Lambda@Edge) such as [https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-examples.html](sample function) 

# What is it
## Distribution

- Has xxx.cloudfront.net cdmain name

```aws cloudfront list-distributions```

List domain names &  ARN

```jq -r '.DistributionList.Items[] | [ .DomainName, .ARN ] |@csv '```

### Certificates

ACM Certs

### Logging

To S3 bucket 

