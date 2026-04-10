# Forgejo Binary Installation

Follow instruction at https://forgejo.org/docs/next/admin/installation/binary/ and 

```
[server]
SSH_DOMAIN = 192.168.2.6
DOMAIN = 192.168.2.6
HTTP_PORT = 3000
ROOT_URL = http://192.168.2.6:3000/
APP_DATA_PATH = /var/lib/forgejo/data
DISABLE_SSH = false
SSH_PORT = 2222
START_SSH_SERVER = true
LFS_START_SERVER = true
LFS_JWT_SECRET = [Redacted]
OFFLINE_MODE = true
```

`START_SSH_SERVER = true` had to be enabled and then you update `~/.ssh/config` with

```
Host 192.168.2.6
    User git
    Port 2222
```
