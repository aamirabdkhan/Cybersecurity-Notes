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

# Extracting information from MySQL
- **MySQL** --> widely used database behind database-driven web applications
- Databases contain critical info about users as well as confidential info such as credit card numbers
- Other popular content managements systems (CMSs) 
	- Joomla, Drupal, and Ruby on rail all use MySQL.
## *Starting MySQL*
Start MySQL
```
service mysql start
```
Authenticate yourself by logging in: 
```sql
mysql -u root -p
```
## ***Interacting with MySQL***
- SQL is interpreted programming language for interfacing with a database.
- The database is often relational database, meaning data is stored in multiple tables that interact and each table has values in one or more columns or rows
SQL Commands:
1. `select` --> Used to retrieve data
2. `union` --> Used to combine results of two or more select operations
3. `insert` --> Used to add new data
4. `update` --> Used to modify existing data
5. `delete` --> Used to delete data
Example
```sql
select user, password from customers where users='admin';
```
- will return the values of user and password fields for any user whose user value is equal to 'admin' in the customers table
## ***Setting a MySQL password*** 
Checking users in our MySQL system
```sql
select user, host, password from mysql.user;
```
- This shows root users have no passwords
- First select a database
- To view databases
```sql
show databases;
```
- By default MySQL comes with 3 databases
- Two of which `information_schema & performance schema` are administrative databases.
- the third one, `mysql` is the non-administrative database and we'll use it.
Using `mysql` database
```sql
use mysql;
```
- The above command connects us to mysql
Setting the password
```sql
update user set password = PASSWORD("deadboy") where user = 'root';
```
## ***Accessing a remote database***
Access MySQL on localhost
```sql
mysql -u <username> -p
```
- if a hostname or Ip adress is not given it uses localhost's MySQL instance by default
Example
```sql
mysql -u root -p 192.168.1.101
```
This will connect us to the MySQL instance at the given IP address
## ***Connecting to a Database***
Snooping the around the system:
```sql
show databases;
```
We we found a database to use the database:
```sql
use <database name>
```
The `database changed` response indicates that we are now connected to the selected database
## ***Database Tables***
To find out what tables are present in the database:
```sql
show tables;
```
TO access a given table:
```sql
describe <tablename>;
```
## Examining the Data
To actually see the data in the table, we use the `SELECT` command. The `SELECT` command requires us to know the following:
- The table that holds the data you want to view.
- The columns within the table that hold the data you want to view.
SYNTAX:
```sql
SELECT columns FROM table
```
- to look at the data of all the columns we can use astrerisk *
EXAMPLE:
```sql
SELCT * FROM <tablename>
```
# PostgreSQL with Metasploit
- **PostgreSQL** another open source relational database often used in very large, internet=facing applications due to it's ability to scale easily and handle heavyworkloads 
Starting PostgreSQL start
```
service postgresql start
```
Start Metasploit
```
msfconsole
```

Setting up PostgreSQL so that it can store data from any Metasploit activity
```
msfdb init
```
Login to postgres as root
```
su postgres
```
Create a user and password:
```sql
createuser mds_user -P
```
Create database and grant permission for msf_user
```sql
createdb --owner=msf_user hackers_arise_db
```
```
exit
```

We have to connect our Metasploit to own PostgreSQL, definging the following:
- The user
- The password
- The host
```msf
db_connect msf_user:password@137.0.0.1/hacker_arise_db
```
```msf
db_status
```
