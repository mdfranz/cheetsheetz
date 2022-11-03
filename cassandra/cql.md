# Keyspaces


```
cqlsh> DESC keyspaces

store   system_auth         system_schema  system_views
system  system_distributed  system_traces  system_virtual_schema


cqlsh> describe keyspace bind

CREATE KEYSPACE bind WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '1'}  AND durable_writes = true;
```

# Tables


```
cqlsh> desc tables

Keyspace store
--------------
shopping_cart

Keyspace system
---------------
available_ranges     paxos_repair_history  sstable_activity
available_ranges_v2  peer_events           sstable_activity_v2
batches              peer_events_v2        table_estimates
built_views          peers                 top_partitions
compaction_history   peers_v2              transferred_ranges
"IndexInfo"          prepared_statements   transferred_ranges_v2
local                repairs               view_builds_in_progress
paxos                size_estimates

Keyspace system_auth
--------------------
network_permissions             role_members      roles
resource_role_permissons_index  role_permissions

Keyspace system_distributed
---------------------------
parent_repair_history  partition_denylist  repair_history  view_build_status

Keyspace system_schema
----------------------
aggregates  dropped_columns  indexes    tables    types
columns     functions        keyspaces  triggers  views

Keyspace system_traces
----------------------
events  sessions

Keyspace system_views
---------------------
batch_metrics              internode_outbound              repair_sessions
caches                     jmx_permissions_cache_keys      repair_validations
clients                    local_read_latency              repairs
coordinator_read_latency   local_scan_latency              roles_cache_keys
coordinator_scan_latency   local_write_latency             rows_per_read
coordinator_write_latency  max_partition_size              settings
cql_metrics                network_permissions_cache_keys  sstable_tasks
credentials_cache_keys     pending_hints                   streaming
disk_usage                 permissions_cache_keys          system_properties
gossip_info                repair_jobs                     thread_pools
internode_inbound          repair_participates             tombstones_per_read

Keyspace system_virtual_schema
------------------------------
columns  keyspaces  tables
```
