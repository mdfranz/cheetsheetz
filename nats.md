# Intro Articles
- [NATS: the Secret to Microservices in Go and Python that Scale without Complexity](https://hansonkd.medium.com/nats-the-secret-to-microservices-in-go-and-python-that-scale-without-complexity-620f7ca66cc1) - 2018
- [Lightweight, Cloud-Native Messaging with NATS](https://medium.com/capital-one-tech/lightweight-cloud-native-messaging-with-nats-ad730ca2becf) - 2018
- [Kicking the Tires With the NATS Go Client](https://oswalt.dev/2019/09/kicking-the-tires-with-the-nats-go-client/)
- [SF Python Meetup - Introduction to NATS Messaging with Python3](https://www.slideshare.net/wallyqs/sf-python-meetup-introduction-to-nats-messaging-with-python3k)
- June 2019
- [Building Distributed Event Streaming Systems In Go With NATS JetStream](https://shijuvar.medium.com/building-distributed-event-streaming-systems-in-go-with-nats-jetstream-3938e6dc7a13) - May 2021
- [NATS Messaging - Part 1](https://choria.io/blog/post/2020/03/23/nats_patterns_1/) and [Part 6](https://choria.io/blog/post/2020/03/30/nats_patterns_6/)

## Comps
- [Contrasting NATS with Apache Kafka](https://itnext.io/contrasting-nats-with-apache-kafka-1d3bdb9aa767)

# Ops
## Get & Config
- https://github.com/nats-io/nats-server/releases
- https://docs.nats.io/nats-server/configuration
- https://github.com/nats-io/natscli

## Monitoring
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
- https://github.com/nats-io/natscli - This should have everything now for 2.2.x

# Hello World-ish

```
go get github.com/nats-io/go-nats-examples/tools/nats-pub
go get github.com/nats-io/go-nats-examples/tools/nats-sub`
```

And follow https://docs.nats.io/nats-server/clients

# Videos
- [Think Differently](https://www.youtube.com/watch?v=ud-cdirF8OA) - OSCON 2019


# Sample Code & Projects (JetStream)
## Golang
- https://github.com/pkbhowmick/nats-demo
