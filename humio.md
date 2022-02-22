# Queries 

## Suricata Examples

Filter out specific ports

```
event_type = "flow" | !in(dest_port,values=[443,53,1900,80,514]) 
```


# Local Docker 

From https://library.humio.com/stable/docs/installation/containers/docker/

```
docker run -v "$(pwd)/mounts:/data"  \
       -v "$(pwd)/mounts/kafka-data:/data/kafka-data"  \
       -v "$(pwd):/etc/humio:ro"  \
       --name=humio --ulimit="nofile=8192:8192"  \
       --env-file="$(pwd)/humio.conf" humio/humio
```
