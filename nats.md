# Ops

## Get & Config
- https://github.com/nats-io/nats-server/releases
- https://github.com/nats-io/nats-streaming-server/releases
- https://docs.nats.io/nats-server/configuration

## Monitor
- https://docs.nats.io/nats-tools/nats_top


Monitoring with Telegraf

```
[[inputs.httpjson]]
   name = "nats"
   servers = [
     "http://localhost:8222/varz",
   ]
   method = "GET"
```

## Management

- https://docs.nats.io/nats-tools/nsc


# Hello World-ish

```
go get github.com/nats-io/go-nats-examples/tools/nats-pub
go get github.com/nats-io/go-nats-examples/tools/nats-sub`
```

And follow https://docs.nats.io/nats-server/clients

# Libraries
- https://github.com/nats-io/nats.rs
- https://github.com/nats-io/stan.py

# Videos
[Think Differently](https://www.youtube.com/watch?v=ud-cdirF8OA) - OSCON 2019

