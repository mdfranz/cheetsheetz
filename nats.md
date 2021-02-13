# Ops

## Intro Articles
- [https://hansonkd.medium.com/nats-the-secret-to-microservices-in-go-and-python-that-scale-without-complexity-620f7ca66cc1](NATS: the Secret to Microservices in Go and Python that Scale without Complexity) - 2018
- [https://medium.com/capital-one-tech/lightweight-cloud-native-messaging-with-nats-ad730ca2becf](Lightweight, Cloud-Native Messaging with NATS) - 2018
- [https://oswalt.dev/2019/09/kicking-the-tires-with-the-nats-go-client/](Kicking the Tires With the NATS Go Client)
- [https://www.slideshare.net/wallyqs/sf-python-meetup-introduction-to-nats-messaging-with-python3k](SF Python Meetup - Introduction to NATS Messaging with Python3) - June 2019


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

