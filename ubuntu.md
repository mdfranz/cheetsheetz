This is the basic setup I use on bare-metal Ubuntu Servers (amd64 or aarch64)

Also see [kvm](kvm.md) 

# Monitoring
- [Vector](https://vector.dev/releases/0.11.1/download/) - for log forwarding to remote systems or AWS
- [Telegraf](https://github.com/influxdata/telegraf/releases) - for metrics to be forwarded to [InfluxDB](https://www.influxdata.com/get-influxdb/) and then so metrics can be viewed with [Grafana](https://grafana.com/grafana/download)

# Raspberry Pi Disk Setup

For RPI (or Jetson) that I use non-trivially I put the /var and /home partition on an external USB drive

This is so whatever you are doing in your home directory or /var (for docker or LXC or whatever) doesn't hit the SD-Card. Reminder `blkid` allows you to see the LABELs. 

I usually stop `snapd` and `lxd` services  prior to rsyncing over

```
LABEL=writable	/	 ext4	defaults	0 0
LABEL=system-boot       /boot/firmware  vfat    defaults        0       1
UUID="79038852-3311-490f-a4bc-85e548deb5d0" /home ext4  defaults        0 0
UUID="685a37b9-5405-4397-8539-9e005db9bcd4" /var ext4  defaults        0 0
```

# Setup a Bridge for Wired for VMs or Containers

Something like this. On Ubuntu desktop NetworkManager is used by default

```
$ sudo cat /etc/netplan/bridged.yaml 
[sudo] password for mdfranz: 
network:
  ethernets:
    eno1:
      dhcp4: false
  version: 2

  bridges:
    br0:
      interfaces: [eno1]
      dhcp4: true

```

# Enable Screen Blank

Add the following to `/etc/default/grub`

```
GRUB_CMDLINE_LINUX_DEFAULT="consoleblank=450"
```

And confirm with

```
# cat /sys/module/kernel/parameters/consoleblank
450
```

# LXD Setup 

See [Rocky Linux LXD Beginners guide](https://docs.rockylinux.org/guides/containers/lxd_web_servers/) and [Ubuntu Wiki](https://ubuntu.com/server/docs/containers-lxd) page 

This is the most simple setup for non-bridged LXD

```
$ sudo lxd init
Would you like to use LXD clustering? (yes/no) [default=no]: 
Do you want to configure a new storage pool? (yes/no) [default=yes]: 
Name of the new storage pool [default=default]: 
Name of the storage backend to use (ceph, btrfs, dir, lvm, zfs) [default=zfs]: dir
Would you like to connect to a MAAS server? (yes/no) [default=no]: 
Would you like to create a new local network bridge? (yes/no) [default=yes]: 
What should the new bridge be called? [default=lxdbr0]: 
What IPv4 address should be used? (CIDR subnet notation, “auto” or “none”) [default=auto]: 
What IPv6 address should be used? (CIDR subnet notation, “auto” or “none”) [default=auto]: none
Would you like the LXD server to be available over the network? (yes/no) [default=no]: no
Would you like stale cached images to be updated automatically? (yes/no) [default=yes] 
Would you like a YAML "lxd init" preseed to be printed? (yes/no) [default=no]: no
```

## Using Non Ubuntu Images

```
mfranz@notakia:~$ lxc image list images: | grep amazon
| amazonlinux/2 (3 more)                   | 8b7940ce7f91 | yes    | Amazonlinux 2 amd64 (20231219_05:09)       | x86_64       | CONTAINER       | 63.27MiB   | Dec 19, 2023 at 12:00am (UTC) |
| amazonlinux/2/arm64 (1 more)             | 16ff9c2c08d6 | yes    | Amazonlinux 2 arm64 (20231219_05:09)       | aarch64      | CONTAINER       | 62.92MiB   | Dec 19, 2023 at 12:00am (UTC) |
| amazonlinux/2023 (3 more)                | c1ab4fd6dc12 | yes    | Amazonlinux 2023 amd64 (20231219_05:09)    | x86_64       | CONTAINER       | 63.07MiB   | Dec 19, 2023 at 12:00am (UTC) |

```

Disable [CGroupv2](https://chrisdown.name/talks/cgroupv2/cgroupv2-fosdem.pdf) with the following command to get AWS Linux to work and run `update-grub` and reboot


```
GRUB_CMDLINE_LINUX="systemd.unified_cgroup_hierarchy=0"
```

And create container with 

```
$ lxc launch images:amazonlinux/2
```	

# Citrix

Download [Workspaces](https://www.citrix.com/downloads/workspace-app/linux/workspace-app-for-linux-latest.html)

Do not install app protection component

```
 sudo dpkg -i icaclient_21.6.0.28_amd64.deb 
[sudo] password for mfranz: 
Selecting previously unselected package icaclient.
(Reading database ... 218596 files and directories currently installed.)
Preparing to unpack icaclient_21.6.0.28_amd64.deb ...
Unpacking icaclient (21.6.0.28) ...
Setting up icaclient (21.6.0.28) ...
^[[1;3B/usr/bin/sudo
Synchronizing state of ctxlogd.service with SysV service script with /lib/systemd/systemd-sysv-install.
Executing: /lib/systemd/systemd-sysv-install enable ctxlogd
Created symlink /etc/systemd/system/multi-user.target.wants/ctxlogd.service → /lib/systemd/system/ctxlogd.service.
Processing triggers for systemd (245.4-4ubuntu3.11) ...
Processing triggers for gnome-menus (3.36.0-1ubuntu1) ...
Processing triggers for desktop-file-utils (0.24-1ubuntu3) ...
Processing triggers for mime-support (3.64ubuntu1) ...
```

Login to your foo.blah.com domain in Firefox

Select detect receiver

You will receive multiple errors, but ultimately you'll need to do

```
sudo ln -s /usr/share/ca-certificates/mozilla/* /opt/Citrix/ICAClient/keystore/cacerts
```

# X on Ubuntu Server

```
# apt install gnome-terminal xinit openbox gnome-tweaks
# snap install firefox
```

Install wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb and 

```
# apt --fix-broken install
```

# Extending a Volume Group that was too small during the install

```
# vextend -l +100%FREE -r /dev/ubuntu-vg/ubuntu-lv
```

From https://4sysops.com/archives/extending-lvm-space-in-ubuntu/


