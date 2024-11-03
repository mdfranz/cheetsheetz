# Kubernetes
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

Then annotate a service with
```
  annotations:
    tailscale.com/expose: "true"
```

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
