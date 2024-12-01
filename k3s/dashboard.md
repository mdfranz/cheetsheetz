# Docs
- https://gist.github.com/jannegpriv/06427e4ecc2a17f317a4bebc32b6445c
- https://kubernetes.io/docs/tasks/access-application-cluster/web-ui-dashboard/

# Steps

```
helm upgrade --install kubernetes-dashboard kubernetes-dashboard/kubernetes-dashboard --create-namespace --namespace kubernetes-dashboard
```

Expose `kubernetes-dashboard-kong-proxy` with Tailscale

```
$ kubectl get svc -n kubernetes-dashboard
NAME                                   TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE
kubernetes-dashboard-api               ClusterIP   10.43.53.47    <none>        8000/TCP   70m
kubernetes-dashboard-auth              ClusterIP   10.43.192.9    <none>        8000/TCP   70m
kubernetes-dashboard-kong-proxy        ClusterIP   10.43.225.87   <none>        443/TCP    70m
kubernetes-dashboard-metrics-scraper   ClusterIP   10.43.64.206   <none>        8000/TCP   70m
kubernetes-dashboard-web               ClusterIP   10.43.31.95    <none>        8000/TCP   70m

```

Will look like

```
$ kubectl describe svc kubernetes-dashboard-kong-proxy -n kubernetes-dashboard
Name:              kubernetes-dashboard-kong-proxy
Namespace:         kubernetes-dashboard
Labels:            app.kubernetes.io/instance=kubernetes-dashboard
                   app.kubernetes.io/managed-by=Helm
                   app.kubernetes.io/name=kong
                   app.kubernetes.io/version=3.6
                   enable-metrics=true
                   helm.sh/chart=kong-2.38.0
Annotations:       meta.helm.sh/release-name: kubernetes-dashboard
                   meta.helm.sh/release-namespace: kubernetes-dashboard
                   tailscale.com/expose: true
Selector:          app.kubernetes.io/component=app,app.kubernetes.io/instance=kubernetes-dashboard,app.kubernetes.io/name=kong
Type:              ClusterIP
IP Family Policy:  SingleStack
IP Families:       IPv4
IP:                10.43.225.87
IPs:               10.43.225.87
Port:              kong-proxy-tls  443/TCP
TargetPort:        8443/TCP
Endpoints:         10.42.2.11:8443
Session Affinity:  None
Events:            <none>
```

Create `service-account.yaml`

```
apiVersion: v1
kind: ServiceAccount
metadata:
  name: admin-user
  namespace: kubernetes-dashboard
```

Create `cluster-role-binding.yaml`

```
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: admin-user
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: admin-user
  namespace: kubernetes-dashboard
```

kubectl -n kubernetes-dashboard create token admin-user


