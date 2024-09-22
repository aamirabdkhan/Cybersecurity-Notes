We will examine the two most famous wireless connections i.e. Wi-Fi and Bluetooth.
# Wi-Fi Networks
- **AP (Access Point** --> This is the device wireless users connect to for internet access
- **ESSID (Extended service set Identifier)** --> This is the same as the SSID, but it can be used for multiple APs in a wireless LAN.
- **BSSID (Basic Service set identifier** --> This is the unique identifier of each AP, and it is the same as the MAC Address of the device.
- **SSID (Service set Identifier)** --> This is the name of the network.
- **Channels** --> 

## Basic Wireless Commands
- `ifconfig` --> Lists each activated network interface on your system along with some basic statistics, including the IP address of each interface.
- In Kali Linux Wi-Fi interfaces are usually designated as **wlan*X*** where ***X*** represents the number of that interface.
- `iwconfig` --> if we just want to see the Wi-Fi interfaces and their statistics.
```
┌──(deadboy㉿kali)-[~]
└─$ iwconfig
lo        no wireless extensions.

eth0      no wireless extensions.

wlan0     IEEE 802.11  ESSID:"Asjad"  
          Mode:Managed  Frequency:2.457 GHz  Access Point: 58:D5:6E:CC:86:7D   
          Bit Rate=72.2 Mb/s   Tx-Power=16 dBm   
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Power Management:off
          Link Quality=57/70  Signal level=-53 dBm  
          Rx invalid nwid:0  Rx invalid crypt:0  Rx invalid frag:0
          Tx excessive retries:0  Invalid misc:109   Missed beacon:0
```
Here, we just see the wireless interfaces, also known as *network cards* and key data about them, including the wireless standard utilized, whether the ESSID is off and the mode.
- The mode has three settings: 
  1. **Managed** --> means it is ready to join or has joined an AP
  2. **Master** --> means it is ready to act as or already is an AP.
  3. **Monitor** --> 

- `iwlist` --> We can see all the wireless access points your network card can reach using this command.
	- Syntax: `iwlist <interface> <action>`
- The output from this command include all the Wi-Fi Aps within the range of our wireless interface, along with the key data about each AP.
	- such as MAC address of the AP
	- the channel
	- the frequency it is operating on,
	- it's quality
	- signal level
	- whether it's encryption key is enabled

- You will need the MAC Address of the target AP (BSSID) , the MAC address of a client (another wireless network card) and the channel the AP is operating on in order to perform any kind of hacking.

- `nmcli` --> used to view the Wi-Fi Aps near us and their key data
	- Syntax: `nmcli dev networktype`
	- `dev` --> short for devices and the type is wifi (in this case)
- Syntax to connect to an AP: `nmcli dev wifi connect AP-SSID password AP-password`
```
┌──(deadboy㉿kali)-[~]
└─$ nmcli dev wifi connect Asjad password Aamir21co11
Device 'wlan0' successfully activated with '35d36081-c57d-4070-80f4-496432278978'.
```
## Wi-Fi Recon with `aircrack-ng`
#### Step 1: 
- Putting wireless network card in monitor mode
- To do so using the `airmon-ng` command from the `aircrack-ng` s
Syntax:
`airmon-ng start|stop|restart interface`
To put wireless network card in monitor mode
`airmon-ng start wlan0`
```
┌──(deadboy㉿kali)-[~]
└─$ sudo airmon-ng start wlan0
[sudo] password for deadboy: 

Found 2 processes that could cause trouble.
Kill them using 'airmon-ng check kill' before putting
the card in monitor mode, they will interfere by changing channels
and sometimes putting the interface back in managed mode

    PID Name
    735 NetworkManager
    805 wpa_supplicant

PHY     Interface       Driver          Chipset

phy0    wlan0           ath9k           Qualcomm Atheros QCA9565 / AR9565 Wireless Network Adapter (rev 01)
                (mac80211 monitor mode vif enabled for [phy0]wlan0 on [phy0]wlan0mon)
                (mac80211 station mode vif disabled for [phy0]wlan0)

                                                                                                     
┌──(deadboy㉿kali)-[~]
└─$ iwconfig
lo        no wireless extensions.

eth0      no wireless extensions.

wlan0mon  IEEE 802.11  Mode:Monitor  Frequency:2.457 GHz  Tx-Power=16 dBm   
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Power Management:off
```

make note of the new assigned name i.e. `wlan0mon`

#### Step 2:
- Finding key data from wireless traffic
- `airodump-ng` --> captures and displays teh key data from broadcasting APs and any clients connected to those APs or within the vicinity.
Syntax
`airodump-ng interface from airmo-ng`

### Important terms

- **BSSID** --> MAC Address of the AP or client.
- **PWR** --> The strength of the signal
- **ENC** --> The encryption used to secure the transmission
- **#Data** --> The data throughput rate
- **CH** --> The channel the AP is operating on
- **ESSID** --> The name of the AP.
