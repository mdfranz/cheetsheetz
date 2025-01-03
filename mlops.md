This page covers MLOps and DataOps/Eng topics. I started this in early 2020. Also see [dataeng](dataeng.md)

# General Articles, Blogs, and Talks
- [Hidden Tech Debt in Machine Learning Systems](https://papers.nips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html) - 2015 paper that laid the foundations
- [InnoQ MLOps Site](https://ml-ops.org/) - this looks dormant but provides the state of things and problem definition in late 2019 early 2020

## Principles & Meta
- [What are Model Governance and Model Operations](https://www.oreilly.com/radar/what-are-model-governance-and-model-operations/) (OReilly, June 2019)
- [DataOps Manifesto](https://www.dataopsmanifesto.org/)
- [The Rise of the Term “MLOps:” Properly Operationalized Machine Learning is the New Holy Grail](https://towardsdatascience.com/the-rise-of-the-term-mlops-3b14d5bd1bdb)
- [MLOps: ML Engineering Best Practices from the Trenches](https://cdn2.hubspot.net/hubfs/4584542/Conference%20Slides/2019_ODSCwest_MLOps.pdf) - 2019
- [Bristech 2019 Luke Marsdon - The future of MLOps](https://www.youtube.com/watch?v=UW2SzLwA4Xc) - 2019 
- [Reimagining DevOps for ML by Elle O'Brien, Iterative.ai](https://www.youtube.com/watch?v=0MDrZpO_7Q4&list=PLVeJCYrrCemgbA1cWYn3qzdgba20xJS8V) - 2020
- [Machine learning deserves its own flavor of Continuous Delivery](https://towardsdatascience.com/machine-learning-deserves-its-own-flavor-of-continuous-delivery-f4d1e76e6b69) - April 2020
- [MLOps — Is it a Buzzword??? Part -1](https://medium.com/walmartglobaltech/mlops-is-it-a-buzzword-part-1-8573fe95290e) - June 2021, Walmart Labs

## Practices
- [Building an End-to-End MLOps Pipeline with Open-Source Tools](https://medium.com/infer-qwak/building-an-end-to-end-mlops-pipeline-with-open-source-tools-d8bacbf4184f) - Nov 2023
- [This is how you set up an MLOps platform on AWS EKS with Kubeflow and MLflow](https://medium.com/ubuntu-ai/kubeflow-mlflow-on-eks-136b672e9afa)
- [Productionizing Machine Learning Models with MLOps](https://www.xenonstack.com/blog/mlops/)
- [Deploying ML Models in Distributed Real-time Data Streaming Applications](https://www.kharekartik.dev/2020/01/12/streaming-machine-learning/)
- [Architecting a Machine Learning Pipeline How to build scalable Machine Learning systems — Part 2/2](https://towardsdatascience.com/architecting-a-machine-learning-pipeline-a847f094d1c7)
- [Being a Data Scientist does not make you a Software Engineer!](https://towardsdatascience.com/being-a-data-scientist-does-not-make-you-a-software-engineer-c64081526372)
- [Deploying Python ML Models with Flask, Docker and Kubernetes](https://alexioannides.com/2019/01/10/deploying-python-ml-models-with-flask-docker-and-kubernetes/)
- [Deploying and Versioning Data Piplines at Scale](https://medium.com/@QuantumBlack/deploying-and-versioning-data-pipelines-at-scale-942b1d81b5f5)
- [CI/CD + ML == MLOps - The Way To Speed Bringing Machine Learning To Production - David Aronchick](https://www.youtube.com/watch?v=uOCR4Xw-BZ8) - this as well!
- [Data Pipelines @ Samsara](https://medium.com/samsara-engineering/data-pipelines-samsara-64596dbc2137) - March 2021
- [Continuous Delivery For Machine Learning: Patterns And Pains - Emily Gorcenski](https://www.youtube.com/watch?v=bFW5mZmj0nQ) - great talk, I saw this in person in January 2020.

# Maturity Modesl
- [Microsoft MLOps Maturity Model](https://learn.microsoft.com/en-us/azure/architecture/example-scenario/mlops/mlops-maturity-model)

# Relevant Research & Serious Articles
- [Hidden Tech Debt in Machine Learning Systems](https://papers.nips.cc/paper/5656-hidden-technical-debt-in-machine-learning-systems.pdf)
- [Continuous Delivery for Machine Learning](https://martinfowler.com/articles/cd4ml.html)
- [Coding habits for data scientists](https://www.thoughtworks.com/insights/blog/coding-habits-data-scientists)
- [Continuous Delivery for Machine Learning: Automating the end-to-end lifecycle of Machine Learning application](https://martinfowler.com/articles/cd4ml.html)
- [What Is MLOps And Why Your Team Should Implement It](https://medium.com/smb-lite/what-is-mlops-and-why-your-team-should-implement-it-b05b741cdf94) 

# Conferences & Workshops
- https://www.mlopsnyc.com/agenda-sessions - see https://www.youtube.com/channel/UChmi6ZzsZd9doYYVut1ppUg
- https://www.usenix.org/sites/default/files/opml19_full_proceedings.pdf
- https://github.com/thoughtworksInc/CD4ML-Scenarios

# Tooling
- [Deploying Python ML Models with Flask, Docker and Kubernetes](https://alexioannides.com/2019/01/10/deploying-python-ml-models-with-flask-docker-and-kubernetes/)
- [MLOps, Kubeflow, and Tekton - Simon Kaegi, IBM](https://www.youtube.com/watch?v=npQkdeU2cEM)
- [End-to-end Machine Learning Platforms Compared](https://towardsdatascience.com/end-to-end-machine-learning-platforms-compared-c530d626151b)

## Dagster
- See [Dagster](dagster/)

## Metaflow (Netflix) 
- [Metaflow](https://metaflow.org/) 
- [source](https://github.com/Netflix/metaflow)
- [Open-Sourcing Metaflow, a Human-Centric Framework for Data Science](https://netflixtechblog.com/open-sourcing-metaflow-a-human-centric-framework-for-data-science-fa72e04a5d9)

## Mlfow (DataBricks)
- [Simplifying Model Management with MLflow](https://databricks.com/session_eu19/1-simplifying-model-management-with-mlflow)
- [mlfow](https://www.mlflow.org/) - an open source platform for managing the end-to-end machine learning lifecycle. It tackles three primary functions: 1) tracking experiments to record and compare parameters and results 2) packaging ML code in a reusable, reproducible form in order to share with other data scientists or transfer to production 3) managing and deploying models from a variety of ML libraries to a variety of model serving and inference platforms (MLflow Models). By [Databricks](https://databricks.com)

## Feature Stores
- [Feast](https://feast.dev/)
- [Hopsworks](https://github.com/logicalclocks/hopsworks)

## Kubeflow
- [Accelerating Machine Learning App Development with Kubeflow Pipelines (Cloud Next '19](https://www.youtube.com/watch?v=TZ1lGrJLEZ0)
- [Kubeflow: Simplified, Extended and Operationalized](https://towardsdatascience.com/kubeflow-simplified-extended-and-operationalized-fcbcc34f79e5)

## General K8s
- [Seldon](https://github.com/SeldonIO) - Seldon Core an open source platform for deploying machine learning models on a Kubernetes cluster.
- [Argo CD](https://argoproj.github.io/argo-cd/) 
- [Flyte](https://lyft.github.io/flyte/) - a structured programming and distributed processing platform created at Lyft that enables highly concurrent, scalable and maintainable workflows for machine learning and data processing.
- [

## Mleap
- https://medium.com/rv-data/mleap-providing-near-real-time-data-science-with-apache-spark-c34e7df093ca
- https://github.com/combust/mleap

## Spark
- [Best Practices for Building and Deploying Data Pipelines in Apache Spark - Vicky Avison](https://www.youtube.com/watch?v=1WUIua-xjJA)
- [Waimak](https://github.com/CoxAutomotiveDataSolutions/waimak) - an open-source framework that makes it easier to create complex data flows in Apache Spark

## Data Versioning & Validation 
- [DVC](https://dvc.org/) - is built to make ML models shareable and reproducible. It is designed to handle large files, data sets, machine learning models, and metrics as well as code.

### DBT
- [DBT](https://www.getdbt.com/)
- [Taming the Dependency Hell with dbt](https://medium.com/tiqets-tech/taming-the-dependency-hell-with-dbt-2491771a11be) - March 2021

### Great Expectations
- [Great Expectations](https://github.com/great-expectations/great_expectations) -  helps teams save time and promote analytic integrity by offering a unique approach to automated testing: pipeline tests. Pipeline tests are applied to data (instead of code) and at batch time (instead of compile or deploy time). Pipeline tests are like unit tests for datasets: they help you guard against upstream data changes and monitor data quality and https://greatexpectations.io/
- [Using GitHub Actions for MLOps & Data Science](https://github.blog/2020-06-17-using-github-actions-for-mlops-data-science/)
- [Keeping your data pipelines healthy with the Great Expectations GitHub Action](https://github.blog/2020-10-01-keeping-your-data-pipelines-healthy-with-the-great-expectations-github-action/)
- [Great Expectations: Validating datasets in machine learning pipelines](https://blog.codecentric.de/en/2020/02/great-expectations-validating-datasets-in-machine-learning-pipeline/)
- [Database Testing with Great Expectations](https://blog.testproject.io/2020/06/24/database-testing-with-great-expectations/) - June 2020

## Other Open Source Tools 
- [Apache Camel](https://camel.apache.org/)
- [Airbyte](https://github.com/airbytehq/airbyte)
- [Benthos (now RedPanda Connect](https://github.com/redpanda-data/connect) 
- [Kedro](https://github.com/quantumblacklabs/kedro) - an open source development workflow tool that helps structure reproducible, scaleable, deployable, robust and versioned data pipelines (by [Quantum Black Labs](https://www.quantumblack.com/labs/)])
- [H20 AutoML](https://www.h2o.ai/products/h2o/)
- [Meltano](https://gitlab.com/meltano/meltano)
- [Firebolt](https://github.com/digitalocean/firebolt)
- [Pachyderm](https://github.com/pachyderm/pachyderm) and [Deploy on a Cloud via K8s](https://docs.pachyderm.com/latest/deploy-manage/deploy/amazon_web_services/)
- [PrefectCore](https://github.com/prefecthq/prefect) 
- [PipelineWise](https://github.com/transferwise/pipelinewise) 
- [Singer](https://www.singer.io/) 

## Lineage and Metadata Management
- [DataHub](https://github.com/linkedin/datahub)
- [OpenLineage](https://github.com/OpenLineage/OpenLineage)
- [Apache Atlas](https://atlas.apache.org/#/)
- [Marquez](https://github.com/MarquezProject/marquez)
- [Tokern](https://tokern.io/)

## Observability
- [Databand](https://github.com/databand-ai)

# Vendors 
- [Dot Science](https://dotscience.com)
- [Data Kitche](https://datakitchen.io)
- [Hydrosphere](https://hydrosphere.io/)
- [StreamSets](https://streamsets.com/) - see https://github.com/streamsets

# Cloud Offerings
- [Qwak](https://www.qwak.com/) 


## Google
- [Architecture for MLOps using TFX, Kubeflow Pipelines, and Cloud Build](https://cloud.google.com/solutions/machine-learning/architecture-for-mlops-using-tfx-kubeflow-pipelines-and-cloud-build)
- [Google ](https://cloud.google.com/dataflow/docs/guides/deploying-a-pipeline)

## Azure
- https://azure.microsoft.com/en-us/services/machine-learning/mlops/
- https://docs.microsoft.com/en-us/azure/machine-learning/concept-model-management-and-deployment
