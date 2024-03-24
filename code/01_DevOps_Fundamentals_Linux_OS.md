# LINUX OS
## Sample of Master node to make new folder on worker node through ssh

Below is a master node 192.168.68.116 that will aim to reach Raspberry Pi

```sh
$ ip addr show
	1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
	    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
	    inet 127.0.0.1/8 scope host lo
	       valid_lft forever preferred_lft forever
	    inet6 ::1/128 scope host 
	       valid_lft forever preferred_lft forever
	2: enp61s0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN group default qlen 1000
	    link/ether 4c:cc:6a:e2:1d:9c brd ff:ff:ff:ff:ff:ff
	3: wlp62s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default qlen 1000
	    link/ether 9c:b6:d0:1d:9d:c3 brd ff:ff:ff:ff:ff:ff
	    inet 192.168.68.116/24 brd 192.168.68.255 scope global dynamic noprefixroute wlp62s0
	       valid_lft 5786sec preferred_lft 5786sec
	    inet6 fe80::8fa6:dca4:e568:7457/64 scope link noprefixroute 
	       valid_lft forever preferred_lft forever
	4: mpqemubr0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default qlen 1000
	    link/ether 52:54:00:f2:6f:ed brd ff:ff:ff:ff:ff:ff
	    inet 10.116.10.1/24 brd 10.116.10.255 scope global mpqemubr0
	       valid_lft forever preferred_lft forever
	    inet6 fe80::5054:ff:fef2:6fed/64 scope link 
	       valid_lft forever preferred_lft forever
	6: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default 
	    link/ether 02:42:67:31:ea:47 brd ff:ff:ff:ff:ff:ff
	    inet 172.17.0.1/16 brd 172.17.255.255 scope global docker0
	       valid_lft forever preferred_lft forever
```
As soon as Master Node tried to ping we will get below 
```txt
$ ping 192.168.68.121
	PING 192.168.68.121 (192.168.68.121) 56(84) bytes of data.
	64 bytes from 192.168.68.121: icmp_seq=1 ttl=64 time=85.8 ms
	64 bytes from 192.168.68.121: icmp_seq=2 ttl=64 time=8.91 ms
	64 bytes from 192.168.68.121: icmp_seq=3 ttl=64 time=10.4 ms
```
The ping will stop as purposely stop the access from Raspberry Pi to mimic the down time.
```txt
$ sudo iptables -A INPUT -s 192.168.68.116 -p icmp --icmp-type echo-request -j DROP
```
It will start pinging again as I enable it like below to mimic the resolved down time.
```txt
$ sudo iptables -D INPUT -s 192.168.68.116 -p icmp --icmp-type echo-request -j DROP
```
...like below
```txt
	64 bytes from 192.168.68.121: icmp_seq=4 ttl=64 time=9.25 ms
	64 bytes from 192.168.68.121: icmp_seq=5 ttl=64 time=8.75 ms
	64 bytes from 192.168.68.121: icmp_seq=6 ttl=64 time=8.58 ms
	64 bytes from 192.168.68.121: icmp_seq=7 ttl=64 time=10.9 ms
	64 bytes from 192.168.68.121: icmp_seq=8 ttl=64 time=14.9 ms
	64 bytes from 192.168.68.121: icmp_seq=9 ttl=64 time=8.06 ms
```
Ultimately the master node can control Raspberry Pi. Below example is to make a new folder
```txt
$ ssh atjioesman@192.168.68.121 mkdir -p /home/atjioesman/test
	The authenticity of host '192.168.68.121 (192.168.68.121)' can't be established.
	ECDSA key fingerprint is SHA256:lNhIcdbqErBh8DG4v2mzLJqv/S1i8QHz4AFhsoulm5g.
	Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
	Warning: Permanently added '192.168.68.121' (ECDSA) to the list of known hosts.
	atjioesman@192.168.68.121's password: 

$ ssh atjioesman@192.168.68.121 mkdir -p /home/atjioesman/test3
	atjioesman@192.168.68.121's password: 
```
