# References
- https://kubernetes.io/docs/reference/kubectl/cheatsheet/

# Namespaces

[a mechanism for isolating groups of resources within a single cluster](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) and most Kubernetes resources (e.g. pods, services, replication controllers, and others) are in some namespaces. However namespace resources are not themselves in a namespaces. Resource naming must be unique *within* but not *across* namespaces

```
# k3s kubectl get namespaces
NAME              STATUS   AGE
default           Active   51d
kube-system       Active   51d
kube-public       Active   51d
kube-node-lease   Active   51d
```

# Services
[An abstract way to expose an application running on a set of Pods as a network service, which defines a logical set of Pods and a policy by which to access them](https://kubernetes.io/docs/concepts/services-networking/service/)

```
$ kubectl get services --namespace kube-system
NAME             TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)                      AGE
kube-dns         ClusterIP      10.43.0.10      <none>          53/UDP,53/TCP,9153/TCP       51d
metrics-server   ClusterIP      10.43.141.215   <none>          443/TCP                      51d
traefik          LoadBalancer   10.43.132.75    192.168.3.171   80:32314/TCP,443:32762/TCP   51d
```
and

```
# kubectl get services -A
NAMESPACE     NAME             TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)                      AGE
default       kubernetes       ClusterIP      10.43.0.1       <none>          443/TCP                      51d
kube-system   kube-dns         ClusterIP      10.43.0.10      <none>          53/UDP,53/TCP,9153/TCP       51d
kube-system   metrics-server   ClusterIP      10.43.141.215   <none>          443/TCP                      51d
kube-system   traefik          LoadBalancer   10.43.132.75    192.168.3.171   80:32314/TCP,443:32762/TCP   51d
```

and for kind

```
$ kubectl get services -A
NAMESPACE     NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)                  AGE
default       kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP                  2m1s
kube-system   kube-dns     ClusterIP   10.96.0.10   <none>        53/UDP,53/TCP,9153/TCP   118s
```


# Pods
- [The smallest deployable unit consisting of one or more containers and each pod gets its own IP address](https://kubernetes.io/docs/concepts/workloads/pods/)

```
$ k3s kubectl get pods -A
NAMESPACE     NAME                                      READY   STATUS      RESTARTS       AGE
kube-system   helm-install-traefik-crd-dp2vv            0/1     Completed   1              51d
kube-system   helm-install-traefik-df9w6                0/1     Completed   2              51d
kube-system   local-path-provisioner-7b7dc8d6f5-xx97l   1/1     Running     1 (9m8s ago)   51d
kube-system   svclb-traefik-bed2ff7e-dpxx9              2/2     Running     2 (9m8s ago)   51d
kube-system   metrics-server-668d979685-dqlnj           1/1     Running     1 (9m8s ago)   51d
kube-system   coredns-b96499967-fwslh                   1/1     Running     1 (9m8s ago)   51d
kube-system   traefik-7cd4fcff68-k2rvq                  1/1     Running     1 (9m9s ago)   51d
```

and 


```
root@xps7100:/home/mfranz# kubectl get pods --namespace kube-system
NAME                                      READY   STATUS      RESTARTS       AGE
helm-install-traefik-crd-dp2vv            0/1     Completed   1              51d
helm-install-traefik-df9w6                0/1     Completed   2              51d
local-path-provisioner-7b7dc8d6f5-xx97l   1/1     Running     1 (7m3s ago)   51d
svclb-traefik-bed2ff7e-dpxx9              2/2     Running     2 (7m3s ago)   51d
metrics-server-668d979685-dqlnj           1/1     Running     1 (7m3s ago)   51d
coredns-b96499967-fwslh                   1/1     Running     1 (7m3s ago)   51d
traefik-7cd4fcff68-k2rvq                  1/1     Running     1 (7m4s ago)   51d
```

and for kind

```
kubectl get pods -A
NAMESPACE            NAME                                         READY   STATUS    RESTARTS   AGE
kube-system          coredns-6d4b75cb6d-7xlfs                     1/1     Running   0          3m24s
kube-system          coredns-6d4b75cb6d-drplw                     1/1     Running   0          3m24s
kube-system          etcd-kind-control-plane                      1/1     Running   0          3m36s
kube-system          kindnet-zrt54                                1/1     Running   0          3m25s
kube-system          kube-apiserver-kind-control-plane            1/1     Running   0          3m37s
kube-system          kube-controller-manager-kind-control-plane   1/1     Running   0          3m36s
kube-system          kube-proxy-wz7fr                             1/1     Running   0          3m25s
kube-system          kube-scheduler-kind-control-plane            1/1     Running   0          3m37s
local-path-storage   local-path-provisioner-9cd9bd544-wxslr       1/1     Running   0          3m24s

```

# Nodes
[Workloads consist of containers placed into pods that run on nodes](https://kubernetes.io/docs/concepts/architecture/nodes/) and nodes consist of components that consist of [kubelet, kube-proxy, and a container runtime](https://kubernetes.io/docs/concepts/overview/components/#node-components)

```
k3s kubectl get node
NAME      STATUS   ROLES                  AGE   VERSION
xps7100   Ready    control-plane,master   51d   v1.24.4+k3s1
```
