# Checking if VT

```
mfranz@mfranz-h30:~$ kvm-ok 
INFO: /dev/kvm exists
KVM acceleration can be used
```

# Install  uvtools
```apt install uvtool```

See https://help.ubuntu.com/lts/serverguide/cloud-images-and-uvtool.html


# Add your user to  libvirt group 

See https://help.ubuntu.com/community/KVM/Installation


# Sync VMs

```
uvt-simplestreams-libvirt --verbose sync release=focal arch=amd64
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

Or with a disk and bridge

```
uvt-kvm create --memory 4096 nats release=bionic --disk 40 --bridge br0
```

You won't be able to uvt-ssh into this and there will be no way to find the IP address



# Virsh

```
mfranz@mfranz-h30:~$ virsh dominfo gitlab
Id:             4
Name:           gitlab
UUID:           006bfa59-3abb-44cf-942d-48f80ed6365d
OS Type:        hvm
State:          running
CPU(s):         2
CPU time:       6424.5s
Max memory:     6291456 KiB
Used memory:    6291456 KiB
Persistent:     yes
Autostart:      disable
Managed save:   no
Security model: apparmor
Security DOI:   0
Security label: libvirt-006bfa59-3abb-44cf-942d-48f80ed6365d (enforcing)
```

Show domain config for editing

```
mfranz@mfranz-h30:~$ virsh dumpxml gitlab | egrep -i '(memory|cpu)'
  <memory unit='KiB'>6291456</memory>
  <currentMemory unit='KiB'>6291456</currentMemory>
  <vcpu placement='static'>2</vcpu>
```

## Ensuring it starts on boot

```
$ virsh autostart <domain>

```

## Changing Hardware

```
$ virsh edit <domain>
```

Settings that I've changed:
- memory
- vcpu
