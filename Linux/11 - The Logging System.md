# The rsyslog Logging Daemon
- Linux uses daemon called `syslogd` to automatically log events on your computer.
	- There are several variations of `syslog` including `rsyslog` and `syslong-ng` used on different distributions of Linux.
	- Kali Linux is based on Debian and Debian comes with `rsyslog`

Searching all files related to `rsyslog`
```
┌──(deadboy㉿kali)-[~]
└─$ locate rsyslog
/etc/rsyslog.conf
/etc/rsyslog.d
/etc/logcheck/ignore.d.server/rsyslog
/etc/logrotate.d/rsyslog
/etc/systemd/system/multi-user.target.wants/rsyslog.service
/usr/lib/rsyslog
.
.
.
```
We are going to examine `rsyslog.conf`
## The `rsyslog` Configuration file
- located in `/etc` directory
`leafpad /etc/rsyslog.conf`
- Comes well documented with numerous comments explaining it's use.
- at line 50 rules section starts
- That is were we can set the rules for what your Linux system will automatically log for you
```
###############
#### RULES ####
###############

#
# Log anything besides private authentication messages to a single log file
#
*.*;auth,authpriv.none		-/var/log/syslog

#
# Log commonly used facilities to their own log file
#
auth,authpriv.*			/var/log/auth.log
cron.*				-/var/log/cron.log
kern.*				-/var/log/kern.log
mail.*				-/var/log/mail.log
user.*				-/var/log/user.log

#
# Emergencies are sent to everybody logged in.
#
*.emerg				:omusrmsg:*
```
## The `rsyslog` logging rules
- The rules sections allows us to find out what is being logged and where those logs are written so we can delete or obscure them
- Each line is separate logging rule that says what messages are logged and wher they're logged to.
`facility.priority             action`
--> The `facility` keyword references the program. such as mail, kerna, or lpr whose messages are being logged.
--> The `priority` keyword determines what kind of messages to log for that program.
--> The `action` keyword references the location where the log will be sent.
### Facility Keyword
- Let's look at each section more closely, beginning with `facility` keyword. which refers to whatever software is generating the log, whether that's the kernel, the mail system in our configuration file rules.
List of valid codes that can be used in place of the `facility` keyword
 in configuration file
 1. `auth/authpriv` --> Security / Authorization messages
 2. `cron` --> Clock daemon
 3. `daemon` --> Other daemons
 4. `kern` --> Kernel messages
 5. `lgr` --> Printing System
 6. `mail` --> Mail system
 7. `user` --> Generic user-level messages
An asterisk( * ) in place of a word refers to all facilities. You can select more than one facility by listing them separated by a comma.

### Priority Keyword
- Tells the system what kinds of messages to log. 
- Codes are listed from lowest priority - `debug` to the highest priority `panic`
- If the priority is * * messages of all priorities are logged.
- When you specify a priority, messages or that priority and higher are logged
Full list of valid codes for priority:
1. debug
2. info
3. notice
4. warning
5. warn
6. error
7. err
8. crit
9. alert
10. emerg
11. panic
The codes warning, warn, error, err, emrg, and panic have all been deprecated and should not be used.

### Action Keyword
- Usually filename or location where the logs should be sent.
- Generally log files are sent to the `/var/log` directory with a filename that describes the facility that generated the, such as auth

### Example
`mail.* /var/log/mail`
This example will log mail events of all priorities to /var/log/mail

`*.emerg *`
Log all events of the emergency (emerg) priority to all logged on users


With these rules, the hacker can determine where the log files are located, change the priorities, or even disable specific logging rules.

# Automatically cleaning up logs with `logrotate`
`logrotate` -- use to determine the balance between these opposing requirements by rotating your logs
- **Log Rotation** --> The process of regularly archiving log files by moving then to some other location, leaving you with a fresh log file. That archived location will then get cleaned up after a specified period of time.
- Your system is already rotating log files using a `cron` job that employs the `logrotate` utility.
- We can configure the `logrotate` utility to choose the regularity of your log rotation with the `/etc/logrotate.conf` text file.
```
# see "man logrotate" for details

# global options do not affect preceding include directives

# rotate log files weekly
weekly

# keep 4 weeks worth of backlogs
rotate 4

# create new (empty) log files after rotating old ones
create

# use date as a suffix of the rotated file
#dateext

# uncomment this if you want your log files compressed
#compress

# packages drop log rotation information into this directory
include /etc/logrotate.d

# system-specific logs may also be configured here.
```
`logrotate.conf` file
# Remaining Stealthy
## Removing Evidence
`shred` -->Overwrite the specified FILE(s) repeatedly, in order to make it harder
for even very expensive hardware probing to recover the data.
Syntax: `shred <File>`
 - By default `shred` overwrites four times. (The more time the files are overwritten the harder it is to recover)
 - Two useful switch to use with `shred`
	 1. `-f` --> Changes the permissions on the files to allow overwriting if a permission change is necessary.
	 2. `-n` --> let you choose how many times to overwrite the files.
Syntax: `shred -f -n 10 <file>`

## Disabling Logging
- To disable logging, the hacker could simple stop the `rsyslog` daemon. Stopping any service in Linux uses the same syntax, shown here:
`service servicename start|stop|restart`

- To stop the logging daemon, following command can be used:
`kali >service rsyslog stop`

- Now Linux will stop generating any log files until the service is restarted, enabling you to operate without leaving behind any evidence in the log files.
