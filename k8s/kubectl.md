# Pods

```
kubectl get pods -A -o go-template='{{range .items}}{{.metadata.name}},{{.status.podIP}}{{"\n"}}{{end}}' 
```

# Services

```
kubectl get services -A -o go-template='{{range .items}}{{.metadata.name}},{{.spec.clusterIP}}{{"\n"}}{{end}}'
```  
