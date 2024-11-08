# Installation 
Assuming you have [uv](https://docs.astral.sh/uv/) installed. 

```
uv  tool install llm
```

# Overview
Notes and tricks for [python-llm](https://llm.datasette.io/en/stable/)

- [cli reference](https://llm.datasette.io/en/stable/help.html)

## System Prompts

[System Prompts](https://llm.datasette.io/en/stable/usage.html#system-prompts) are the best way to pass 

```
curl -s https://raw.githubusercontent.com/longhorn/longhorn/master/deploy/longhorn.yaml | llm -m 4o-mini -s "Explain what these Kubernetes Resources do in less that 25 lines"
This YAML defines various Kubernetes resources primarily for managing Longhorn, a cloud-native distributed block storage solution.

1. **Namespace**: Creates a dedicated namespace (`longhorn-system`) for Longhorn's resources, isolating them from other workloads.

2. **PriorityClass**: Assigns a critical priority to Longhorn pods, ensuring they are less likely to be evicted during resource contention on nodes.
...

Overall, these resources together establish a coherent architecture for deploying, managing, and operating Longhorn in a Kubernetes environment, emphasizing high availability, security, and integration with Kubernetes' native features.
```

## Logging

See [logging](https://llm.datasette.io/en/stable/logging.html)

`llm logs list -n 0 --json`

### Analyzing with SQL 
Find the SQLite DB 

```
mfranz@rogstrix-b450-ryzen5:~/.local$ llm logs path
/home/mfranz/.config/io.datasette.llm/logs.db
```

## Plugins
- [llm-ollama](https://github.com/taketwo/llm-ollama) - access local or remote Ollama servers, if you are doing something funky set `OLLAMA_HOST`
- [llm-gemini](https://pypi.org/project/llm-gemini/)
- [llm-bedrock-anthropic](https://github.com/sblakey/llm-bedrock-anthropic)
