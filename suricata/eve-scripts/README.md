# Finding corruption in JSON

I had a 20GB file where a single record had corrupted JSON that initial attempts to parse with DuckDB failed. 

```
mfranz@asus-pn50:~/suricata$ cat eve-2025-corrupted.json | jq 'select(.event_type=="dhcp")|.timestamp' 
jq: parse error: Invalid literal at line 29456650, column 2102
```

Use sed to confirm and delete 

```
 sed -n '29456650p' eve-2025-corrupted.json
```
{"timestamp":"2025-07-27T21:17:41.439098+0000","event_type":"stats","stats":{"uptime":1091055,"capture":{"kernel_packets":273210446,"kernel_drops":0,"errors":0,"afpacket":{"busy_loop_avg":0,"polls":218828853,"poll_signal":0,"poll_timeout":11705414,"poll_data":207123439,"poll_errors":0,"send_errors":0}},"decoder":{"pkts":273210446,"bytes":238308194881,"invalid":16865762,"ipv4":269995705,"ipv6":284471,"ethernet":273210446,"arp":2904664,"unknown_ethertype":28858,"chdlc":0,"raw":0,"null":0,"sll":0,"tcp":89609735,"udp":163408227,"sctp":0,"esp":1,"icmpv4":292695,"icmpv6":55467,"ppp":0,"pppoe":0,"geneve":0,"gre":0,"vlan":256279496,"vlan_qinq":0,"vlan_qinqinq":0,"vxlan":0,"vntag":0,"ieee8021ah":0,"teredo":3248,"ipv4_in_ipv6":0,"ipv6_in_ipv6":0,"mpls":0,"avg_pkt_size":872,"max_pkt_size":1530,"max_mac_addrs_src":0,"max_mac_addrs_dst":0,"erspan":0,"nsh":0,"event":{"ipv4":{"pkt_too_small":0,"hlen_too_small":0,"iplen_smaller_than_hlen":0,"trunc_pkt":16865751,"opt_invalid":0,"opt_invalid_len":0,"opt_malformed":0,"opt_pad_required":45033,"opt_eol_required":0,"opt_duplicate":0,"opt_unknown":0,"wrong_ip_version":0,"icmpv6":0,"frag_pkt_too_large":0,"frag_overlap":0,"frag_ignored":0},"icmpv4":{"pkt_too_small":0,"unknown_type":0,"unknown_code":0,"ipv4_trunc_pkt":0,"ipv4_unknown_ver":0},"icmpv6":{"unknown_type":0,"unknown_code":0,"pkt_too_small":0,"ipv6_unknown_version":0,"ipv6_trunc_pkt":0,"mld_message_with_invalid_hl":0,"unassigned_type":0,"experimentation_type":0},"ipv6":{"pkt_too_small":0,"trunc_pkt":11,"trunc_exthdr":0,"exthdr_dupl_fh":0,"exthdr_useless_fh":0,"exthdr_dupl_rh":0,"exthdr_dupl_hh":0,"exthdr_dupl_dh":0,"exthdr_dupl_ah":0,"exthdr_dupl_eh":0,"exthdr_invalid_optlen":0,"wrong_ip_version":0,"exthdr_ah_res_not_null":0,"hopopts_unknown_opt":0,"hopopts_only_padding":0,"dstopts_unknown_opt":0,"dstopts_only_padding":0,"rh_type_0":0,"zero_len_padn":43952,"fh_non_zero_reserved_field":0,"data_after_none_header":0,"unknown_next_header":0,"icmpv4":0,"frag_pkt_too_large":0,"frag_overlap":0,"frag_invalid_length":0,"frag_ignored":0,"ipv4_in_ipv6_too_small":0,"ipv4_in_ipv6_wr{"timestamp":"2025-07-27T23:04:29.083676+0000","flow_id":1485286801735706,"in_iface":"tap0","event_type":"dns","vlan":[2],"src_ip":"192.168.3.184","src_port":12753,"dest_ip":"1.1.1.1","dest_port":53,"proto":"UDP","pkt_src":"wire/pcap","dns":{"version":2,"type":"query","id":48115,"rrname":"connectivitycheck.gstatic.com","rrtype":"A","tx_id":0,"opcode":0}}


Delete the bad line

```
sed '29456650d' eve-2025-corrupted.json > eve-2025-fixed.json
```
