Services --> An application that runs in the background waiting for us to use it

In this chapter we'll learn how to set up a web apache server, physically spy wiith OpenSSH, access data with MySQL and store your hacking information with PostgreSQL

# Starting, Stopping and Restarting services
Basic Syntax for managing a services
```
service servicename start|stop|restart
```
Start apcahe2 service (web server or HTTP Service):
```
service apache2 start
```
Stop Apache web server:
```
service apache2 stop
```
Restart Apache Web server:
```
service apache2 restart
```
**Restarting a service** --> Usually when you make a configuration change to an application or service by altering it's plaintext configuration file, you need to restart the service to capture the new configurations

# Creating an HTTP Web Server with the Apache Web server
- Apache is found over 60% of the world's web servers.
- We can also use Apache to set up our own web servers, from which we could serve up malware via cross-site scripting (XSS) to anyone who visits your site, or we can clone a website and redirect traffic to our site via abuse of the Domain Name System.
## *Starting with Apache*
- Apache Web Server is often associated with the MySQL database and these two service are very often paired with a scripting language such as Perl or PHP to develop web applications.
- These combinations of Linux, Apache, MySQL, Perl, PHP forms a powerful and robust platform for the collectively as LAMP.
- When they are used with the Windows they're referred to as WAMP
First Step
Starting the Apache Web Server:
```
service apache2 start
```
Enter `hhtp://localhost/` in browser to bring up the web page
## *Editing the index.html file*
- Apache's default web page is at `/var/www/html/index.html` 
- use text editor to edit the `index.html` file
## *Adding some HTML*
Create out own html page:
```html
<html>
<body>

<h1> Using and Abusing Services </h1>

<p> I want to learn hacking</p>

</body>
</html>
```
## *Seeing what happens*
![](../Attachments/Pasted%20image%2020240912212301.png)
# OpenSSH and the Raspberry Spy Pi
- **SSH** --> Acronym for Secure Shell and is basically what enables us to connect securely to a terminal on a remote system --- a replacement for insecure telnet that was so common year ago.
- SSH enables us to create a access list (a list of users who can use this service), authenticate users with the encrypted passwords, and encrypt all communications 
- This reduces the chance of unwanted users using the remote terminal (due to the added authentication process) or intercepting our communication (due to encryption).
**USES**
1. System administrators often use SSH to manage remote systems.
2. Hackers often use SSH to connect to compromised remote systems.

**Setting up a remote Raspberry Pi system for spying**
Starting OpenSSH
```
service ssh start
```
- using SSH to build and control a remote spying Raspberry Pi.
- We will employ a Raspberry Pi with camera module to use as a spying device
- We'll use the Raspberry Spy Pi on the same network as our Kali System, which allow us to use private internal IP addresses.
## *Setting up the Raspberry Pi*
- Make sure the Raspbian OS is running
- Connect Raspberry Pi to a monitor, mouse and Keyboard and then connect to the internet
- Then Log in with  username ***pi*** and password ***raspberry** 

## *Building the Raspberry Spy Pi*
- Make sure the SSH is running and enabled on the Raspberry Spy Pi.
- SSH is usually off by default, to enable it, `Preferences menu > Launch Raspberry Pi Configuration > interfaces > SSH -> Enabled`
- Start SSH
```
service ssh start
```
- Attach the camera module
- Place Raspberry Pi within you home
- Obtain Ip address of Raspberry Pi
```
ifconfig
```
- Connect Kali to Raspberry Pi
- To connect to the remote Raspberry Pi via SSH from Kali system:
```
ssh pi@<IP address of Raspberry PI>
```
- Spy Pi will prompt for  a password, In this case it the default password ***raspberry***
## *Configuring the Camera*
- Start Raspberry Pi configuration tool
```
sudo raspi-config
```
- Scroll down to ***Enable Camera*** and press ENTER
- now select FINISH and press ENTER
- When Configuration tool ask to *reboot* select ***YES***  and press ENTER
Camera is enabled and is ready to spy
## *Starting to Spy*
- We'll be using `raspistill` application to take picture from our Raspberry Spy Pi
- Enter `raspistill` in the terminal to see the tool's help screen and all it's option
- To take picture and save it as a JPEG:
```
raspistill -v -o firstpicture.jpg
```
- `-v` --> gives us verbose output
- `-o` --> option to tell `raspistill` we're about to give it a filename to use
- Then we give it the filename