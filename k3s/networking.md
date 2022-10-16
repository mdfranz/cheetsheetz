

Chain INPUT (policy ACCEPT 613 packets, 135K bytes)
 pkts bytes target     prot opt in     out     source               destination
  918  201K KUBE-ROUTER-INPUT  all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* kube-router netpol - 4IA2OSFRMVNDXBVV */
  613  135K KUBE-NODEPORTS  all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* kubernetes health check service ports */
    6   264 KUBE-EXTERNAL-SERVICES  all  --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate NEW /* kubernetes externally-visible service portals */
  613  135K KUBE-FIREWALL  all  --  *      *       0.0.0.0/0            0.0.0.0/0


Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
 pkts bytes target     prot opt in     out     source               destination         
    4   208 KUBE-ROUTER-FORWARD  all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* kube-router netpol - TEMCG2JMHZYE7H7T */
    0     0 KUBE-FORWARD  all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* kubernetes forwarding rules */
    0     0 KUBE-SERVICES  all  --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate NEW /* kubernetes service portals */
    0     0 KUBE-EXTERNAL-SERVICES  all  --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate NEW /* kubernetes externally-visible service portals */
    0     0 ACCEPT     all  --  *      *       10.42.0.0/16         0.0.0.0/0            /* flanneld forward */
    0     0 ACCEPT     all  --  *      *       0.0.0.0/0            10.42.0.0/16         /* flanneld forward */


Chain OUTPUT (policy ACCEPT 573 packets, 224K bytes)
 pkts bytes target     prot opt in     out     source               destination         
  909  276K KUBE-ROUTER-OUTPUT  all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* kube-router netpol - VEAAIY32XVBHCSCY */
    8   448 KUBE-SERVICES  all  --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate NEW /* kubernetes service portals */
  573  224K KUBE-FIREWALL  all  --  *      *       0.0.0.0/0            0.0.0.0/0           

Chain KUBE-EXTERNAL-SERVICES (2 references)
 pkts bytes target     prot opt in     out     source               destination         

Chain KUBE-FIREWALL (2 references)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* kubernetes firewall for dropping marked packets */ mark match 0x8000/0x8000
    0     0 DROP       all  --  *      *      !127.0.0.0/8          127.0.0.0/8          /* block incoming localnet connections */ ! ctstate RELATED,ESTABLISHED,DNAT


Chain KUBE-FORWARD (1 references)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 DROP       all  --  *      *       0.0.0.0/0            0.0.0.0/0            ctstate INVALID
    0     0 ACCEPT     all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* kubernetes forwarding rules */ mark match 0x4000/0x4000
    0     0 ACCEPT     all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* kubernetes forwarding conntrack rule */ ctstate RELATED,ESTABLISHED


Chain KUBE-KUBELET-CANARY (0 references)
 pkts bytes target     prot opt in     out     source               destination         

Chain KUBE-NODEPORTS (1 references)
 pkts bytes target     prot opt in     out     source               destination         

Chain KUBE-NWPLCY-DEFAULT (18 references)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 MARK       all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* rule to mark traffic matching a network policy */ MARK or 0x10000

Chain KUBE-POD-FW-4TBGXTVMHTNMZMVN (7 references)
 pkts bytes target     prot opt in     out     source               destination         
   25  5728 ACCEPT     all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* rule for stateful firewall for pod */ ctstate RELATED,ESTABLISHED
    0     0 ACCEPT     all  --  *      *       0.0.0.0/0            10.42.0.10           /* rule to permit the traffic traffic to pods when source is the pod's local node */ ADDRTYPE match src-type LOCAL
    0     0 KUBE-NWPLCY-DEFAULT  all  --  *      *       10.42.0.10           0.0.0.0/0            /* run through default egress network policy  chain */
    0     0 KUBE-NWPLCY-DEFAULT  all  --  *      *       0.0.0.0/0            10.42.0.10           /* run through default ingress network policy  chain */
    0     0 NFLOG      all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* rule to log dropped traffic POD name:acorn-api-7b65bf697c-6h8q7 namespace: acorn-system */ mark match ! 0x10000/0x10000 limit: avg 10/min burst 10 nflog-group 100
    0     0 REJECT     all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* rule to REJECT traffic destined for POD name:acorn-api-7b65bf697c-6h8q7 namespace: acorn-system */ mark match ! 0x10000/0x10000 reject-with icmp-port-unreachable
    0     0 MARK       all  --  *      *       0.0.0.0/0            0.0.0.0/0            MARK and 0xfffeffff
    0     0 MARK       all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* set mark to ACCEPT traffic that comply to network policies */ MARK or 0x20000

Chain KUBE-POD-FW-7FRHLS7SY4DK552W (7 references)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 ACCEPT     all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* rule for stateful firewall for pod */ ctstate RELATED,ESTABLISHED
    0     0 ACCEPT     all  --  *      *       0.0.0.0/0            10.42.0.8            /* rule to permit the traffic traffic to pods when source is the pod's local node */ ADDRTYPE match src-type LOCAL
    0     0 KUBE-NWPLCY-DEFAULT  all  --  *      *       10.42.0.8            0.0.0.0/0            /* run through default egress network policy  chain */
    0     0 KUBE-NWPLCY-DEFAULT  all  --  *      *       0.0.0.0/0            10.42.0.8            /* run through default ingress network policy  chain */
    0     0 NFLOG      all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* rule to log dropped traffic POD name:svclb-traefik-b8c67b47-r8szh namespace: kube-system */ mark match ! 0x10000/0x10000 limit: avg 10/min burst 10 nflog-group 100
    0     0 REJECT     all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* rule to REJECT traffic destined for POD name:svclb-traefik-b8c67b47-r8szh namespace: kube-system */ mark match ! 0x10000/0x10000 reject-with icmp-port-unreachable
    0     0 MARK       all  --  *      *       0.0.0.0/0            0.0.0.0/0            MARK and 0xfffeffff
    0     0 MARK       all  --  *      *       0.0.0.0/0            0.0.0.0/0            /* set mark to ACCEPT traffic that comply to network policies */ MARK or 0x20000


snip...

Chain KUBE-ROUTER-INPUT (1 references)
 pkts bytes target     prot opt in     out     source               destination         
    0     0 RETURN     all  --  *      *       0.0.0.0/0            10.43.0.0/16         /* allow traffic to primary cluster IP range - TZZOAXOCHPHEHX7M */
    0     0 RETURN     tcp  --  *      *       0.0.0.0/0            0.0.0.0/0            /* allow LOCAL TCP traffic to node ports - LR7XO7NXDBGQJD2M */ ADDRTYPE match dst-type LOCAL multiport dports 30000:32767
    0     0 RETURN     udp  --  *      *       0.0.0.0/0            0.0.0.0/0            /* allow LOCAL UDP traffic to node ports - 76UCBPIZNGJNWNUZ */ ADDRTYPE match dst-type LOCAL multiport dports 30000:32767
    0     0 KUBE-POD-FW-7FRHLS7SY4DK552W  all  --  *      *       10.42.0.8            0.0.0.0/0            /* rule to jump traffic from POD name:svclb-traefik-b8c67b47-r8szh namespace: kube-system to chain KUBE-POD-FW-7FRHLS7SY4DK552W */
    3   195 KUBE-POD-FW-M4VKHH7SE6MAJ5UB  all  --  *      *       10.42.0.9            0.0.0.0/0   




