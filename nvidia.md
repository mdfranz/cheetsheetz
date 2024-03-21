# Monitoring with CLI Tools
- [nvidia-smi Cheat Sheet](https://www.seimaxim.com/kb/gpu/nvidia-smi-cheat-sheet)
- [Useful Nvidia SMI Queries](https://enterprise-support.nvidia.com/s/article/Useful-nvidia-smi-Queries-2)
- [Monitoring and Logging GPU Utilization in your job](https://www.docs.arc.vt.edu/usage/gpumon.html)

## Examples

```
nvidia-smi -l 1 --query-gpu=memory.used,memory.total --format=csv
```

# Prometheus
- https://github.com/utkuozdemir/nvidia_gpu_exporter
