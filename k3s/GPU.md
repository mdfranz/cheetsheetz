# OS Depedencies
Go with Ubuntu 22.04 and install drivers, will be something like

```
sudo apt install nvidia-driver-550-server
```

See (Rancher on Ubuntu)[https://docs.rke2.io/advanced#deploy-nvidia-operator] instructions 


(This avoids having to install in the container) 

# Install Container Toolkit
See https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html#installation to see the PPA 

```
sudo apt-get install -y nvidia-container-toolkit
```

# Confirm It was installed properly

Confirm [runtime class](https://kubernetes.io/docs/concepts/containers/runtime-class/)


```
kubectl get runtimeclass
NAME                  HANDLER               AGE
nvidia                nvidia                6m39s
nvidia-experimental   nvidia-experimental   6m39s
```


# Install Operator (Optional)

```
helm repo add nvidia https://helm.ngc.nvidia.com/nvidia \
    && helm repo update
```

I did not get this to work 

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
--set driver.enabled=false \
--set toolkit.enabled=false \ 
nvidia/gpu-operator
```
