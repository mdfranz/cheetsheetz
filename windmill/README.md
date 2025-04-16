# Articles
- [Long-running tasks done easy](https://invak.id/long-running-tasks)

# Important Features & Concepts
- [Self Host](https://www.windmill.dev/docs/advanced/self_host)
- [Caching](https://www.windmill.dev/docs/core_concepts/caching)
- [States](https://www.windmill.dev/docs/core_concepts/resources_and_types#states) - 
- [Webhooks](https://www.windmill.dev/docs/core_concepts/webhooks)
- [Preprocessors](https://www.windmill.dev/docs/core_concepts/preprocessors)
- [Data Pipelines](https://www.windmill.dev/docs/core_concepts/data_pipelines)
- [Workflows as Code](https://www.windmill.dev/docs/core_concepts/workflows_as_code)

## Python Specific
- [Private PyPi](https://www.windmill.dev/docs/advanced/dependencies_in_python#private-pypi-repository) - `EE` Only
- [Relative Imports](https://www.windmill.dev/docs/advanced/dependencies_in_python#sharing-common-logic-with-relative-imports) 

# CLI

You need Nodejs installed (deno is gone) via 

```
npm install -g windmill-cli
```

## Add Instance

```
mfranz@cros-acer516ge:~/windmill/rog$ wmill workspace add rog rog http://100.83.76.59:8000/
? How do you want to login › Browser
Login by going to http://100.83.76.59:8000/user/cli?port=25843
Opened browser for you
```

## Local Development Tips

See (recommended setup)[https://www.windmill.dev/docs/advanced/local_development#local-development-recommended-setup] which suggests using the following when using within CI/CD

```
wmill sync pull --skip-variables --skip-secrets --skip-resources
```
