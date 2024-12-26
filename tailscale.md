# Kubernetes Operator
- [Kubernetes operator](https://tailscale.com/kb/1236/kubernetes-operator)

Add this

```
	// Define the tags which can be applied to devices and by which users.
	// "tagOwners": {
	//  	"tag:example": ["autogroup:admin"],
	// },

	"tagOwners": {
		"tag:k8s-operator": [],
		"tag:k8s":          ["tag:k8s-operator"],
	},
```

Generate key, then

```
helm upgrade \
  --install \
  tailscale-operator \
  tailscale/tailscale-operator \
  --namespace=tailscale \
  --create-namespace \
  --set-string oauth.clientId="<OAauth client ID>" \
  --set-string oauth.clientSecret="<OAuth client secret>" \
  --wait
```

## Exposing an internal service to your tailnet

Then annotate a service with
```
  annotations:
    tailscale.com/expose: "true"
```

Or from the command line

```
kubectl annotate service -n ollama ollama tailscale.com/expose="true"
```


## Exposing an External tailnet host to your cluster as a Service

See (cluster egress}[https://tailscale.com/kb/1438/kubernetes-operator-cluster-egress] documentation 

Create a service in your cluster (this example uses IP)

```
apiVersion: v1
kind: Service
metadata:
  annotations:
    tailscale.com/tailnet-ip: 100.108.187.89
  name: clickhouse-pn50   
spec:
  externalName: placeholder
  type: ExternalName
```

It will then create the following service

```
mfranz@asus-rogstrix:~/tailscale$ kubectl get svc | grep click
clickhouse-pn50   ExternalName   <none>       ts-clickhouse-pn50-2kk6c.tailscale.svc.cluster.local   <none>    9m34s
```
Which you can refer to on any jobs 










# Headscale
- https://github.com/juanfont/headscale
- [Has anyone used Headscale?](https://www.reddit.com/r/selfhosted/comments/13et1uu/has_anyone_used_headscale/) - 

## Managmennt
- https://github.com/gurucomputing/headscale-ui
- https://github.com/spotsnel/cockpit-headscale
- https://github.com/hichamelkaddioui/headview

## IAC
- https://github.com/brucellino/terraform-module-digitalocean-headscale

## Containerized
- https://github.com/sonroyaalmerol/docker-headscale
- https://github.com/azaurus1/headscale-operator
