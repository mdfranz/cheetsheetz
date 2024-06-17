# Blogs
- [AWS CLI with jq and Bash](https://medium.com/circuitpeople/aws-cli-with-jq-and-bash-9d54e2eabaf1)
- [Dig into API calls on AWS with cloudtrail and jq](https://medium.com/@pascalwhoop/dig-into-api-calls-on-aws-with-cloudtrail-and-jq-38899c89b9ab)
- [Quick and Dirty CloudTrail Threat Hunting Log Analysis](https://medium.com/@george.fekkas/quick-and-dirty-cloudtrail-threat-hunting-log-analysis-b64af10ef923)
- [JSON object values into CSV with jq](https://qmacro.org/blog/posts/2022/05/19/json-object-values-into-csv-with-jq/)

# Some examples


## Google StackDriver logs to pull out .message
```
[
  {
    "insertId": "u8zf22fb5neif",
    "jsonPayload": {
      "message": "2024-03-21T00:50:08.774508+00:00 localhost systemd[1]: Finished gce-workload-cert-refresh.service - GCE Workload Certificate refresh."
    },
````

is

```
jq '.[].jsonPayload.message' downloaded-logs-20240320-205148.json  | grep ollama | tac | less
```

## CloudTrail
See https://github.com/warlocksmurf/jq-cheatsheet

You can crawl by doing:
```
find . -name "*.json.gz" | xargs gzcat | jq '.Records[] | .userIdentity | select(.type == "AssumedRole")' | less
```
Creating SQL

```
find . -name "*202403*.json.gz" | xargs gzcat | jq -r '.Records[] | [.eventTime, .eventSource, .eventCategory, .readOnly, .eventName, .awsRegion, .sourceIPAddress]| @csv'
```

```
jq '.Records[] | .userIdentity | select(.type == "AssumedRole")'
jq '.Records[] | .userIdentity | select(.type == "AssumedRole")|.sessionContext|.sessionIssuer|.userName'
jq '.Records[] | .sourceIPAddress' | egrep -v '(amazon|AWS)' | sort | uniq -c | sort -n | head -30
```




