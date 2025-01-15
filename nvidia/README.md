# Python Tools

I've testing these with `uv`

- https://nvitop.readthedocs.io/en/latest/
- https://github.com/wookayin/gpustat

# Monitoring with Built in CLI Tools
- [nvidia-smi Cheat Sheet](https://www.seimaxim.com/kb/gpu/nvidia-smi-cheat-sheet)
- [Useful Nvidia SMI Queries](https://enterprise-support.nvidia.com/s/article/Useful-nvidia-smi-Queries-2)
- [Monitoring and Logging GPU Utilization in your job](https://www.docs.arc.vt.edu/usage/gpumon.html)

## Examples

```
nvidia-smi -l 1 --query-gpu=memory.used,memory.total --format=csv
```

# Prometheus
- https://github.com/utkuozdemir/nvidia_gpu_exporter

# Container Tools 
- https://hub.docker.com/r/nvidia/cuda
- [container toolkit](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installation) - latest Ubuntu is `22.04`
- [nvidia operator](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/getting-started.html#prerequisites) and see [time slicing](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-sharing.html#)

# Random GPU Infra Projects
## GPU over IP 
- https://github.com/Juice-Labs/Juice-Labs
- https://github.com/kevmo314/scuda
