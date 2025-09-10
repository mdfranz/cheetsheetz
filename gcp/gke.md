# Cluster Modes
- [Modes of Operations](https://cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)
- [Autopilot](https://cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)


# IAM
- [Workload Identity Federation](https://cloud.google.com/kubernetes-engine/docs/concepts/workload-identity)
- [GKE security overview](https://cloud.google.com/kubernetes-engine/docs/concepts/security-overview)

# Concepts
- [GKE Network Models](https://cloud.google.com/kubernetes-engine/docs/concepts/gke-compare-network-models)

# Set up kubectl with GKE

Make sure you have a default zone setup with gcloud

```
gcloud config set compute/zone us-east4-a
```

# Create `KUBECONFIG`

```
See https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl

```
gcloud container clusters get-credentials CLUSTER_NAME \
    --region=COMPUTE_REGION
```
