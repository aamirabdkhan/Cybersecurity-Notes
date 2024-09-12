# A Crash Course in Bash
**Shell** --> An interface between the user and the OS that enables you to manipulate files and run commands, utilities, programs, and much more
**Different types of shell**
1. Korn Shell
2. Z shell
3. C shell
4. Bourne-again Shell (Bash)
# First Script: "Hello, Hackers-Arise"
First you need to tell the text editor which interpreter we want to use for the script.
To do this, enter `shebang` which is a combination of a hash-mark and an exclamation mark
`#!`
You then follow the shebang with the `/bin/bash` to indicate that you want the OS to use the bash shell interpreter
`#! /bin/bash`
Enter the commands
`echo` --> tells the system to simply repeat (or echo) back to your monitor whatever follows the command.
```bash
#! /bin/bash

# This is my first bash script

echo "Hello, DeadBoy!"
```
- In bash we use hash-mark (#) to comment a line.
## Setting Execute Permissions
- By default the bash script is not executable even by the Owner.
- We can check the permissions of the files in the current directory by using the `ls -l` 
```terminal
┌──(deadboy㉿kali)-[~/CyberSecurity/Linux Basics for Hackers/Commands]
└─$ ls -l
total 32
-rw-r--r-- 1 deadboy deadboy   30 Aug  6 21:58 cp
-rw-r--r-- 1 deadboy deadboy    0 Aug  6 22:09 example
-rw-r--r-- 1 deadboy deadboy   68 Sep  2 20:32 first
```
our file name is `first` and you see it the read`r` and write `w` permissions but not executable `e` 
- To give the executable permissions to the owner, the group and all the other execute permissions, use the following command:
`chmod 755 first`
```
┌──(deadboy㉿kali)-[~/CyberSecurity/Linux Basics for Hackers/Commands]
└─$ ls -l 
total 32
-rw-r--r-- 1 deadboy deadboy   30 Aug  6 21:58 cp
-rw-r--r-- 1 deadboy deadboy    0 Aug  6 22:09 example
-rwxr-xr-x 1 deadboy deadboy   68 Sep  2 20:32 first
```
Now we can see we have the execute permissions
## Running the bash file
To run the script enter the following:
`./<filename>`
- `./` before the filename tells the system that we want to execute this script in the file from the current directory.
- It also tells the system that if there is another file in another directory named the same please ignore it  and only run the file from the current directory
## Adding the functionality with Variables and User Input
- Always open the file `shebang` --> `#! /bin/bash`
- use `echo` to display the content on the terminal to the user
- we use `read` followed by the a word which will act as our variable here we too `name` & `chapter` as our variable
- To display the content of the variable we must precede it with a `$` symbol

```bash
#! /bin/bash

# Second script.
# in this script take input from the user and store it in the variable

# Taking user input
echo "What is your name?"
read name # variable

echo "What chapter are you on?"
read chapter

#Display the stored value of the variable
echo "Welcome" $name "to Chapter" $chapter "of Linux"  
```
NOTE: Don't forget to give yourself the execute permissions every time you create a new file

# Our very first hacker script: Scan for Open ports
nmap --> Used to probe  a system to see whether it is connected to the network and finds out what ports are open
- With open ports we can surmise what services are running on the target system
- Simplest form: syntax for running an nmap scan looks like:
  `nmap <type of scan><target IP><optionally, target port>`
- TCP Connect scan is the simplest and most reliable nmap scan.
  Designated with `-sT` switch 
- scanning following IP with the TCP scan
  `nmap -sT 192.168.181.1`
- Taking a step further, Perform a TCP scan of address 192.168.181.1 looking to see whether port 3306 (the default port for MySQL) was open
  `nmap -sT 192.168.181.1 -p 3306`
- `-p` designates the port you want to scan for
## Simple Scanner
- Before going big will start with small
- A script to scan for port 3306 on a local area network
```bash
#! /bin/bash

# This script is designed to find hosts with MySQL installed

nmap -sT 192.168.0.13 -p 3305 >/dev/null -oG MySQLscan

cat MySQL | grep open > MySQLscan2

cat MySQLscan2
```

- `nmap -sT 192.168.0.13 -p 3305` --> use the `nmap` command to request TCP on our LAN looking for 3306
- `>/dev/null ` --> To stay healthy we also send the standard nmap output that would easily appear on the screen to a special place in Linux wher it would disappear
- `-oG MySQLscan` --> WE then send the output of the scan to a file name MySQLscan in a grep-able format, meaning a format that grep can work on
- `cat MySQL | grep open > MySQLscan2` --> This line displays the MySQLscan file we stored the output in and then pipes that output to `grep` to filter for lines that include the keywords `open` . Then we put those lines into a file name MySQLscan2
## Improving the MySQL scanner
### Adding prompts and variable to our scanner script
```bash
#! /bin/bash

echo "Enter the starting IP Address: "
read FirstIP

echo "Enter the last octet of the last IP Address: "
read LastOctetIP

echo "Enter the port number you want to scan for: "
read port

nmap -sT $FirstIP-$LastOctetIP -p $port >/dev/null -oG MySQLscan

cat MySQLscan | grep open > MySQLscan2

cat MySQLscan2
```
- `nmap -sT $FirstIP-$LastOctetIP` --> The first thing we did was to replace the specified subnet with an IP address range.
- we used variable `FirstIP` and `LastOctetIP` to create the range as well as a variable named `port` for the port number.
  (The last octet is the last group of digits after the third period in the IP Address. In the IP address 192.168.1.101, the last octet is 101)
# Common Built-in Bash Commands
![[Pasted image 20240909113800.png]]
![[Pasted image 20240909113830.png]]
