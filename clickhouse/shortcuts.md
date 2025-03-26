# Copying Table Schema

See [raw formats](https://clickhouse.com/docs/interfaces/formats/RawBLOB#raw-formats-comparison) 
```
show create table table_name format TSVRaw
```

# Inserting into local database from remote

```
INSERT INTO local_table
SELECT *
FROM remote('clickhouse_ip:9000', 'remote_table', 'default', 'password');
```
