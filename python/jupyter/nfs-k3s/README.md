
See https://ubuntu.com/server/docs/network-file-system-nfs

`/etc/exports` is

```
/var/nfs/csi       192.162.122.0/24(rw,async,no_subtree_check,no_root_squash)
```

And installed https://github.com/kubernetes-csi/csi-driver-nfs/ via helm (defaults) 

which installs these pods

```
$ kubectl get pods -A | grep nfs
kube-system       csi-nfs-controller-64fc56cd5d-wq2nq                 4/4     Running   0             69m
kube-system       csi-nfs-node-7fvj5                                  3/3     Running   0             69m
kube-system       csi-nfs-node-qvnv5                                  3/3     Running   0             69m
kube-system       csi-nfs-node-r4894                                  3/3     Running   0             69m
```

These are created

*StorageClass*
```
- apiVersion: storage.k8s.io/v1
  kind: StorageClass
  metadata:
    annotations:
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"storage.k8s.io/v1","kind":"StorageClass","metadata":{"annotations":{"storageclass.kubernetes.io/is-default-class":"false"},"name":"nfs-csi"},"parameters":{"server":"192.168.122.1","share":"/var/nfs/csi"},"provisioner":"nfs.c
si.k8s.io","reclaimPolicy":"Delete","volumeBindingMode":"Immediate"}
      storageclass.kubernetes.io/is-default-class: "false"
    creationTimestamp: "2025-01-12T19:19:07Z"
    name: nfs-csi
    resourceVersion: "147219"
    uid: c87f5d56-08d5-497e-8ab5-544507c2fb64
  parameters:
    server: 192.168.122.1
    share: /var/nfs/csi
  provisioner: nfs.csi.k8s.io
  reclaimPolicy: Delete
  volumeBindingMode: Immediate
kind: List
metadata:
  resourceVersion: ""
```

*PVC*
```
- apiVersion: v1
  kind: PersistentVolumeClaim
  metadata:
    annotations:
      kubectl.kubernetes.io/last-applied-configuration: |
        {"apiVersion":"v1","kind":"PersistentVolumeClaim","metadata":{"annotations":{},"name":"jupyterhub-shared-volume","namespace":"jlab"},"spec":{"accessModes":["ReadWriteMany"],"resources":{"requests":{"storage":"20Gi"}},"storageClassName":"nfs-csi"}}
      pv.kubernetes.io/bind-completed: "yes"
      pv.kubernetes.io/bound-by-controller: "yes"
      volume.beta.kubernetes.io/storage-provisioner: nfs.csi.k8s.io
      volume.kubernetes.io/storage-provisioner: nfs.csi.k8s.io
    creationTimestamp: "2025-01-12T19:20:32Z"
    finalizers:
    - kubernetes.io/pvc-protection
    name: jupyterhub-shared-volume
    namespace: jlab
    resourceVersion: "147395"
    uid: 2eee4110-3dc8-4ed3-b3c5-40581ec9319d
  spec:
    accessModes:
    - ReadWriteMany
    resources:
      requests:
        storage: 20Gi
    storageClassName: nfs-csi
    volumeMode: Filesystem
    volumeName: pvc-2eee4110-3dc8-4ed3-b3c5-40581ec9319d
  status:
    accessModes:
    - ReadWriteMany
    capacity:
      storage: 20Gi
    phase: Bound
kind: List
metadata:
  resourceVersion: ""
```

and

*PVC*

```
- apiVersion: v1
  kind: PersistentVolume
  metadata:
    annotations:
      pv.kubernetes.io/provisioned-by: nfs.csi.k8s.io
      volume.kubernetes.io/provisioner-deletion-secret-name: ""
      volume.kubernetes.io/provisioner-deletion-secret-namespace: ""
    creationTimestamp: "2025-01-12T19:20:32Z"
    finalizers:
    - external-provisioner.volume.kubernetes.io/finalizer
    - kubernetes.io/pv-protection
    name: pvc-2eee4110-3dc8-4ed3-b3c5-40581ec9319d
    resourceVersion: "147392"
    uid: 898d2b40-2ee7-4e9b-9e70-d43656417f5d
  spec:
    accessModes:
    - ReadWriteMany
    capacity:
      storage: 20Gi
    claimRef:
      apiVersion: v1
      kind: PersistentVolumeClaim
      name: jupyterhub-shared-volume
      namespace: jlab
      resourceVersion: "147387"
      uid: 2eee4110-3dc8-4ed3-b3c5-40581ec9319d
    csi:
      driver: nfs.csi.k8s.io
      volumeAttributes:
        csi.storage.k8s.io/pv/name: pvc-2eee4110-3dc8-4ed3-b3c5-40581ec9319d
        csi.storage.k8s.io/pvc/name: jupyterhub-shared-volume
        csi.storage.k8s.io/pvc/namespace: jlab
        server: 192.168.122.1
        share: /var/nfs/csi
        storage.kubernetes.io/csiProvisionerIdentity: 1736708954388-984-nfs.csi.k8s.io
        subdir: pvc-2eee4110-3dc8-4ed3-b3c5-40581ec9319d
      volumeHandle: 192.168.122.1#var/nfs/csi#pvc-2eee4110-3dc8-4ed3-b3c5-40581ec9319d##
    persistentVolumeReclaimPolicy: Delete
    storageClassName: nfs-csi
    volumeMode: Filesystem
  status:
    lastPhaseTransitionTime: "2025-01-12T19:20:32Z"
    phase: Bound
kind: List
metadata:
  resourceVersion: ""
```
