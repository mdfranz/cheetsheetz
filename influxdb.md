# InfluxDB 2.x OSS

- See https://docs.influxdata.com/influxdb/v2.6/install/?t=Linux#install-influxdb-as-a-service-with-systemd
- Get from https://github.com/influxdata/influxdb/releases





# Old

## Directory 



## Basic Queries

```
> select average_response_ms,host FROM ping limit 10;
name: ping
time                average_response_ms host
----                ------------------- ----
1594163670000000000 9.864               e4300
1594163680000000000 18.321              e4300
1594163690000000000 18.539              e4300
1594163700000000000 11.57               e4300
1594163710000000000 17.924              e4300
1594163720000000000 11.797              e4300
1594163730000000000 12.549              e4300
1594163740000000000 9.264               e4300
1594163750000000000 10.148              e4300
1594163760000000000 14.105              e4300
```

## Tags

Tags are ...

```
> show tag keys                                                                                                                                                                                                                      
name: cpu                                                                                                                                                                                                                            
tagKey                                                                                                                                                                                                                               
------                                                                                                                                                                                                                               
cpu                                                                                                                                                                                                                                  
host                                                                                                                                                                                                                                 
                                                                                                                                                                                                                                     
name: disk                                                                                                                                                                                                                           
tagKey                                                                                                                                                                                                                               
------                                                                                                                                                                                                                               
device                                                                                                                                                                                                                               
fstype                                                                                                                                                                                                                               
host                                                                                                                                                                                                                                 
mode                                                                                                                                                                                                                                 
path 
```



### Viewing Values for a Key
```
> show tag values with key = url
name: ping
key value
--- -----
url 192.168.1.1
url google.com
url verizon.net
```

```
> show tag values with key = host                                                                                                                                                                                                    
name: cpu                                                                                                                                                                                                                            
key  value                                                                                                                                                                                                                           
---  -----                                                                                                                                                                                                                           
host dc8500                                                                                                                                                                                                                          
host e4300                                                                                                                                                                                                                           
host mfranz-h30                                                                                                                                                                                                                      
host optiplex3010                                                                                                                                                                                                                    
host penguin                                                                                                                                                                                                                         
host penguin123                                                                                                                                                                                                                      
host pi0w-8400d6a5                                                                                                                                                                                                                   
host pi3b-0ef66bb41                                                                                                                                                                                                                  
                                                                                                                                                                                                                                     
name: disk                                                                                                                                                                                                                           
key  value                                                                                                                                                                                                                           
---  -----                                                                                                                                                                                                                           
host dc8500                                                                                                                                                                                                                          
host e4300                                                                                                                                                                                                                           
host mfranz-h30                                                                                                                                                                                                                      
host optiplex3010                                                                                                                                                                                                                    
host penguin                                                                                                                                                                                                                         
host penguin123                                                                                                                                                                                                                      
host pi0w-8400d6a5                                                                                                                                                                                                                   
host pi3b-0ef66bb41
```

