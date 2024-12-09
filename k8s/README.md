# Great Blogs
- [Raesene's Ramblings](https://raesene.github.io/)

# Sandbox
- [killercoda](https://killercoda.com/)
- [Play with K8S](https://labs.play-with-k8s.com/)

# Links Pages
- [ramitsurana github awesome-k8s](https://github.com/ramitsurana/awesome-kubernetes) and [HTML rendered](https://ramitsurana.gitbook.io/awesome-kubernetes/docs)

# Tutorials
- [Learn K8s Weekly](https://learnk8s.io/issues/) - and [blog](https://learnk8s.io/blog)
- [A Crash Course on Kubernetes](https://blog.gruntwork.io/a-crash-course-on-kubernetes-a96c3891ad82) - July 2022
- [Learning Kubernetes, the Easy Way](https://medium.com/towards-data-science/learn-kubernetes-the-easy-way-d1cfa460c013) - September 2022

# Templating  
## Jsonnet
- Streamlining Kubernetes Deployment With Jsonnet: [part 1](https://brian-candler.medium.com/streamlining-kubernetes-application-deployment-with-jsonnet-711e15e9c665) and [part2](https://brian-candler.medium.com/streamlining-kubernetes-application-deployment-with-jsonnet-part-2-46927b189953)
- [Automating deploys to Kubernetes using ArgoCD and jsonnet](https://www.bekk.christmas/post/2020/16/automating-deploys-to-kubernetes-using-argocd-and-jsonnet) - December 2020
- [Declarative Infrastructure with the Jsonnet Templating Language](https://www.databricks.com/blog/2017/06/26/declarative-infrastructure-jsonnet-templating-language.html) - June 2017
- [Using Jsonnet With Kubernetes](https://jsonnet.org/articles/kubernetes.html)

# Packaging & Deployment
- [The Power of Kustomize and Helm](https://brentgruber.com/posts/kustomize_and_helm/) - July 2023
- [Kustomize vs. Helm – How to Use & Comparison](https://spacelift.io/blog/kustomize-vs-helm) - June 2023 
- [When and How to Use Helm and Kustomize Together](https://trstringer.com/helm-kustomize/) - Mar 2023
- [Comparing Helm vs Kustomize](https://www.harness.io/blog/helm-vs-kustomize) - April 2021

## Helm
- https://github.com/helm/helm/releases
- https://github.com/cdwv/awesome-helm
- https://helm.sh/docs/intro/quickstart/ 
- https://codefresh.io/docs/docs/new-helm/helm-best-practices/
- https://rafay.co/the-kubernetes-current/the-ultimate-guide-to-helm-charts/
- [DevSpace Component Chart](https://www.devspace.sh/component-chart/docs/configuration/reference)

## Kustomize
- [Awesome Kustomize Overview](https://www.trackawesomelist.com/aabouzaid/awesome-kustomize/readme/)
- [Managing Kubernetes Manifest Complexity with Kustomize](https://code.tubitv.com/managing-kubernetes-manifest-complexity-with-kustomize-b172346a805a) - Feb 2023

## Operator Pattern
- https://codeburst.io/kubernetes-operators-by-example-99a77ea4ac43
- https://digitalis.io/blog/kubernetes/kubernetes-operators-pros-and-cons/
- https://www.bluematador.com/blog/using-helm-for-kubernetes-management-and-configuration
- https://cloudblogs.microsoft.com/opensource/2020/04/02/when-to-use-helm-operators-kubernetes-ops/
- https://www.openshift.com/blog/build-kubernetes-operators-from-helm-charts-in-5-steps
- https://medium.com/operators/operator-pattern-kubernetes-openshift-380ddc6a147c

# Observability & Visualization
- [caretta](https://github.com/groundcover-com/caretta) - Instant K8s service dependency map, right to your Grafana.
- [headlamp](https://headlamp.dev/)

# Security Distributions
- https://www.talos.dev/

# Lite Implementations

See [k3s](k3s/)

## Minikube
- https://fabianlee.org/2019/02/11/kubernetes-running-minikube-locally-on-ubuntu-using-kvm/
- https://medium.com/@nieldw/switching-from-minikube-with-virtualbox-to-kvm-2f742db704c9
minikube-jammy

### KVM
- https://minikube.sigs.k8s.io/docs/drivers/kvm2/

## Microk8s

## KIND

# Platforms and PaaS
- [acorn](https://acorn.io/)

# Tools
## Available in Homebrew 

```
eksctl kubectl awscli k9s aws-cdk
```


# Random Ingress
- [skipper](https://github.com/zalando/skipper) - an HTTP router and reverse proxy for service composition. It's designed to handle >300k HTTP route definitions with detailed lookup conditions, and flexible augmentation of the request flow with filters. It can be used out of the box or extended with custom lookup, filter logic and configuration sources.
