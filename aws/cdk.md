# Installation
Get nodejs (LTS) from https://nodejs.org/download/release/latest-v20.x/

Get it (NPM, not HomeBrew)
```
npm install -g aws-cdk

```

Get Python Dependencies (Ubuntu/Debian)

```
apt -y install python3-pip python3-venv
```

# Blogs
## Python Development
- [How To Setup AWS EC2 Instance Usi ng AWS CDK Python](https://unbiased-coder.com/setup-aws-ec2-instance-cdk-python/)
- [Build Your First AWS CDK Project](https://towardsdatascience.com/build-your-first-aws-cdk-project-18b1fee2ed2d) 

## Other CDK
- [Provision an Ubuntu-based EC2 instance with CDK](https://loige.co/provision-ubuntu-ec2-with-cdk/)

## From Terraform
- [From Terraform to CDK](https://medium.com/carsales-dev/from-terrafrom-to-cdk-our-journey-of-migrating-existing-aws-resource-to-cdk-managed-f533416a4254) - May 2021

## EKS (Python and TypeScript)
- [Deploying an EKS Cluster with AWS Cloud Development Kit (CDK)](https://aws.plainenglish.io/deploying-an-eks-cluster-with-aws-cloud-development-kit-cdk-afdb96ce3a83) - March 2024
- [AWS: CDK and Python – building an EKS cluster, and general impressions of CDK](https://rtfm.co.ua/en/aws-cdk-and-python-building-an-eks-cluster-and-general-impressions-of-cdk/) - July 2023
- [AWS CDK (Python) How to Create EKS Cluster](https://ramasankarmolleti.com/2021/02/25/aws-cdk-python-how-to-create-eks-cluster/)
- [Automating EKS Deployment and NGINX Setup Using Helm with AWS CDK in Python](https://dev.to/marocz/automating-eks-deployment-and-nginx-setup-using-helm-with-aws-cdk-in-python-27mn) - April 2024
- [Managing K8S Infrastructure and Applications on AWS: The Imperative Way](https://xebia.com/blog/managing-k8s-infrastructure-and-applications-on-aws/) and [sample code](https://github.com/binxio/aws-cdk-and-cdk8s-example-project)
- https://github.com/aws-quickstart/cdk-eks-blueprints

# Tools 
- https://github.com/tinystacks/precloud

# References
- [Security & Safety Dev Guide](https://github.com/aws/aws-cdk/wiki/Security-And-Safety-Dev-Guide)
- [AWS CDK Workshop](https://cdkworkshop.com/)
- [Python Reference](https://docs.aws.amazon.com/cdk/api/v2/python/index.html)
- [Python Construct Library](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_ec2/README.html)
- [Environments](https://docs.aws.amazon.com/cdk/v2/guide/environments.html)

## Common Python Modules 

[V2 Modules](https://docs.aws.amazon.com/cdk/api/v2/python/modules.html)

- [IAM](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_iam/README.html)
- [CloudWatch Logs](https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_logs/README.html)


# Sample Projects
## OpenSearch
- https://github.com/patrickmryan/opensearch-cdk
- https://github.com/ryparker/aws-cdk-sample-opensearch-python

# Concepts
From https://docs.aws.amazon.com/cdk/v2/guide/home.html

Apps are build from [Constructs](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html) which represent [AWS Resources at various levels](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-construct-library.html)

Apps contain [Stacks](https://docs.aws.amazon.com/cdk/v2/guide/apps.html)




