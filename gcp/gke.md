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
