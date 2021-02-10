
# Ops

- https://github.com/influxdata/telegraf/releases


# Inputs

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
