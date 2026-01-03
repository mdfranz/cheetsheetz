# Installation

See [Downloads](https://openobserve.ai/downloads/) and pick the following

* Kubernetes
* Latest
* OSS
* Single Node

## Kubernetes customization

Modify the manifest to do the following to use Tailscale 

```
metadata:
  name: openobserve
  namespace: openobserve
  annotations:
    tailscale.com/expose: "true"
spec:
  selector:
    app: openobserve
  ports:
  - name: http
    port: 5080
    targetPort: 5080
---   
```

Set `ZO_ROOT_USER_EMAIL` and `ZO_ROOT_USER_PASSWORD`
