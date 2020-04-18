# Remote Forwarding

I primarily use a ChromeBook with local VMs as my primary laptop so I had to do this to be able to port forward through the local container that gets an 100.115.92.x address.

Update `~/.jupyter/jupyter_notebook_config.py`

```
c.NotebookApp.allow_origin = '*'
c.NotebookApp.allow_remote_access = True
```

And then `ssh -L 0.0.0.0:8888:127.0.0.1:8888 mfranz@192.168.2.218`

This is insecure but within local ChromeBook so :thisisfine:

