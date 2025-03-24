This is an example of how to react to mounted file changes. Mounts are from a Secret, a ConfigMap and a DownwardAPI annotation.

Requirements: `docker`, `kind`, `kubectl`.

To reproduce this, first initialize the environment with resources and watch pod logs:
```
kind create cluster -n watcher
kubectl create -f configmap.yaml
kubectl create -f secret.yaml
docker build -t mount-watching-image .
kind load docker-image -n watcher mount-watching-image
kubectl create -f deployment.yaml
kubectl wait --for=condition=available deploy/mount-watching
kubectl logs -f $(kubectl get pod -l app=mount-watching -o jsonpath="{.items[0].metadata.name}")
```

To trigger changes you can use the following commands in a different terminal:
```
kubectl patch secret secret-resource -p "{\"data\":{\"data-from-secret\":\"$(echo -n "second" | base64)\"}}"
kubectl patch configmap configmap-resource -p '{"data":{"data-from-configmap":"second"}}'
kubectl annotate pod $(kubectl get pod -l app=mount-watching -o jsonpath="{.items[0].metadata.name}") --overwrite data-from-annotation=second
```

The results you can see in the `mount-watching-...` pod logs.

To clean up you can use:
```
kind delete clusters watcher
```

The logs should look something like this:
```
SECRET: Directory /etc/secret-folder:
total 4
drwxrwxrwt 3 root root  100 Mar 24 13:57 .
drwxr-xr-x 1 root root 4096 Mar 24 13:57 ..
drwxr-xr-x 2 root root   60 Mar 24 13:57 ..2025_03_24_13_57_59.3564152794
lrwxrwxrwx 1 root root   32 Mar 24 13:57 ..data -> ..2025_03_24_13_57_59.3564152794
lrwxrwxrwx 1 root root   23 Mar 24 13:57 data-from-secret -> ..data/data-from-secret
SECRET: File /etc/secret-folder/data-from-secret:
"
first
"
CONFIG-MAP: Directory /etc/configmap-folder:
total 12
drwxrwxrwx 3 root root 4096 Mar 24 13:57 .
drwxr-xr-x 1 root root 4096 Mar 24 13:57 ..
drwxr-xr-x 2 root root 4096 Mar 24 13:57 ..2025_03_24_13_57_59.4040030899
lrwxrwxrwx 1 root root   32 Mar 24 13:57 ..data -> ..2025_03_24_13_57_59.4040030899
lrwxrwxrwx 1 root root   26 Mar 24 13:57 data-from-configmap -> ..data/data-from-configmap
CONFIG-MAP: File /etc/configmap-folder/data-from-configmap:
"
first
"
ANNOTATIONS: Directory /etc/annotations:
total 4
drwxrwxrwt 3 root root  100 Mar 24 13:57 .
drwxr-xr-x 1 root root 4096 Mar 24 13:57 ..
drwxr-xr-x 2 root root   60 Mar 24 13:57 ..2025_03_24_13_57_59.701178428
lrwxrwxrwx 1 root root   31 Mar 24 13:57 ..data -> ..2025_03_24_13_57_59.701178428
lrwxrwxrwx 1 root root   23 Mar 24 13:57 annotations-file -> ..data/annotations-file
ANNOTATIONS: File /etc/annotations/annotations-file:
"
first
"
SECRET: event: CREATE        "/etc/secret-folder/..2025_03_24_13_59_21.3424772795"
CONFIG-MAP: event: CREATE        "/etc/configmap-folder/..2025_03_24_13_59_21.2513226119"
ANNOTATIONS: event: CREATE        "/etc/annotations/..2025_03_24_13_59_21.3539374523"
ANNOTATIONS: File /etc/annotations/annotations-file:
"
second
"
SECRET: File /etc/secret-folder/data-from-secret:
"
second
"
CONFIG-MAP: File /etc/configmap-folder/data-from-configmap:
"
second
"
SECRET: event: CHMOD         "/etc/secret-folder/..2025_03_24_13_59_21.3424772795"
CONFIG-MAP: event: CHMOD         "/etc/configmap-folder/..2025_03_24_13_59_21.2513226119"
ANNOTATIONS: event: CHMOD         "/etc/annotations/..2025_03_24_13_59_21.3539374523"
SECRET: event: CREATE        "/etc/secret-folder/..data_tmp"
CONFIG-MAP: event: CREATE        "/etc/configmap-folder/..data_tmp"
CONFIG-MAP: event: RENAME        "/etc/configmap-folder/..data_tmp"
ANNOTATIONS: event: CREATE        "/etc/annotations/..data_tmp"
SECRET: event: RENAME        "/etc/secret-folder/..data_tmp"
CONFIG-MAP: event: CREATE        "/etc/configmap-folder/..data" ← "/etc/configmap-folder/..data_tmp"
ANNOTATIONS: event: RENAME        "/etc/annotations/..data_tmp"
SECRET: event: CREATE        "/etc/secret-folder/..data" ← "/etc/secret-folder/..data_tmp"
SECRET: event: REMOVE        "/etc/secret-folder/..2025_03_24_13_57_59.3564152794"
ANNOTATIONS: event: CREATE        "/etc/annotations/..data" ← "/etc/annotations/..data_tmp"
ANNOTATIONS: event: REMOVE        "/etc/annotations/..2025_03_24_13_57_59.701178428"
CONFIG-MAP: event: REMOVE        "/etc/configmap-folder/..2025_03_24_13_57_59.4040030899"
```
