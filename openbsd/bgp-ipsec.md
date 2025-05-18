# Common Configuration

Update `/etc/sysctl.conf` to the following

```
net.inet.ip.forwarding=1
net.inet.esp.enable=1
net.inet.ah.enable=1
```

Create `/etc/rc.conf.local`

```
bgpd_flags=""
bgpd_enable=YES
iked_flags=""
iked_enable="YES"
```

Ensure `/etc/bgpd.conf` and `/etc/iked.conf` are `0400`

Create loopback interfaces on the `192.168.0.0/16` network such address with `ifconfig create lo1` and assign an RFC 1918 address.

# Router 1 (194.182.183.35/192.168.1.1)

## Interfaces

```
VM-1d675609-e495-447b-b08d-81c3d854be3a# ifconfig -a
lo0: flags=2008049<UP,LOOPBACK,RUNNING,MULTICAST,LRO> mtu 32768
        index 3 priority 0 llprio 3
        groups: lo
        inet6 ::1 prefixlen 128
        inet6 fe80::1%lo0 prefixlen 64 scopeid 0x3
        inet 127.0.0.1 netmask 0xff000000
vio0: flags=2e08b43<UP,BROADCAST,RUNNING,PROMISC,ALLMULTI,SIMPLEX,MULTICAST,AUTOCONF6,INET6_NOSOII,AUTOCONF4,LRO> mtu 1500
        lladdr 06:6d:d4:00:02:f1
        index 1 priority 0 llprio 3
        groups: egress
        media: Ethernet autoselect
        status: active
        inet6 fe80::46d:d4ff:fe00:2f1%vio0 prefixlen 64 scopeid 0x1
        inet 194.182.183.35 netmask 0xfffffc00 broadcast 194.182.183.255
enc0: flags=141<UP,RUNNING,PROMISC>
        index 2 priority 0 llprio 3
        groups: enc
        status: active
pflog0: flags=141<UP,RUNNING,PROMISC> mtu 33136
        index 4 priority 0 llprio 3
        groups: pflog
lo1: flags=2008049<UP,LOOPBACK,RUNNING,MULTICAST,LRO> mtu 32768
        index 5 priority 0 llprio 3
        groups: lo
        inet 192.168.1.1 netmask 0xffffff00
```


## BGP Configuration

Create `/etc/bgpd.conf`

```
AS 64521
router-id 192.168.1.1
listen on 192.168.1.1

network 192.168.1.0/24

neighbor 192.168.2.1 {
        remote-as 64522
        descr "upstream2"
        local-address 192.168.1.1
}

allow from any inet prefixlen 8 - 24
deny from any prefix 0.0.0.0/0
deny from any prefix 169.254.0.0/16 prefixlen >= 16
deny from any prefix 224.0.0.0/4 prefixlen >= 4
allow to any

log updates
```

Create `/etc/iked.conf`

```
ikev2 "bsd1_bsd2" active esp \
        from 192.168.1.0/24 to 192.168.2.0/24 \
        local 194.182.183.35 peer 194.182.177.6 \
        psk "XXXX"
```

# Router 2 (194.182.177.6/192.168.2.1)
## Interfaces

```
lo0: flags=2008049<UP,LOOPBACK,RUNNING,MULTICAST,LRO> mtu 32768
        index 3 priority 0 llprio 3
        groups: lo
        inet6 ::1 prefixlen 128
        inet6 fe80::1%lo0 prefixlen 64 scopeid 0x3
        inet 127.0.0.1 netmask 0xff000000
vio0: flags=2e08843<UP,BROADCAST,RUNNING,SIMPLEX,MULTICAST,AUTOCONF6,INET6_NOSOII,AUTOCONF4,LRO> mtu 1500
        lladdr 06:aa:36:00:00:d4
        index 1 priority 0 llprio 3
        groups: egress
        media: Ethernet autoselect
        status: active
        inet6 fe80::4aa:36ff:fe00:d4%vio0 prefixlen 64 scopeid 0x1
        inet 194.182.177.6 netmask 0xfffffc00 broadcast 194.182.179.255
enc0: flags=141<UP,RUNNING,PROMISC>
        index 2 priority 0 llprio 3
        groups: enc
        status: active
pflog0: flags=141<UP,RUNNING,PROMISC> mtu 33136
        index 4 priority 0 llprio 3
        groups: pflog
lo1: flags=2008149<UP,LOOPBACK,RUNNING,PROMISC,MULTICAST,LRO> mtu 32768
        index 5 priority 0 llprio 3
        groups: lo
        inet 192.168.2.1 netmask 0xffffff00
```

## BGP
```
AS 64522
router-id 192.168.2.1
listen on 192.168.2.1

network 192.168.2.0/24

neighbor 192.168.1.1 {
        remote-as 64521
        descr "upstream1"
        local-address 192.168.2.1
}

allow from any inet prefixlen 8 - 24
deny from any prefix 0.0.0.0/0
deny from any prefix 169.254.0.0/16 prefixlen >= 16
deny from any prefix 224.0.0.0/4 prefixlen >= 4
allow to any

log updates
```


## IKED

```
ikev2 "bsd1_bsd2" active esp \
        from 192.168.2.0/24 to 192.168.1.0/24 \
        local 194.182.177.6 peer 194.182.183.35 \
        psk "XXX"
```
