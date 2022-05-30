# Concepts

## Cluster

```
$ kubectl get componentstatuses
NAME                 AGE
etcd-1               <unknown>
controller-manager   <unknown>
scheduler            <unknown>
etcd-0               <unknown>
```

Default on k3s
```
ubuntu@k3s-xps7100:~$ k3ctl get componentstatuses
Warning: v1 ComponentStatus is deprecated in v1.19+
NAME                 STATUS    MESSAGE   ERROR
controller-manager   Healthy   ok        
scheduler            Healthy   ok   
```

### Nodes

VM or hardware that includes:
* kublet - agent that runs on each node 
* container runtime
* kube-proxy - maintains networking and firewall rules


https://kubernetes.io/docs/concepts/architecture/nodes/
https://github.com/kubernetes/community/blob/master/contributors/design-proposals/architecture/architecture.md#the-kubernetes-node

## Service

"In Kubernetes, a Service is an abstraction which defines a logical set of Pods and a policy by which to access them (sometimes this pattern is called a micro-service). The set of Pods targeted by a Service is usually determined by a selector (see below for why you might want a Service without a selector)."

See https://kubernetes.io/docs/concepts/services-networking/service/


## Pod

https://www.ianlewis.org/en/what-are-kubernetes-pods-anyway


```
$ kubectl get pods
NAME                            READY   STATUS    RESTARTS   AGE
hello-server-64db4d4dc7-x6vm6   1/1     Running   0          8m39s
```

## Service

https://kubernetes.io/docs/concepts/services-networking/service/

Kubernetes gives Pods their own IP addresses and a single DNS name for a set of Pods, and can load-balance across them.

```
kubectl get service hello-server
NAME           TYPE           CLUSTER-IP    EXTERNAL-IP    PORT(S)        AGE
hello-server   LoadBalancer   10.12.5.110   35.239.50.92   80:31350/TCP   8m38s
Oauth
```

# Bad things

- https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/

# Resources

## CPU

## Memory

## Ephemeral Storage

## Attachable Volumes


## CRD
- https://www.bmc.com/blogs/kubernetes-crd-custom-resource-definitions/
- https://itnext.io/crd-is-just-a-table-in-kubernetes-13e15367bbe4

# System Services (kube-system)

## Kube Proxy

## Fluentd

See https://cloud.google.com/solutions/customizing-stackdriver-logs-fluentd

The following containers

- fluentd-gcp-scaler
- fluentd-gcp - logging agent for StackDriver

## Metrics

metrics-server

## Heapter

heapster-*

## DNS

kube-dns-*
kube-dns-autoscaler -

https://unofficial-kubernetes.readthedocs.io/en/latest/tasks/administer-cluster/dns-horizontal-autoscaling/


Kubelet



# Networking

## CNI

GKE uses CNI (cbr0) by default

```
# brctl show cbr0
bridge name     bridge id               STP enabled     interfaces
cbr0            8000.da94d0f62ae3       no              veth1510bc2a
                                                        veth738fec85
                                                        veth97ca4f54
                                                        vethd0dbc708
```

https://github.com/containernetworking/cni
https://cloud.google.com/kubernetes-engine/docs/concepts/network-overview

## Public & Private

## Ports & Ingress

Port
Node Port
Target Port

# Packaging 

##  Helm
- https://github.com/helm/helm/releases
- https://helm.sh/docs/intro/quickstart/ 
- https://codefresh.io/docs/docs/new-helm/helm-best-practices/
- https://rafay.co/the-kubernetes-current/the-ultimate-guide-to-helm-charts/

## Operator Pattern

- https://codeburst.io/kubernetes-operators-by-example-99a77ea4ac43
- https://digitalis.io/blog/kubernetes/kubernetes-operators-pros-and-cons/
- https://www.bluematador.com/blog/using-helm-for-kubernetes-management-and-configuration
- https://cloudblogs.microsoft.com/opensource/2020/04/02/when-to-use-helm-operators-kubernetes-ops/
- https://www.openshift.com/blog/build-kubernetes-operators-from-helm-charts-in-5-steps
- https://medium.com/operators/operator-pattern-kubernetes-openshift-380ddc6a147c

# Lite Implementations

## Minikube
- https://fabianlee.org/2019/02/11/kubernetes-running-minikube-locally-on-ubuntu-using-kvm/
- https://medium.com/@nieldw/switching-from-minikube-with-virtualbox-to-kvm-2f742db704c9

## K3S

## Microk8s

## KIND

# Security Tools
- [pixie](https://github.com/pixie-io/pixie)
