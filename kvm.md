# Checking if VT

```
mfranz@mfranz-h30:~$ kvm-ok 
INFO: /dev/kvm exists
KVM acceleration can be used
```

# Install  uvtools
```apt install uvtool virt-manager```

See https://help.ubuntu.com/lts/serverguide/cloud-images-and-uvtool.html

# Sync VMs

```
uvt-simplestreams-libvirt --verbose sync release=xenial arch=amd64
uvt-simplestreams-libvirt --verbose sync release=bionic arch=amd64
```

# Creating VMs

```
mfranz@mfranz-e6230:~$ uvt-kvm create --memory 2048 first release=bionic
mfranz@mfranz-e6230:~$ uvt-kvm wait first
mfranz@mfranz-e6230:~$ uvt-kvm ssh first
Welcome to Ubuntu 18.04.4 LTS (GNU/Linux 4.15.0-112-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Thu Jul 30 16:16:22 UTC 2020

  System load:  0.17              Processes:             94
  Usage of /:   13.4% of 7.58GB   Users logged in:       0
  Memory usage: 6%                IP address for enp1s0: 192.168.122.95
  Swap usage:   0%


0 packages can be updated.
0 updates are security updates.


To run a command as administrator (user "root"), use "sudo <command>".
See "man sudo_root" for details.
```
