
## Writing Data in Python

Here is a simple example with the [put_item](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.put_item) method.

```
def update_hostdb(r):
    """Write data to DynamoDB, create new item or updater timestamp"""

    db = boto3.resource('dynamodb',region_name="us-east-2")
    tbl = db.Table("hosts")

    tbl.put_item(
        Item= {
            'macaddr': r[0],
            'ipaddr': r[1],
            'hostname': r[2],
            'vendor': r[3],
            'timestamp': int(r[4])
        }
    )
```

## Querying Data from the CLI

The quickest way to get a small amount of data out of Database is with a [scan](https://docs.aws.amazon.com/cli/latest/reference/dynamodb/scan.html)

```
aws --region us-east-2 dynamodb scan --table-name hosts --output json | jq .Items
```


