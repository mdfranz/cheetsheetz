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


### Nodes

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