# Ubuntu 4

Compared to a decade+ ago you need to allow routes to propogate

## Configuration
```
frr version 8.4.4
frr defaults traditional
hostname ubuntu4
log syslog
no ipv6 forwarding
service integrated-vtysh-config
!
router bgp 65424
 bgp router-id 192.168.122.148
 neighbor 192.168.122.109 remote-as 65426
 !
 address-family ipv4 unicast
  network 192.168.4.0/24
  neighbor 192.168.122.109 route-map ALLOW_ALL in
  neighbor 192.168.122.109 route-map ALLOW_ALL out
 exit-address-family
exit
!
route-map ALLOW_ALL permit 10
exit
!
```

## Interfaces

```
root@ubuntu4:/var/log/frr# ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host noprefixroute
       valid_lft forever preferred_lft forever
2: enp1s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 52:54:00:01:5d:d5 brd ff:ff:ff:ff:ff:ff
    inet 192.168.122.148/24 metric 100 brd 192.168.122.255 scope global dynamic enp1s0
       valid_lft 2454sec preferred_lft 2454sec
    inet6 fe80::5054:ff:fe01:5dd5/64 scope link
       valid_lft forever preferred_lft forever
3: enp7s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 52:54:00:28:f9:4a brd ff:ff:ff:ff:ff:ff
    inet 192.168.4.1/24 brd 192.168.4.255 scope global enp7s0
       valid_lft forever preferred_lft forever
    inet6 fe80::5054:ff:fe28:f94a/64 scope link
       valid_lft forever preferred_lft forever`
```

# Ubuntu6 

```
frr version 8.4.4
frr defaults traditional
hostname ubuntu6
log syslog
no ipv6 forwarding
service integrated-vtysh-config
!
debug bgp neighbor-events
debug bgp updates in
debug bgp updates out
debug bgp zebra
debug bgp graceful-restart
!
router bgp 65426
 bgp router-id 192.168.122.109
 neighbor 192.168.122.148 remote-as 65424
 !
 address-family ipv4 unicast
  network 192.168.6.0/24
  neighbor 192.168.122.148 route-map ALLOW_ALL in
  neighbor 192.168.122.148 route-map ALLOW_ALL out
 exit-address-family
exit
!
route-map ALLOW_ALL permit 10
exit
!
```

# Status info

Show neighbor

```
ubuntu6# sh bgp neighbors
BGP neighbor is 192.168.122.148, remote AS 65424, local AS 65426, external link
  Local Role: undefined
  Remote Role: undefined
Hostname: ubuntu4
  BGP version 4, remote router ID 192.168.122.148, local router ID 192.168.122.109
  BGP state = Established, up for 02:05:28
  Last read 00:00:28, Last write 00:00:28
  Hold time is 180 seconds, keepalive interval is 60 seconds
  Configured hold time is 180 seconds, keepalive interval is 60 seconds
  Configured conditional advertisements interval is 60 seconds
  Neighbor capabilities:
    4 Byte AS: advertised and received
    Extended Message: advertised and received
    AddPath:
      IPv4 Unicast: RX advertised and received
    Long-lived Graceful Restart: advertised and received
      Address families by peer:
    Route refresh: advertised and received(old & new)
    Enhanced Route Refresh: advertised and received
    Address Family IPv4 Unicast: advertised and received
    Hostname Capability: advertised (name: ubuntu6,domain name: n/a) received (name: ubuntu4,domain name: n/a)
    Graceful Restart Capability: advertised and received
      Remote Restart timer is 120 seconds
      Address families by peer:
        none
  Graceful restart information:
    End-of-RIB send: IPv4 Unicast
    End-of-RIB received: IPv4 Unicast
    Local GR Mode: Helper*
    Remote GR Mode: Helper
    R bit: True
    N bit: True
    Timers:
      Configured Restart Time(sec): 120
      Received Restart Time(sec): 120
    IPv4 Unicast:
      F bit: False
      End-of-RIB sent: Yes
      End-of-RIB sent after update: Yes
      End-of-RIB received: Yes
      Timers:
        Configured Stale Path Time(sec): 360
  Message statistics:
    Inq depth is 0
    Outq depth is 0
                         Sent       Rcvd
    Opens:                  2          2
    Notifications:          0          0
    Updates:               12         12
    Keepalives:           127        127
    Route Refresh:          3          3
    Capability:             0          0
    Total:                144        144
  Minimum time between advertisement runs is 0 seconds

 For address family: IPv4 Unicast
  Update group 2, subgroup 2
  Packet Queue length 0
  Community attribute sent to this neighbor(all)
  Inbound path policy configured
  Outbound path policy configured
  Route map for incoming advertisements is *ALLOW_ALL
  Route map for outgoing advertisements is *ALLOW_ALL
  1 accepted prefixes

  Connections established 2; dropped 1
  Last reset 02:05:32,  No AFI/SAFI activated for peer
  External BGP neighbor may be up to 1 hops away.
Local host: 192.168.122.109, Local port: 179
Foreign host: 192.168.122.148, Foreign port: 48354
Nexthop: 192.168.122.109
Nexthop global: fe80::5054:ff:fe53:3ab5
Nexthop local: fe80::5054:ff:fe53:3ab5
BGP connection: shared network
BGP Connect Retry Timer in Seconds: 120
Estimated round trip time: 1 ms
Read thread: on  Write thread: on  FD used: 24
```

```
ubuntu6# sh bgp ipv4
BGP table version is 4, local router ID is 192.168.122.109, vrf id 0
Default local pref 100, local AS 65426
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath,
               i internal, r RIB-failure, S Stale, R Removed
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self
Origin codes:  i - IGP, e - EGP, ? - incomplete
RPKI validation codes: V valid, I invalid, N Not found

   Network          Next Hop            Metric LocPrf Weight Path
*> 192.168.4.0/24   192.168.122.148          0             0 65424 i
*> 192.168.6.0/24   0.0.0.0                  0         32768 i

Displayed  2 routes and 2 total paths
```
