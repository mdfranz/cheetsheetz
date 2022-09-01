# References
- https://kubernetes.io/docs/reference/kubectl/cheatsheet/


# Namespaces


```
# k3s kubectl get namespaces
NAME              STATUS   AGE
default           Active   51d
kube-system       Active   51d
kube-public       Active   51d
kube-node-lease   Active   51d
```



# Services

```
$ kubectl get services --namespace kube-system
NAME             TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)                      AGE
kube-dns         ClusterIP      10.43.0.10      <none>          53/UDP,53/TCP,9153/TCP       51d
metrics-server   ClusterIP      10.43.141.215   <none>          443/TCP                      51d
traefik          LoadBalancer   10.43.132.75    192.168.3.171   80:32314/TCP,443:32762/TCP   51d
```


```
# kubectl get services -A
NAMESPACE     NAME             TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)                      AGE
default       kubernetes       ClusterIP      10.43.0.1       <none>          443/TCP                      51d
kube-system   kube-dns         ClusterIP      10.43.0.10      <none>          53/UDP,53/TCP,9153/TCP       51d
kube-system   metrics-server   ClusterIP      10.43.141.215   <none>          443/TCP                      51d
kube-system   traefik          LoadBalancer   10.43.132.75    192.168.3.171   80:32314/TCP,443:32762/TCP   51d
```


# Pods

- [smallest deployable unit consisting of one or more containers](https://kubernetes.io/docs/concepts/workloads/pods/)

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

# Nodes

```
k3s kubectl get node
NAME      STATUS   ROLES                  AGE   VERSION
xps7100   Ready    control-plane,master   51d   v1.24.4+k3s1
```
