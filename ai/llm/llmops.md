# Overview
- [Awesome-LLMOps](https://github.com/tensorchord/Awesome-LLMOps/)
- [LLMOps (LLM Bootcamp)](https://www.youtube.com/watch?v=Fquj2u7ay40) - May '23
- [https://medium.com/@iamleonie/understanding-llmops-large-language-model-operations-4253820922](https://medium.com/@iamleonie/understanding-llmops-large-language-model-operations-4253820922)
- [Microsoft Open Sources LMOps: A New Research Initiative to Enable Applications Development with Foundation Models, Part I](https://medium.com/towards-artificial-intelligence/microsoft-open-sources-lmops-a-new-research-initiative-to-enable-applications-development-with-d6d7e7ca2059)
- [ML Engineer's Hell](https://github.com/stas00/ml-engineering/blob/master/insights/ai-battlefield.md#ml-engineers-hell) from [Machine Language Engineering Open Book](https://github.com/stas00/ml-engineering/tree/master)


## Performance
- [LLM Inference Performance Engineering: Best Practices](https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices) - Oct 2023

## AWS Services (mostly SageMaker)
- [How to deploy LLama 2 as an AWS Lambda function for scalable serverless inference](https://aws.plainenglish.io/guide-for-running-llama-2-using-llama-cpp-on-aws-fargate-7086bcd1ed3c) and [code](https://github.com/penkow/llama-lambda) - Oct 2023
- [Deploy Generative AI on EKS](https://aws.amazon.com/blogs/containers/deploy-generative-ai-models-on-amazon-eks/)
- [Amazon Bedrock](https://aws.amazon.com/bedrock/) and [Titan](https://aws.amazon.com/bedrock/titan/) and 
[Amazon SageMaker Notebook Instances](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html) and [Deep Learning Containers](https://docs.aws.amazon.com/deep-learning-containers/latest/devguide/what-is-dlc.html) with [gitlab](https://github.com/aws/deep-learning-containers)
- [Retrieval Augmented Generation](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-customize-rag.html) 
- [Deploy generative AI models from Amazon SageMaker JumpStart using the AWS CDK](https://github.com/aws-samples/generative-ai-sagemaker-cdk-demo)
- [Use Built-in Algorithms with Pre-trained Models in SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/overview.html#use-sagemaker-jumpstart-algorithms-with-pretrained-models) and https://github.com/aws/amazon-sagemaker-examples/
- [Use Machine Learning Frameworks, Python, and R with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/frameworks.html) 

Also see [SageMaker](../aws/sagemaker.md)

# Personal/Local LLMs

## Containerizing Open Source Models
Container or single file deployment of models seems like a solved problem with [ollama](https://ollama.com/)

### Blogs
[A Simple Guide to Run the LLama Model in a Docker Container](https://medium.com/@ahmedtm/a-simple-guide-to-run-the-llama-model-in-a-docker-container-a3899032995e) - Dec 2023

### Tools/Code 
- https://github.com/soulteary/llama-docker-playground
- https://github.com/getumbrel/llama-gpt
- https://github.com/bergos/llama-cpp-bundled
- https://github.com/Mozilla-Ocho/llamafile

## Self-Hosting (aka "Air Gapped" LLMs) 
- [privategpt](https://github.com/zylon-ai/private-gpt) - a production-ready AI project that allows you to ask questions about your documents using the power of Large Language Models (LLMs), even in scenarios without an Internet connection. 100% private, no data leaves your execution environment at any point.
- [h2ogpt](https://github.com/h2oai/h2ogpt) - Query and summarize your documents or just chat with local private GPT LLMs using h2oGPT, an Apache V2 open-source project.
- [LocalAI](https://github.com/mudler/LocalAI) - free, Open Source OpenAI alternative. LocalAI act as a drop-in replacement REST API that’s compatible with OpenAI API specifications for local inferencing. It allows you to run LLMs, generate images, audio (and not only) locally or on-prem with consumer grade hardware, supporting multiple model families. Does not require GPU.
- [Open Web UI](https://github.com/open-webui/open-webui)
- [OpenLLM](https://github.com/bentoml/OpenLLM)
- [ollama](https://github.com/ollama/ollama)
- [Skypilot](https://github.com/skypilot-org/skypilot) - SkyPilot: Run LLMs, AI, and Batch jobs on any cloud. Get maximum savings, highest GPU availability, and managed execution—all with a simple interface.
- 

### Streamlit Local Hosting
- https://github.com/3eeps/llmon-py

# Full Stack Frameworks (Non-SaaS)
These may or may not be commerical 

- [Metaflow](https://github.com/Netflix/metaflow) 
- [BentoML](https://github.com/bentoml/BentoML) - a framework for building reliable, scalable, and cost-efficient AI applications. It comes with everything you need for model serving, application packaging, and production deployment.
- [dstack](https://github.com/dstackai/dstack) - engine for running GPU workloads on any cloud. It works with a wide range of cloud GPU providers (AWS, GCP, Azure, Lambda, TensorDock, Vast.ai, etc.) as well as on-premises servers.
- [pezzo](https://github.com/pezzolabs/pezzo) and [docs](https://docs.pezzo.ai/introduction/what-is-pezzo) - a powerful open-source toolkit designed to streamline the process of AI development. It empowers developers and teams to leverage the full potential of AI models in their applications with ease

## Gateways & Routers
 - [glide](https://github.com/EinStack/glide) - The Cloud Native LLM Gateway

# SaaS Vendor Solutions
- [Arthur](https://www.arthur.ai/) 
- [BentoML](https://www.bentoml.com/cloud) 
- [MindsDB](https://mindsdb.com/) - "the platform for customizing AI from enterprise data, enabling smarter organizations." see [What is MindsDB](https://docs.mindsdb.com/what-is-mindsdb) and https://github.com/mindsdb/mindsdb
- [truefoundry](https://www.truefoundry.com/llmops) and [Intro to LLMOps](https://docs.truefoundry.com/docs/introduction-1) and [github](https://github.com/truefoundry)


# Misc Tools

## Agent Deployment
- [swarms](https://github.com/kyegomez/swarms) - "Swarms "provides you with all the building blocks you need to build reliable, production-grade, and scalable multi-agent apps!"
