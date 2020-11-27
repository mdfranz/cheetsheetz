# Primary Abstractions
## Solid

Functional unity of computation with inputs and outputs.

## Pipeline

A dependency graph of build by connecting the inputs and outputs of solids. A set of solids that forms a DAG. 

These can be defined through decoration or through a constructor.

## Repository

## Workspace 

Collection of repositories

## Partitions

# Deployment
- Service
- K8S

# Storage
- Postgres (RDS, Cloud SQL) 
- Object Storage (S3, GCS) 

# Execution 
Pipeline "launching" allocates compute (process, container, K8S pod) to run then executes whereas dagit UI or dagster cli just execute directly.

- Celery / RabbitMQ
- Dask Distributed
- K8S
- Docker 



