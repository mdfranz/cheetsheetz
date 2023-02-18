# Blogs
## Parquet
- [Convert or Query Parquet files without Bigdata tool(s)](https://medium.com/datadriveninvestor/convert-or-query-parquet-files-without-bigdata-tool-s-6d58132b99a7)




# Commands to Remember

## Creating from Parquet

```
create table aws_cloudtrail as select * from "*.parquet";
```

## Memory Usage
```
PRAGMA database_size;
```

## Modes 

```
.mode x
Error: mode should be one of: ascii duckbox box column csv html insert json line list markdown quote table tabs tcl latex trash
```

