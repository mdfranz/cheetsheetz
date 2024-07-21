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


# Usage Plugins
- [llm-ollama](https://github.com/taketwo/llm-ollama) - access local or remote Ollama servers, if you are doing something funky set `OLLAMA_HOST=http://127.0.0.1:11434`
- [llm-python](https://github.com/simonw/llm-python) - use llm within a REPL or script. See [documentation](https://llm.datasette.io/en/stable/python-api.html)
