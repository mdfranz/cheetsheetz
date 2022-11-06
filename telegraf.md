
# Ops

- https://github.com/influxdata/telegraf/releases


# Inputs


Dropping Fields that are bad

I encountered 

```
Jun 25 21:19:20 dell-inspiron-15 telegraf[7719]: 2021-06-26T01:19:20Z E! [outputs.influxdb] E! [outputs.influxdb] Failed to write metric (will be dropped: 400 Bad Request): partial write: field type conflict: input field "allocator_frag_bytes" on measurement "redis" is type float, already exists as type integer dropped=1

```

So dropped it

```
[[inputs.redis]]
   servers = ["tcp://localhost:6379"]
   fielddrop = ["allocator_frag_bytes"]
```

## Disks

To avoid things like  telegraf[4583]: 2022-10-22T06:00:10Z E! [inputs.disk] [SystemPS] => error getting disk usage ("/var/snap/lxd/common/ns/shmounts"): permission denied

```
[inputs.disk]]
  ## By default stats will be gathered for all mount points.
  ## Set mount_points will restrict the stats to only the specified mount points.
  # mount_points = ["/"]

  ## Ignore mount points by filesystem type.
  ignore_fs = ["nsfs","hostfs","gvfs","run","tmpfs", "devtmpfs", "devfs", "iso9660", "overlay", "aufs", "squashfs","fuse.gvfsd-fuse"]

```


## Physical Stuff

```
[[inputs.temp]]
```

## System Utilizaiton

```
[[inputs.cpu]]
  percpu = true
  totalcpu = true
  collect_cpu_time = false
  report_active = false
```

## Containers & Virtualizaiton

Telegraf user must be added to the `docker` group for this to work 

```
[[inputs.docker]]
   endpoint = "unix:///var/run/docker.sock"
```


## Application Endpoints


This was for Benthos

```
[[inputs.http]]
 urls = [
     "http://localhost:4195/metrics",
     "http://localhost:4195/stats"
  ]

data_format = "json"
```




## Networking

```
[[inputs.netstat]]
```

```
[[inputs.ping]]
   urls = ["192.168.1.1","verizon.net","google.com"]
   ping_interval = 5.0
   timeout = 5.0
```

### Interface Stats
``
[[inputs.ethtool]]
    interface_include = ["eth1","eth2"]
``
