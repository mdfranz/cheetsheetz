# Remote Forwarding

I primarily use a ChromeBook with local VMs as my primary laptop so I had to do this to be able to port forward through the local container that gets an 100.115.92.x address.

Update `~/.jupyter/jupyter_notebook_config.py`

```
c.NotebookApp.allow_origin = '*'
c.NotebookApp.allow_remote_access = True
```
