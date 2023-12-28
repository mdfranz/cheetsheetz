Summary of [Patterns of Distributed Systems](https://www.oreilly.com/library/view/patterns-of-distributed/9780138222246/) by Unmesh Joshi

# Chapter 1 - Promise and Perils of Distributed Systems

## Scaling 
- Moving beyond a single server and its constraints (compute, network, storage) 
- Separate appserver from database
- Scale out appservers 
- Partition data across multiple DBs 

## Failures

- Hardware
- Networking 
- Software

The real problem is for data replication 

## Chapter 2 - Overview of the Patterns

## Chapter 6 - Leaders and Followers

Pattern: `Have a single server to coordinate replication across a set of servers.`

## Chapter 7 - Heartbeats

Pattern: `Show a server is available by periodically sending a message to all the other servers.`

- Heartbeats like [CARP](https://www.netbsd.org/docs/guide/en/chap-carp.html) advertisements work on a small number of nodes `timeout interval > request interval > network round trip time between the servers` and time sync is required here so 
- Consensus based protocols (Raft, ZooKeeper) heartbeats come from leader to follower 
- Large clusters like Consul uses [GOSSIP](https://developer.hashicorp.com/consul/docs/architecture/gossip) based on [SWIM](https://www.cs.cornell.edu/projects/Quicksilver/public_pdfs/SWIM.pdf) using [Serf](https://www.serf.io/) because heartbeats don't scale to large clusters
