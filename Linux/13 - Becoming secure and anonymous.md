# The Onion Router System
- US Office of Naval Research develop the anonymously navigating the internet system for espionage purposes.
- The plan was to set up a network of routers that was separate from the internet's router, that could encrypt the traffic, and that only stored the unencrypted IP address of the previous router ---  meaning all other router addresses along the way were encrypted.
## *TOR Browser*
download the tor browser from the tor project website
Extract the downloaded file
```
tar -xvf <tor filename>
```
moving the downloaded file to opt
```
sudo mv tor-browser /opt/tor-browser
```
```
folder path ./start-tor-browser.desktop
```
# Proxy Servers
**Proxies** --> Intermediate system which act as middlemen for traffic:

the user connects to a proxy -> and the traffic is given the IP Address of the proxy before it's passed on (Like the image below). When the traffic returns from the destination, the proxy sends the traffic back to the source.                                  
![](../Attachments/Pasted%20image%2020240918230132.png)

- Kali has an excellent proxying tool called `proxyschains`
Syntax for the `proxychains` command
```
proxychains <the command you want to proxied> <arguments>
```
- arguments might include IP address
Example: Using proxychains to scan a site with `nmap` anonymously
```
proxychains nmap -sT - Pn <IP Address>
 ```
## *Setting Proxies in the `config` file* 
```
# using leafpad to open the proxychains config file
leafpad /etc/proxychains.conf
```
At line 61 we can see the proxyLists
```
[ProxyList]
# add proxy here ...
# meanwile
# defaults set to "tor"
socks4 	127.0.0.1 9050
```
we can add proxies by entering the IP addresses and ports of the proxies we want to use in that list
### *Some more interesting options*
- We can put in multiple proxies and use all of them.
-  we can use a limited number from the list.
- or we can have proxychains change the order randomly
#### Adding more proxies
we can add multiple proxies below the line "add proxy here"
```
proxychains firefox www.hackersarise.com
```
#### Dynamic Chaining
- With multiple IPs in our `proxychains.conf` file we can set up dynamic chaining which runs our traffic through every proxy on our list and, if one of the proxies is down or not responding, automatically goes to the next proxy in the list without throwing an error. If we didn't set this up a single failing proxy would break our request
- In `proxychains.conf` find line 10 Dynamic Chain and uncomment it.
#### Random Chaining 
- `proxychains` will randomly choose a set of IP addresses from our list and use them to create our proxy chain.
- This option is also considered as dynamic because if one of the proxies is down, it will skip to the next one.
- In `proxychains.conf` comment out the dynamic_chain and strict_chain, then uncomment the random_chain.
- We can only use one of these three options at a time.
- Next find the chain_len and uncomment it and then give it a reasonable number. This line determines how many of the IP addresses in your chain will be used in creating your random proxy chain. For example if give it a value of 3 it will use 3 prxoies from the list.
- Although this enhances anonymitybut it increases the latency of our online activites

