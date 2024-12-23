# LGTM Deployment

## Intro 
- https://github.com/grafana/intro-to-mltp

## Docker 
- https://grafana.com/docs/grafana/latest/setup-grafana/installation/docker/

## K8s Deployment
- [Kubernetes Logging with Grafana Loki & Promtail in under 10 minutes](https://akyriako.medium.com/kubernetes-logging-with-grafana-loki-promtail-in-under-10-minutes-d2847d526f9e) - Feb 2023
- [Official Helm Charts](https://grafana.com/docs/helm-charts/) 
- [Install Grafana Loki with Helm](https://grafana.com/docs/loki/latest/setup/install/helm/)  and [Install the simple scalable Helm chart](https://grafana.com/docs/loki/latest/setup/install/helm/install-scalable/) 

### K8S Rigs

- [LGTM-Poc](https://github.com/agalue/LGTM-PoC) by [agalue](https://github.com/agalue)
- [grafana-lgtm-on-k8s](https://github.com/sylnsr/grafana-lgtm-on-k8s) by [sylnsr](https://github.com/sylnsr)

### K3S
- https://rpi4cluster.com/monitoring/k3s-grafana/
- [Lightweight Kubernetes k3s on local machine with Grafana/Docker](https://kondlawork.medium.com/lightweight-kubernetes-k3s-on-local-machine-with-grafana-docker-5f5f8b514dfa) - July 2023

# Alloy
- [Collect Kubernetes logs and forward them to Loki](https://grafana.com/docs/alloy/latest/collect/logs-in-kubernetes/)


# Loki
It now accepts [out of order writes](https://grafana.com/docs/loki/latest/configure/#accept-out-of-order-writes) and uses [single store](https://grafana.com/docs/loki/latest/storage/#single-store) for both index and data with [TSDB](https://grafana.com/docs/loki/latest/operations/storage/tsdb/) as the default Index starting in [2.8](https://grafana.com/docs/loki/latest/release-notes/v2-8/)

See [architecture](https://grafana.com/docs/loki/latest/get-started/architecture/) and [deployment modes](https://grafana.com/docs/loki/latest/get-started/deployment-modes/#simple-scalable)  and [components](https://grafana.com/docs/loki/latest/get-started/components/)

[Labels](https://grafana.com/docs/loki/latest/get-started/labels/bp-labels/) (see [concise guide](https://grafana.com/blog/2020/08/27/the-concise-guide-to-labels-in-loki/)) can be added via [Promtail](https://grafana.com/docs/loki/latest/send-data/promtail/) and includes [pipelines](https://grafana.com/docs/loki/latest/send-data/promtail/pipelines/) that can [parse, transform, and filter](https://grafana.com/docs/loki/latest/send-data/promtail/stages/#prometheus-pipeline-stages)

[LogQL Filter Expressions](https://grafana.com/docs/loki/latest/query/#filter-expression) are used to search and alert. 

# Other Tooling
- https://github.com/grafana/grafonnet (based on (jsonnet)[https://jsonnet.org]

