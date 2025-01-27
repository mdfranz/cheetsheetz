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

# DuckDB Analysis

## DNS (JSON)

The data
```
D .mode line
D select * from dns limit 1;
         ts = 1733616000.00134
        uid = CXvqi3jemNNcTDBk5
  id.orig_h = 192.168.2.177
  id.orig_p = 58786
  id.resp_h = 192.168.1.1
  id.resp_p = 53
      proto = udp
   trans_id = 16868
      query = verizon.net
     qclass = 1
qclass_name = C_INTERNET
      qtype = 28
 qtype_name = AAAA
      rcode = 0
 rcode_name = NOERROR
         AA = false
         TC = false
         RD = true
         RA = false
          Z = 0
   rejected = false
        rtt = 
    answers = 
       TTLs = 
```

Queries 

```
create table dns as select * from read_json("202*/*dns*.gz",ignore_errors=true);
select query, count(*) as cnt from dns group by query order by cnt desc limit 50;
select query, count(*) as cnt from dns where query like '%microsoft.com' group by query order by cnt limit 50;
```
