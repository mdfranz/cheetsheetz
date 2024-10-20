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
