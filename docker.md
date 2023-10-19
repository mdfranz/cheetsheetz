# The Tech
- [Build Your Own Docker with Linux Namespaces, cgroups, and chroot: Hands-on Guide](https://akashrajpurohit.com/blog/build-your-own-docker-with-linux-namespaces-cgroups-and-chroot-handson-guide/) - Jun '23


# Up front
Highly encourage using SSD for /var on Ubuntu 20.04, which is what I'm using 

# Installation 
- https://docs.docker.com/engine/install/ubuntu/
- https://docs.docker.com/engine/install/debian/#install-using-the-convenience-script - for Raspian

# Docker-Compose

## Logging

start detached

```
$ docker-compose up -d
```

and follow logs

```
$ docker-compose logs -f 
```

