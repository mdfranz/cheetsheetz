# Mailing Lists and Things to Monitor
- [fwd:cloudsec](https://fwdcloudsec.org/forum/)
- [AWS Security Digest](https://awssecuritydigest.com/)
- [AWS Cloud Security Weekly](https://aws-cloudsec.com/)
- [CloudSecList](https://cloudseclist.com/)

# Conferences
- [fwd:cloudsec](https://fwdcloudsec.org/conference/north-america/)
- [re:Inforce](https://reinforce.awsevents.com/)

# Links Pages
- [CloudSecDocs](https://cloudsecdocs.com/)
- [Hacking the Cloud](https://hackingthe.cloud/)
- [s0cm0nkey Cloud Resources]( https://github.com/s0cm0nkey/Security-Reference-Guide/blob/main/cloud.md) 
- https://github.com/Funkmyster/awesome-cloud-security
- https://github.com/4ndersonLin/awesome-cloud-security

## Tools
- [toniblyx: aws security tools](https://github.com/toniblyx/my-arsenal-of-aws-security-tools)

# General
- [The values behind scaling cloud native security at Grafana Labs](https://grafana.com/blog/2021/12/20/the-values-behind-scaling-cloud-native-security-at-grafana-labs/) - December 2021 
- [What to look for when reviewing a company's infrastructure](https://www.marcolancini.it/2022/blog-cloud-security-infrastructure-review/) - March 2022
- [Cloud Security Orienteering](https://tldrsec.com/blog/cloud-security-orienteering/)
- [On Establishing a Cloud Security Program](On Establishing a Cloud Security Program) - May 2021

# AWS
- [AWS Security Reference Architecture Examples](https://github.com/aws-samples/aws-security-reference-architecture-examples) which is the CloudFormation and Terraform code for [SRA](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/welcome.html)
- [GuardDuty Runbook Generator](https://github.com/aquia-inc/aws-guardduty-runbook-generator) 
- [Automated Incident Response and Forensics Framework](https://github.com/awslabs/aws-automated-incident-response-and-forensics) and https://github.com/aws-samples/aws-customer-playbook-framework
- [AWS Well Architected Security Labs](https://wellarchitectedlabs.com/security/)
- [Awesome AWS Security](https://github.com/jassics/awesome-aws-security)
- [Complete AWS Security Maturity Model](https://maturitymodel.security.aws.dev/en/model/)
- [Permissions Cloud](https://aws.permissions.cloud/)
- [So You Inherited an AWS Account](https://medium.com/swlh/so-you-inherited-an-aws-account-e5fe6550607d) - April 2020
- [AWS Organizations in 2021](https://www.chrisfarris.com/post/aws-organizations-in-2021/)
- [AWS Security Incident Response Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/aws-security-incident-response-guide.html) - November 2020

## Detection Rules
- [Elastic](https://github.com/elastic/detection-rules/tree/main/rules/integrations/aws)

## Adversary Emulation Tools
- [Stratus Red Team](https://github.com/DataDog/stratus-red-team)
- [Pacu](https://github.com/RhinoSecurityLabs/pacu)
- [CloudSaga](https://github.com/awslabs/aws-cloudsaga)

## Ransomware 
- [Introducing the Ransomware Risk Management on AWS Whitepaper](https://aws.amazon.com/blogs/security/introducing-the-ransomware-risk-management-on-aws-whitepaper/) - Sept 2021
- [NISTIR 7374](https://docs.aws.amazon.com/whitepapers/latest/ransomware-risk-management-on-aws-using-nist-csf/nistir-8374-ransomware-profile.html)
- [Detecting ransomware activities within AWS environments](https://lantern.splunk.com/Security/Use_Cases/Threat_Hunting/Detecting_ransomware_activities_within_AWS_environments)
- [AWS re:Invent 2020: Ransomware: Be prepared](https://www.youtube.com/watch?v=JQ4LWp3Bf20)
- [Ransomware Mitigation]( https://aws.amazon.com/it/blogs/security/ransomware-mitigation-top-5-protections-and-recovery-preparation-actions/)

## Logs
- [Overview of AWS Logs](https://dev-website.lab-terraform.mhg.ovh/overview-of-aws-logs.html) - October 2020

## IR

### GCP
- [Google Cloud Incident Response Cheat Sheet](https://medium.com/google-cloud/google-cloud-incident-response-cheat-sheet-dfde9054ac16) - Jan 2024
- https://github.com/google/gcp_scanner

### Azure
- [How to be IR prepared in Azure](https://www.cadosecurity.com/how-to-be-ir-prepared-in-azure/) - Feb 2024

### AWS
- [How to be IR Prepared in AWS](https://www.cadosecurity.com/how-to-be-ir-prepared-in-aws/)
- [AWS Forensics Presciptive Guidance](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/cyber-forensics.html)
- [AWS Security Hub Automated Response and Remediation](https://github.com/aws-solutions/aws-security-hub-automated-response-and-remediation)
- [AWS Incident Response Playbook Samples](https://github.com/aws-samples/aws-incident-response-playbooks)
- [AWS Security Incident Response Guide](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/welcome.html) - Nov 2020

## IAM
- https://ramimac.me/aws-iam-tools-2024
- [IAMActionHunter](https://github.com/RhinoSecurityLabs/IAMActionHunter)
- [Pmapper](https://github.com/nccgroup/PMapper)
- [AWS Lambda Function: IAM User Password Expiry Notice | SES, Boto3 & Terraform](https://blog.jennasrunbooks.com/aws-lambda-function-iam-user-password-expiry-notice-ses-boto3-terraform)j
- [iamlive](https://github.com/iann0036/iamlive) - Generate an IAM policy from AWS, Azure, or Google Cloud (GCP) calls using client-side monitoring (CSM) or embedded proxy

## IMDS
- [Add defense in depth against open firewalls, reverse proxies, and SSRF vulnerabilities with enhancements to the EC2 Instance Metadata Service](https://aws.amazon.com/blogs/security/defense-in-depth-open-firewalls-reverse-proxies-ssrf-vulnerabilities-ec2-instance-metadata-service/)

# Azure
- [WithSecure Azure Security Framework](https://www.withsecure.com/content/dam/with-secure/en/resources/withsecure-consulting-microsoft-azure-security-framework-guide-en.pdf)
- [Azure Threat Matrix](https://microsoft.github.io/Azure-Threat-Research-Matrix/)

# Containers 
- [Container Security Checklist: From Image to Workload](https://github.com/krol3/container-security-checklist)
- [Top 20 Dockefile best Practices](https://sysdig.com/blog/dockerfile-best-practices/) - Sysdig, March 2021

# K8S
- [Detection Engineering for Kubernetes clusters](https://research.nccgroup.com/2021/11/10/detection-engineering-for-kubernetes-clusters/)

See [../k8sec.md](k8sec.md)

- [WithSecureLabs](https://github.com/WithSecureLabs) as a bunch of tools

## As Code
- [hysnec - awesome policy as code](https://github.com/hysnsec/awesome-policy-as-code)
- [Terraformer](https://github.com/GoogleCloudPlatform/terraformer)

## Forensics
- [Cloud Forensic Utils](https://github.com/google/cloud-forensics-utils)
- [Automated Incident Response & Forensics Framework](https://github.com/awslabs/aws-automated-incident-response-and-forensics)
- [AWS Incident Response](https://github.com/easttimor/aws-incident-response)

## IAM
- https://github.com/aws-samples/iam-access-key-report

## CloudTrail
- https://github.com/flosell/trailscraper


# Misc
- [Lateral movement risks in the cloud and how to prevent them – Part 1: the network layer (VPC)](https://www.wiz.io/blog/lateral-movement-risks-in-the-cloud-and-how-to-prevent-them-part-1-the-network-layer)

# CTD
- [cloudfoxable](https://github.com/BishopFox/cloudfoxable)

# Vendors 
- https://www.cadosecurity.com
- 
