Example using [s3m](https://s3m.stream/)

```
#!/bin/bash

# Get Credentials from Resources
AWS_9431=$(curl -s -H "Authorization: Bearer $WM_TOKEN" \
  "$BASE_INTERNAL_URL/api/w/$WM_WORKSPACE/resources/get_value_interpolated/u/mdfranz/aws_9431" | jq)

export ACCESS_KEY=`echo $AWS_9431 | jq .awsAccessKeyId`
export SECRET_KEY=`echo $AWS_9431 | jq .awsSecretAccessKey`

# Download S3M
wget -q https://github.com/s3m/s3m/releases/download/0.10.0/s3m-0.10.0-x86_64-unknown-linux-musl.tar.gz
tar xzf s3m-0.10.0-x86_64-unknown-linux-musl.tar.gz
cd s3m-0.10.0-x86_64-unknown-linux-musl

# Create config

cat << EOF > config.yaml
hosts:
  aws:
    region: us-east-1
    access_key: ${ACCESS_KEY}
    secret_key: ${SECRET_KEY}
EOF

./s3m --config config.yaml ls aws
```
