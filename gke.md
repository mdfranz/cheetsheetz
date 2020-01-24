
# Set up kubectl with GKE

Make sure you have a default zone setup with gcloud

```
$ gcloud config set compute/zone us-east4-a
```

```
$ gcloud container clusters create presea
WARNING: Currently VPC-native is not the default mode during cluster creation. In the future, this will become the default mode and can be disabled using `--no-enable-ip-alias` flag. Use `--[no-]enable-ip-alias` flag to suppress this warning.
WARNING: Newly created clusters and node-pools will have node auto-upgrade enabled by default. This can be disabled using the `--no-enable-autoupgrade` flag.
WARNING: Starting in 1.12, default node pools in new clusters will have their legacy Compute Engine instance metadata endpoints disabled by default.
To create a cluster with legacy instance metadata endpoints disabled in the default node pool, run `clusters create` with the flag `--metadata disable-legacy-endpoints=true`.
WARNING: Your Pod address range (`--cluster-ipv4-cidr`) can accommodate at most 1008 node(s).
This will enable the autorepair feature for nodes. Please see https://cloud.google.com/kubernetes-engine/docs/node-auto-repair for more information on node autorepairs.
Creating cluster presea in us-east4-a... Cluster is being health-checked (master is healthy)...done.
Created [https://container.googleapis.com/v1/projects/gce-comp/zones/us-east4-a/clusters/presea].
To inspect the contents of your cluster, go to: https://console.cloud.google.com/kubernetes/workload_/gcloud/us-east4-a/presea?project=gce-comp
kubeconfig entry generated for presea.
NAME    LOCATION    MASTER_VERSION  MASTER_IP       MACHINE_TYPE   NODE_VERSION    NUM_NODES  STATUS
presea  us-east4-a  1.13.11-gke.14  35.XXX.XXX.XXX  n1-standard-1  1.13.11-gke.14  3          RUNNING
```

# References

- https://cloud.google.com/kubernetes-engine/docs/quickstart
