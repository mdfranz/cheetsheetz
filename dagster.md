# Primary Abstractions
## Solids

Functional unity of computation with inputs and outputs. Meant to be re-useable chunks of business logic. 

There can also be `composite_solids` 

Something with `.alias`

## Pipelines

A dependency graph of build by connecting the inputs and outputs of solids. A set of solids that forms a DAG. 

These can be defined through decoration or through a constructor.

## Repository

## Workspace 

Collection of repositories

## Partitions

# Deployment

See https://docs.dagster.io/deploying/local

## Service

`dagit` is run by systemd as long as proper environment variables are set and proper workspace is configured and path where pipeline code runs

## ECS/K8S




# Storage
- Postgres (RDS, Cloud SQL) 
- Object Storage (S3, GCS) 

# Execution 
Pipeline "launching" allocates compute (process, container, K8S pod) to run then executes whereas dagit UI or dagster cli just execute directly.

- Celery / RabbitMQ
- Dask Distributed
- K8S
- Docker 



