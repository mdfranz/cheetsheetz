This is the basic setup I use on bare-metal Ubuntu Servers (amd64 or aarch64)

# Monitoring
- [Vector](https://vector.dev/releases/0.11.1/download/) - for log forwarding to remote systems or AWS
- [Telegraf](https://github.com/influxdata/telegraf/releases) - for metrics to be forwarded to [InfluxDB](https://www.influxdata.com/get-influxdb/) and then so metrics can be viewed with [Grafana](https://grafana.com/grafana/download)

# Raspberry Pi Disk Setup

For RPI (Jetson) that I use non-trivially I put the /var and /home partition on an external USB drive

This is so whatever you are doing in your home directory or /var (for docker or LXC or whatever) doesn't hit the SD-Card. 

```
LABEL=writable	/	 ext4	defaults	0 0
LABEL=system-boot       /boot/firmware  vfat    defaults        0       1
UUID="79038852-3311-490f-a4bc-85e548deb5d0" /home ext4  defaults        0 0
UUID="685a37b9-5405-4397-8539-9e005db9bcd4" /var ext4  defaults        0 0
```
	
