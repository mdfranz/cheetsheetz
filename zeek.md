# Installation 

See [Ubuntu](https://software.opensuse.org/download.html?project=security%3Azeek&package=zeek-lts)

to install repo  

```
echo 'deb http://download.opensuse.org/repositories/security:/zeek/xUbuntu_24.04/ /' | sudo tee /etc/apt/sources.list.d/security:zeek.list
curl -fsSL https://download.opensuse.org/repositories/security:zeek/xUbuntu_24.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/security_zeek.gpg > /dev/null
sudo apt update
sudo apt install zeek-lts
```

# Plugins of Interest

## JA4

See https://github.com/FoxIO-LLC/ja4/tree/main/zeek but basically

```
# /opt/zeek/bin/zkg install zeek/foxio/ja4s
```

add `@load ja4` to `/opt/zeek/share/zeek/site/local.zeek`

and `@load policy/tuning/json-logs.zeek` to enable JSON logging unless you are daft

and then `[ZeekControl] > deploy`

# JQ Expressions

## DNS 
```
root@opti3070:/opt/zeek/logs/current# tail -f dns.log  | jq -r '[ .["id.orig_h"] , .query ] | @csv'
"192.168.2.214","franz-m1-2020.local"
"fe80::18ee:f37f:b14:f66b","franz-m1-2020.local"
"192.168.2.214","franz-m1-2020.local"
"fe80::18ee:f37f:b14:f66b","franz-m1-2020.local"
"fe80::18ee:f37f:b14:f66b","franz-m1-2020.local"
"192.168.2.214","franz-m1-2020.local"
"192.168.2.214","_ippusb._tcp.local"
"fe80::18ee:f37f:b14:f66b","_ippusb._tcp.local"
```
