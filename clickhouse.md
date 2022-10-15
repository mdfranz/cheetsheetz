

# Python
- https://clickhouse-driver.readthedocs.io/en/latest/
- https://github.com/kszucs/pandahouse

# MySQL

It works

```
ubuntu@clickhouse:~$ mysql -P 9004 -p -u default -h 127.0.0.1
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 3
Server version: 22.9.3.18-ClickHouse

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| name               |
+--------------------+
| INFORMATION_SCHEMA |
| default            |
| information_schema |
| named              |
| system             |
+--------------------+
5 rows in set (0.00 sec)
Read 5 rows, 708.00 B in 0.001327961 sec., 3765 rows/sec., 520.65 KiB/sec.

mysql> show tables;
Empty set (0.02 sec)
Read 0 rows, 0.00 B in 0.001997736 sec., 0 rows/sec., 0.00 B/sec.

mysql> show tables on named;
ERROR 62 (00000): Code: 62. DB::Exception: Syntax error: failed at position 13 ('on'): on named. Expected one of: FROM, IN, NOT, ILIKE, LIKE, WHERE, LIMIT, INTO OUTFILE, FORMAT, SETTINGS, end of query. (SYNTAX_ERROR) (version 22.9.3.18 (official build))
mysql> show tables from named;
+-------+
| name  |
+-------+
| query |
+-------+
1 row in set (0.00 sec)
Read 1 rows, 28.00 B in 0.001833318 sec., 545 rows/sec., 14.91 KiB/sec.

mysql> describe table named.query;
+--------+--------+--------------+--------------------+---------+------------------+----------------+
| name   | type   | default_type | default_expression | comment | codec_expression | ttl_expression |
+--------+--------+--------------+--------------------+---------+------------------+----------------+
| src_ip | String |              |                    |         |                  |                |
| query  | String |              |                    |         |                  |                |
+--------+--------+--------------+--------------------+---------+------------------+----------------+
2 rows in set (0.00 sec)
Read 2 rows, 149.00 B in 0.000636731 sec., 3141 rows/sec., 228.52 KiB/sec.

```

# Configuration Tips

Open up server to all interfaces
```
<listen_host>::</listen_host>
```
