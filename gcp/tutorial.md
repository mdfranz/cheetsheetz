# First Steps

## Installing on Cloud SDK ChromeBook (Crostini amd64/arm64)

From https://github.com/GoogleContainerTools/base-images-docker/issues/50 this worked on my Lenovo S33

```
echo "deb http://packages.cloud.google.com/apt cloud-sdk-stretch main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update -y && apt-get install google-cloud-sdk -y
```

This takes suprisingly long for some reason. 

## Setting up SDK/CLI (this works on Crostini)

```
gcloud auth login
Your browser has been opened to visit:

    https://accounts.google.com/
...
```
Then authorize within the browser

```
$ gcloud config set project <PROJECT>
Updated property [core/project] ```
```

Confirm it works

```
$ gcloud compute instances list
NAME       ZONE           MACHINE_TYPE  PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP  STATUS
wireguard  us-central1-c  f1-micro                   10.128.0.2                TERMINATED
```

You can use the [interactive shell](https://cloud.google.com/sdk/docs/interactive-gcloud) by

```
$ gcloud beta interactive
```

## Running through Docker

See https://cloud.google.com/sdk/docs/downloads-docker

## Config settings

```
$ gcloud config list
[core]
account = XXXX
disable_usage_reporting = True
project = XXXX
```
## Authentication

From https://cloud.google.com/docs/authentication
* Principals - user & service accounts
* Registered Applications - unique identities that present credentials


# IAC Tools
- https://cloud.google.com/foundation-toolkit


## Terraform
- https://cloud.google.com/docs/terraform
- https://github.com/GoogleCloudPlatform/cloud-foundation-toolkit/blob/master/docs/terraform.md

## Deployment Manager
- https://cloud.google.com/deployment-manager
- https://github.com/GoogleCloudPlatform/deploymentmanager-samples/
- https://github.com/GoogleCloudPlatform/cloud-foundation-toolkit/tree/master/dm

# Account Security

## Auditing

- [Cloud Audit Logs](https://cloud.google.com/logging/docs/audit)
- [Managing Log Buckets](https://cloud.google.com/logging/docs/buckets)


