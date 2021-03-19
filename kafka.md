# Concepts

## Record

Basic unit of persistence that consists of 

- key - not unique like a primary key 
- value
- partition number
- offset
- timestamp

## Topic

Stream of data, comparable to a table in database. Append-only log that may only be changed by the producer (immutable)

Topics are split into partiions, spread across brokers. 

Each message within a topic has an incremental offset. Offset is only meaningful in a partition. Order is only guaranteed within a parition. 

Partitions are unbounded.

Events are randomly assigned to a partition unless there is a key.

## Broker

Clusters consit of multiple brokers. 

Each broker has a unique id.

Bootstrap Broker - just connector to one


## Producers

## Consumers

Retrieving a record from a topic does not remove from the topic and maintain an offset after each read

*Consumer Groups* serve as Load balancing mechanisms for distributing partition assignment across consumer instances in the group


# Overall Ecosystem

- https://medium.com/@stephane.maarek/the-kafka-api-battle-producer-vs-consumer-vs-kafka-connect-vs-kafka-streams-vs-ksql-ef584274c1e


# Simple Tutorials
- https://codetober.com/apache-kafka-on-raspberry-pi-4/
- https://medium.com/better-programming/a-simple-apache-kafka-cluster-with-docker-kafdrop-and-python-cf45ab99e2b9
- https://dattell.com/data-architecture-blog/understanding-kafka-consumer-offset/

# Streaming

- https://medium.com/high-alpha/data-stream-processing-for-newbies-with-kafka-ksql-and-postgres-c30309cfaaf8
- https://www.jesse-anderson.com/2019/10/why-i-recommend-my-clients-not-use-ksql-and-kafka-streams/

# Infrastructure & Deployment

# FOSS Admin Tools
- https://github.com/provectus/kafka-ui
- https://github.com/obsidiandynamics/kafdrop
- https://github.com/edenhill/kafkacat

## Docker Compose
- https://github.com/confluentinc/cp-all-in-one
- https://github.com/simplesteph/kafka-stack-docker-compose

## K8S
- (Strizi)[https://strimzi.io/]
- https://www.confluent.io/blog/getting-started-apache-kafka-kubernetes/ - (2018) 
- https://dzone.com/articles/ultimate-guide-to-installing-kafka-docker-on-kuber
- https://phoenixnap.com/kb/kafka-on-kubernetes
- https://technology.amis.nl/2019/03/24/running-apache-kafka-on-minikube/ (2019) 
