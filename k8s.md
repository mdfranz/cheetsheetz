
# Arm 64 Linux Hoops

From https://github.com/GoogleContainerTools/base-images-docker/issues/50 this worked on my Lenovo S33

```
echo "deb http://packages.cloud.google.com/apt cloud-sdk-stretch main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update -y && apt-get install google-cloud-sdk -y
```

This is will gcloud and kubectl
