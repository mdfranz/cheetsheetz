# New IOS 26 Lightweight Container

- https://apple.github.io/container/documentation/
- https://github.com/apple/container

## Example

Run the contaner like this

```
% container run -d --rm -p 127.0.0.1:8080:8000 python:slim python3 -m http.server --bind 0.0.0.0 8000
```

View and exec

```
matthew@mfranz-mba15 mac % container ls
ID                                    IMAGE                          OS     ARCH   STATE    ADDR          CPUS  MEMORY
3cc8a945-b822-4e09-83db-ccc8066852a3  docker.io/library/python:slim  linux  arm64  running  192.168.64.6  4     1024 MB
matthew@mfranz-mba15 mac % 
matthew@mfranz-mba15 mac % container exec --interactive --tty 3cc8a945-b822-4e09-83db-ccc8066852a3 /bin/sh
# uname -a
Linux 3cc8a945-b822-4e09-83db-ccc8066852a3 6.12.28 #1 SMP Tue May 20 15:19:05 UTC 2025 aarch64 GNU/Linux
# 
```
