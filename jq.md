# Blogs
- [AWS CLI with jq and Bash](https://medium.com/circuitpeople/aws-cli-with-jq-and-bash-9d54e2eabaf1) 



# Some annoything things to remember

Google StackDriver logs to pull out .message

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
