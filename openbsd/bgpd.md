


# BGP
- https://kaizo.org/2024/01/03/openbsd-bgpd/
- https://docs.vultr.com/configuring-bgp-on-vultr-with-openbsd
- https://kernelpanic.life/software/high-availability-with-openbgpd-on-openbsd.html
- https://www.packetmischief.ca/openbsd-openbgpd-notes/


## Minimal Config

```
AS 4202

router-id 192.168.122.106
network 192.168.2.0/24

neighbor 192.168.122.147 {
        remote-as 4201
        descr "upstream1"
}  

allow from any inet prefixlen 8 - 24
deny from any prefix 0.0.0.0/0
deny from any prefix 169.254.0.0/16 prefixlen >= 16
deny from any prefix 224.0.0.0/4 prefixlen >= 4
allow to any

log updates

```
