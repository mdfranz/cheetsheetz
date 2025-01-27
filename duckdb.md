# Links
- https://github.com/davidgasquez/awesome-duckdb

# Support Resources 
- [Discord](https://discord.com/invite/tcvwpjfnZx)
- [GitHub Discussions](https://github.com/duckdb/duckdb/discussions)

# Cool Extensions
- [duckdb-pcap](https://github.com/hrbrmstr/duckdb-pcap)

# Useful Doc Links
- [pragmas](https://duckdb.org/docs/sql/pragmas) - how to view stats and make configuration changes.

# Queries
- https://github.com/mdfranz/matano-scripts/tree/main/data/cloudtrail/duckdb

# Blogs
## Parquet
- [Convert or Query Parquet files without Bigdata tool(s)](https://medium.com/datadriveninvestor/convert-or-query-parquet-files-without-bigdata-tool-s-6d58132b99a7)

# Commands to Remember
## Data Loading

### Creating from Parquet

```
create table aws_cloudtrail as select * from "*.parquet";
```

### Loading from JSON

```
create table flow as select * from  "vpc_flow.json";
```

(replace `create table` with `insert into` if the table already exits)

with various [parameters](https://duckdb.org/docs/data/json/overview.html#parameters)

```
create table json_data as select * FROM read_json("./*.json",ignore_errors=true);
```


From CloudTrail 

```
create table ct as select * from read_json("2024-all.json",format='auto',union_by_name=True);
```

Zeek Directories
```
create table ssl as select * from read_json("202*/*ssl*.gz",ignore_errors=true);
```


## Memory Usage
```
PRAGMA database_size;
```

## Output Modes 

```
.mode x
Error: mode should be one of: ascii duckbox box column csv html insert json line list markdown quote table tabs tcl latex trash
```

`d` is the most visually appealing but not efficient but `line` allows you to see more data on the screen.

```
D pragma database_size;
┌───────────────┬────────────┬──────────────┬─────────────┬─────────────┬──────────┬──────────────┬──────────────┐
│ database_size │ block_size │ total_blocks │ used_blocks │ free_blocks │ wal_size │ memory_usage │ memory_limit │
│    varchar    │   int64    │    int64     │    int64    │    int64    │ varchar  │   varchar    │   varchar    │
├───────────────┼────────────┼──────────────┼─────────────┼─────────────┼──────────┼──────────────┼──────────────┤
│ 0 bytes       │          0 │            0 │           0 │           0 │ 0 bytes  │ 107.4MB      │ 2.3GB        │
└───────────────┴────────────┴──────────────┴─────────────┴─────────────┴──────────┴──────────────┴──────────────┘
D .mode line
D pragma database_size;
database_size = 0 bytes
   block_size = 0
 total_blocks = 0
  used_blocks = 0
  free_blocks = 0
     wal_size = 0 bytes
 memory_usage = 107.4MB
 memory_limit = 2.3GB
```
