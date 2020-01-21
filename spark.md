# Intro Guides

- https://towardsdatascience.com/deep-learning-with-apache-spark-part-1-6d397c16abd

## Components 

### Computing Engine

- Focus on data-loading and computation 
- Uses external storage (Cassandra, Kafka, S3, HDFS, etc.0 

### Libraries

- SQL
- Streaming
- Graph Analytics


### RDD

### Data Frames

Table of Rows & Columns that spans multiple executors (depending on the clustering technology)

These are split into *partitions* which determine the amount of parallism that is possible 

### Transformation 

### Actions

# History / Background

- Limitations and inefficiencies of MapReduce - required multiple passes to get answeres
- Initially was for efficient in-memory queries using functional constructs
- Added interactive console SQL early 

# Architecture

- Programs consist of *driver* and  *executor* <- SparkSession() 
- Console and CLI
- Schedulers/Cluster Managers 

# Languages

Spark translates code in to JVM from 

- Scala
- Python
- R
- Java 

# Schedulers

## Standalone

## YARN

## Mesos

## K8S

- https://spark.apache.org/docs/latest/running-on-kubernetes.html

# Security

- https://spark.apache.org/docs/latest/security.html

# Compatible Frameworks

- TensorFlow
- PyTorch
- R
- Scikit Learn
