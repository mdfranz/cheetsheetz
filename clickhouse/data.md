
# Pandas DataFrames with CHDB

CHDB can return a `DataFrame` per [data-formats](https://clickhouse.com/docs/chdb/reference/data-formats) and is as simple as

```
In [25]: q = chdb.query(""" select * from  s3('https://log-bucket.s3.us-east-1.amazonaws.com/*/nginx-access/*/*/*/*.log.gz') where status = 200
       ⋮ """,'DataFrame')
```



# JSON
- https://clickhouse.com/blog/getting-data-into-clickhouse-part-2-json
- https://clickhouse.com/docs/en/integrations/data-formats/json/overview

# Examples with S3

## BedRock

```
select * from s3('https://abucket.s3.us-east-1.amazonaws.com/AWSLogs/*/BedrockModelInvocationLogs/*/2025/*/*/*/*.gz') 
```

## Zeek 
Get the schema

```
DESCRIBE TABLE s3('https://abucket.s3.us-east-2.amazonaws.com/2024-12-08/conn*gz')
FORMAT csv

Query id: d01f8ab3-5116-40b1-a064-e4034eaffc34

"ts","Nullable(Float64)","","","","",""
"uid","Nullable(String)","","","","",""
"id.orig_h","Nullable(String)","","","","",""
"id.orig_p","Nullable(Int64)","","","","",""
"id.resp_h","Nullable(String)","","","","",""
"id.resp_p","Nullable(Int64)","","","","",""
"proto","Nullable(String)","","","","",""
"service","Nullable(String)","","","","",""
"duration","Nullable(Float64)","","","","",""
"orig_bytes","Nullable(Int64)","","","","",""
"resp_bytes","Nullable(Int64)","","","","",""
"conn_state","Nullable(String)","","","","",""
"local_orig","Nullable(Bool)","","","","",""
"local_resp","Nullable(Bool)","","","","",""
"missed_bytes","Nullable(Int64)","","","","",""
"history","Nullable(String)","","","","",""
"orig_pkts","Nullable(Int64)","","","","",""
"orig_ip_bytes","Nullable(Int64)","","","","",""
"resp_pkts","Nullable(Int64)","","","","",""
"resp_ip_bytes","Nullable(Int64)","","","","",""
"ja4l","Nullable(String)","","","","",""
"ja4ls","Nullable(String)","","","","",""
"ja4t","Nullable(String)","","","","",""
"ja4ts","Nullable(String)","","","","",""

24 rows in set. Elapsed: 8.331 sec. 

:)
```

Use an LLM to convert to `CREATE TABLE`

```
cat conn-schema.csv | llm -m 4 "convert this to a clickhouse create table command ignoring Nullable"
CREATE TABLE IF NOT EXISTS my_table
(
    ts Float64,
    uid String,
    id_orig_h String,
    id_orig_p Int64,
    id_resp_h String,
    id_resp_p Int64,
    proto String,
    service String,
    duration Float64,
    orig_bytes Int64,
    resp_bytes Int64,
    conn_state String,
    local_orig Bool,
    local_resp Bool,
    missed_bytes Int64,
    history String,
    orig_pkts Int64,
    orig_ip_bytes Int64,
    resp_pkts Int64,
    resp_ip_bytes Int64,
    ja4l String,
    ja4ls String,
    ja4t String,
    ja4ts String
) ENGINE = MergeTree() ORDER BY ts;
```

Now insert

```
:) insert into my_table select * from  s3('https://abucket.s3.us-east-2.amazonaws.com/20*/conn*gz') SETTINGS input_format_skip_unknown_fields = 1;

INSERT INTO my_table
SETTINGS input_format_skip_unknown_fields = 1
SELECT *
FROM s3('https://abucket.s3.us-east-2.amazonaws.com/20*/conn*gz')
SETTINGS input_format_skip_unknown_fields = 1
0 rows in set. Elapsed: 95.955 sec. Processed 18.36 million rows, 818.30 MB (191.31 thousand rows/s., 8.53 MB/s.)
Peak memory usage: 1.81 GiB.

:) select count(*) from my_table;
```

