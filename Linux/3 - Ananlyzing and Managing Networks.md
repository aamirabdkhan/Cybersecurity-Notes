# Analyzing Networks with `ifconfig`

`ifconfig` --> This command is one of the most basic tool for examining and interacting with active network interfaces.

`eth0` --> Short form for Ethernet, This is the first wired connection. If there were more wired connection they would have showed up of the screen (eth1, eth2, etc)

`inet add: 192.168.1.1` --> IP address currently assigned to that network
`Bcast` --> Broadcast address, address which is used to send out to all the other IPs on the subnet
`Mask` --> network mask, this is used to determine the what part of the IP address is connected to the network

`lo` --> short form for loopback address and is sometimes called as Localhost.
- Special address that connects you to your own system.
- Software and services not running on your system can't use it.
- We use `lo` to test something on your system such as web server.
- The localhost is generally represented with the IP address of `127.0.0.1`

`wlan0` --> appears only when you have a wireless interface or adapter

This info from `ifconfig` enables you to connect to and manipulate your local area network

# Checking wireless network devices with `iwconfig`
`iwconfig` --> This command is used when you have a wireless adapter
- It can be used for gathering crucial info for wireless hacking
- such as IP address, MAC address, what mode it's on and more
```
┌──(deadboy㉿kali)-[~/CyberSecurity/Linux Basics for Hackers/Commands]
└─$ iwconfig
lo        no wireless extensions.

eth0      no wireless extensions.

wlan0     IEEE 802.11  ESSID:"Asjad"  
          Mode:Managed  Frequency:2.457 GHz  Access Point: 58:D5:6E:CC:86:7D   
          Bit Rate=1 Mb/s   Tx-Power=16 dBm   
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Power Management:off
          Link Quality=62/70  Signal level=-48 dBm  
          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
          Tx excessive retries:0  Invalid misc:11   Missed beacon:0
```
for `wlan0` we learn that our standards are simpel 802.11 and doesn't have b and g

we also learn the mode of the wifi which is `managed` in contrast to `monitor or promiscous`. We'll need `promiscous`  mode for cracking wireless passwords

# Changing your Network Information
## Changing your IP Address
Syntax
``` 
ifconfig <interface name> <new IP Address>
ifconfig ehto 192.168.23.45
```
## Changing your Network Mask and Broadcast Address
Syntax:
```
ifconfig <interface> <new IP> netmask <new mask> broadcast <new bcast>
ifconfig eth0 192.168,122.133 netmask 255.255.255.0 broadcast 192.168.1.255
```
## Spoofing your MAC Address
- We can also use `ifconfig` to change our MAC Address.
- MAC Address is globally unique and is often used as a security measure to keep hackers out of networks
- To spoof your MAC Address you should do the following steps:
	1. take your interface down with `ifconfig <interface> down`
	2. now specify your interface followed by the new MAC Address
	3. Now bring the interface back up
Demo:
```
ifconfig eht0 down
ifconfig eth0 hw ether 00:11:22:33:44:55
ifconfig eth0 up
```
## Assigning new IP Addresses from the DHCP server
Linux has a Dynamic Host Configuration Protocol (DHCP) server that runs a *daemon*
- Daemon --> A process that runs in the background called dhcpd or the dhcp daemon

### Working of DHCP
- DHCP server assigns IP addresses to all the system on the subnet and keeps a log files of which IP address is allocated to which machine at any one time.
### Requesting an IP Address from DHCP without rebooting
- call the DHCP server with the `dhclient` command followed by the interface face name
Syntax: `dhclient eth0`
	**Working**
	- `dhclient` command sends a `DHCPDISCOVER` request from the network interface specified (here, `eth0`).
	- It then receives an offer `DHCPOFFER` from the DHCP Server (192.168.181.131) and confirms the IP assignment to the DHCP server by sending a DHCP request
# Manipulating the Domain Name System
## Examining DNS with `dig`
DNS --> It is service that translates a domain name like hackers-arise.com to the appropriate IP address, that way your system knows how to get to the website without your remembering the actual IP Address

### `dig` command
`dig` --> This command offers a way to gather DNS Info about a target domain
- This info could include IP address of the Target's nameserver (the seerver that translates the target's name to an IP address), target's email server and potentially any subdomains and IP Addresses
```
┌──(deadboy㉿kali)-[~]
└─$ dig hackers-arise.com ns

; <<>> DiG 9.19.21-1-Debian <<>> hackers-arise.com ns
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 8452
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 3

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
; COOKIE: 48d0c6955ef4afe50100000066b66a5e277a73f30cbda14a (good)
;; QUESTION SECTION:
;hackers-arise.com.             IN      NS

;; ANSWER SECTION:
hackers-arise.com.      86400   IN      NS      ns6.wixdns.net.
hackers-arise.com.      86400   IN      NS      ns7.wixdns.net.

;; ADDITIONAL SECTION:
ns7.wixdns.net.         600     IN      A       216.239.34.100
ns6.wixdns.net.         600     IN      A       216.239.32.100

;; Query time: 140 msec
;; SERVER: 192.168.0.1#53(192.168.0.1) (UDP)
;; WHEN: Sat Aug 10 00:43:34
```
`ns` --> nameserver
- The nameserver of the target website is shown in the ANSWER SECTION
- The ADDITIONAL SECTION in the dig query reveals the IP address of the DNS server serving the target website
- To get the info on email servers connected to target, it can be done by adding the mx option
The most common LINUX DNS server is the Berkley Internet Name Domain (BIND), In some cases LINUX users will refer the DNS as BIND don't be confused.
## Changing your DNS Server
- In some cases you want to change the DNS Server
- To do so  you can edit the the IP address of the DNS server in the `/etc/resolv.conf` file
- In the `/etc/resolv.conf` file change the IP which is written after the `nameserver`
```
┌──(deadboy㉿kali)-[~]
└─$ leafpad /etc/resolv.conf
```
![[Pasted image 20240810005607.png]]
you can even overwrite the IP address with the `echo` command
`echo "nameserver 8.8.8.8" > /etc/resolv.conf`
## Mapping your own IP Addresses
- A file on your system called the `hosts` file also performs domain name-IP adress translation. it is located in `/etc/hosts` and just like DNS, you can use ti to specify your own IP Address domain name mapping.
- In simple words this can determine which IP address your browser goes to when you enter `www.aadsds.com` into the browser, rather than let the DNS server decide.
- This can be useful for hijacking a TCP connection with a tool such as dnsspoof
![[Pasted image 20240810010613.png]]
```
┌──(deadboy㉿kali)-[~]
└─$ leafpad /etc/hosts 
```
- By default the file contains your localhost at 127.0.0.1
- and your system's hostname kali at 127.0.1.1
- but we can add our own IP address along with the domain name with it
- 127.0.2.1         www.aamir.com
- like in the example abobe (make certain you press TAB between the IP address and the domain name)
- As you'll get more envolved in hacking search about dnsspoof and Ettercap
