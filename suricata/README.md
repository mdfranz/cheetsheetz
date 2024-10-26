# Installation

Use [ppa](https://launchpad.net/~oisf/+archive/ubuntu/suricata-stable) and change the interface in `/etc/suricata/suricata.yaml`

The latest package install is [here](https://docs.suricata.io/en/suricata-7.0.4/install.html#binary-packages)

and enable Redis support for EVE.

```
  - eve-log:
      enabled: yes
      filetype: redis #regular|syslog|unix_dgram|unix_stream|redis
      filename: eve.json
      # Enable for multi-threaded eve.json output; output files are amended with
      # an identifier, e.g., eve.9.json
      #threaded: false
      #prefix: "@cee: " # prefix to prepend to each log entry
      # the following are valid when type: syslog above
      #identity: "suricata"
      #facility: local5
      #level: Info ## possible levels: Emergency, Alert, Critical,
                   ## Error, Warning, Notice, Info, Debug
      #ethernet: no  # log ethernet header in events when available
      redis:
        server: 127.0.0.1
        port: 6379
        async: true ## if redis replies are read asynchronously
        mode: list ## possible values: list|lpush (default), rpush, channel|publish
```

To confirm monitoring

```
root@zimaboard:/etc/suricata# redis-cli monitor
OK
1690661646.338789 [0 127.0.0.1:41416] "LPUSH" "suricata" "{\"timestamp\":\"2023-07-29T20:14:06.338201+0000\",\"flow_id\":2062992877043484,\"in_iface\":\"enp2s0\",\"event_type\":\"flow\",\"src_ip\":\"10.0.0.125\",\"src_port\":43631,\"dest_ip\":\"10.0.0.1\",\"dest_port\":5351,\"proto\":\"UDP\",\"app_proto\":\"failed\",\"flow\":{\"pkts_toserver\":2,\"pkts_toclient\":2,\"bytes_toserver\":126,\"bytes_toclient\":166,\"start\":\"2023-07-29T20:13:27.808007+0000\",\"end\":\"2023-07-29T20:13:27.808614+0000\",\"age\":0,\"state\":\"new\",\"reason\":\"timeout\",\"alerted\":false},\"host\":\"zimaboard\"}"
1690661647.518402 [0 127.0.0.1:41416] "LPUSH" "suricata" "{\"timestamp\":\"2023-07-29T20:14:07.517234+0000\",\"flow_id\":2221503130018804,\"in_iface\":\"enp2s0\",\"event_type\":\"quic\",\"src_ip\":\"10.0.0.125\",\"src_port\":34524,\"dest_ip\":\"142.251.163.105\",\"dest_port\":443,\"proto\":\"UDP\",\"pkt_src\":\"wire/pcap\",\"quic\":{\"version\":\"1\",\"sni\":\"www.google.com\",\"ja3\":{\"hash\":\"0c3a67d7dad1c9a6c4f3801a68500c62\",\"string\":\"771,4865-4866-4867,51-42-13-43-27-45-57-16-17513-10-0-41,29-23-24,\"},\"extensions\":[{\"name\":\"key_share\",\"type\":51},{\"name\":\"early_data\",\"type\":42},{\"name\":\"signature_algorithms\",\"type\":13},{\"name\":\"supported_versions\",\"type\":43},{\"name\":\"compress_certificate\",\"type\":27},{\"name\":\"psk_key_exchange_modes\",\"type\":45},{\"name\":\"quic_transport_parameters\",\"type\":57},{\"name\":\"alpn\",\"type\":16,\"values\":[\"h3\"]},{\"type\":17513},{\"name\":\"supported_groups\",\"type\":10},{\"name\":\"server_name\",\"type\":0,\"values\":[\"www.google.com\"]},{\"name\":\"pre_shared_key\",\"type\":41}]},\"host\":\"zimaboard\"}"
1690661647.554148 [0 127.0.0.1:41416] "LPUSH" "suricata" "{\"timestamp\":\"2023-07-29T20:14:07.553479+0000\",\"flow_id\":2221503130018804,\"in_iface\":\"enp2s0\",\"event_type\":\"quic\",\"src_ip\":\"142.251.163.105\",\"src_port\":443,\"dest_ip\":\"10.0.0.125\",\"dest_port\":34524,\"proto\":\"UDP\",\"pkt_src\":\"wire/pcap\",\"quic\":{\"version\":\"1\",\"ja3s\":{\"hash\":\"2b0648ab686ee45e0e7c35fcfb0eea7e\",\"string\":\"771,4865,41-51-43\"},\"extensions\":[{\"name\":\"pre_shared_key\",\"type\":41},{\"name\":\"key_share\",\"type\":51},{\"name\":\"supported_versions\",\"type\":43}]},\"host\":\"zimaboard\"}"
```


Watching DNS Requests

```
jq 'select(.event_type == "dns")| .dns' | jq -r 'select(.type == "query")| .rrname'
```

And TLS SNI

```
jq 'select(.event_type == "tls")|.tls.sni'
```

## General Config
- https://thehackerwhorolls.blogspot.com/2019/10/suricata-cheat-sheet.html

## Log Shipping
- https://austinsonger.medium.com/installing-suricata-and-filebeat-on-centos-and-shipping-suricata-logs-to-elastic-siem-48c7c4d784ee

## Parsing JSON 
- https://suricata.readthedocs.io/en/suricata-6.0.1/output/eve/eve-json-examplesjq.html
- https://www.stamus-networks.com/blog/2015/05/18/looking-at-suricata-json-events-on-command-line

## Using Bethos/Red Panda Connect

Create the following file after installing the latest [redpanda connect release](https://github.com/redpanda-data/connect/releases/)

```
input:
  redis_list:
    url: tcp://localhost:6379
    key: suricata

output:
    nats:
      urls: 
        - 100.74.151.61:4222
      subject: 'suricata.${! json("event_type") }'
```

