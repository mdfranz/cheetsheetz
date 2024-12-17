# OS Depedencies
- Go with Ubuntu 22.04

# Install Container Toolkit

See https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installation

# Install Operator
```
helm repo add nvidia https://helm.ngc.nvidia.com/nvidia \
    && helm repo update
```

```
helm install --wait nvidiagpu -n gpu-operator --create-namespace \
--set toolkit.env[0].name=CONTAINERD_CONFIG \
--set toolkit.env[0].value=/var/lib/rancher/k3s/agent/etc/containerd/config.toml \
--set toolkit.env[1].name=CONTAINERD_SOCKET \
--set toolkit.env[1].value=/run/k3s/containerd/containerd.sock \
--set toolkit.env[2].name=CONTAINERD_RUNTIME_CLASS \
--set toolkit.env[2].value=nvidia \
--set toolkit.env[3].name=CONTAINERD_SET_AS_DEFAULT \
--set-string toolkit.env[3].value=true \
--set toolkit.enabled=false \
nvidia/gpu-operator
```
