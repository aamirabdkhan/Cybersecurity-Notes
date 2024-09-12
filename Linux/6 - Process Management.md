# Viewing Processes
`ps` --> Primary tool for viewing process
```ps
┌──(deadboy㉿kali)-[~]
└─$ ps                   
    PID TTY          TIME CMD
 119540 pts/1    00:00:00 zsh
 119566 pts/1    00:00:00 ps
```
- The Linux kernel, the inner core of the OS that controls nearly everything assigns a unique *process ID* (PID) to each process sequentially as the processes are created.
- When working with processes you often need to specify their PID
- `ps` command doesn't really provide you with much info
`ps aux` --> show all processes running on the system for all users
```aux
┌──(deadboy㉿kali)-[~]
└─$ ps aux               
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.3  22800 13160 ?        Ss   18:23   0:02 /sbin/init splash
root           2  0.0  0.0      0     0 ?        S    18:23   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        S    18:23   0:00 [pool_workqueue_release]
root           4  0.0  0.0      0     0 ?        I<   18:23   0:00 [kworker/R-rcu_g]
root           5  0.0  0.0      0     0 ?        I<   18:23   0:00 [kworker/R-rcu_p]
.
.
.
.
.
.
snip
```
- `USER` -> user who invoked the process
- `PID` -> Process ID
- `%CPU` -> percent of CPU this process is using
- `%MEM` -> percent of memory this process is using
- `COMMAND` ->name of the command that started the process 
## Filtering by process name
`ps aux | grep <process name>`

## Finding the Greediest Processes with top
`top` --> Displays the processes ordered by resources used, starting with the largest
- `top` refreshes list dynamically - by default every 10 seconds
- While `top` is running, pressing H or ? key will bring up a list of interactive commands, pressing Q will quit the top

```top
┌──(deadboy㉿kali)-[~]
└─$ top                                                  
top - 00:07:14 up 9 min,  1 user,  load average: 0.72, 0.61, 0.40
Tasks: 166 total,   1 running, 165 sleeping,   0 stopped,   0 zombie
%Cpu(s):  4.9 us,  2.4 sy,  0.0 ni, 92.7 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st 
MiB Mem :   3846.1 total,   1874.1 free,   1333.1 used,   1071.0 buff/cache     
MiB Swap:  47694.0 total,  47694.0 free,      0.0 used.   2513.1 avail Mem 

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                                              
    834 root      20   0  734424 112728  62984 S   9.5   2.9   0:16.28 Xorg                                                 
   3497 deadboy   20   0  532916 101504  84736 S   4.8   2.6   0:01.45 qterminal                                            
      1 root      20   0   22812  13424   9712 S   0.0   0.3   0:01.51 systemd                                              
      2 root      20   0       0      0      0 S   0.0   0.0   0:00.00 kthreadd                                             
      3 root      20   0       0      0      0 S   0.0   0.0   0:00.00 pool_workqueue_release                               
      4 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/R-rcu_g                                      
      5 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/R-rcu_p                                      
      6 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/R-slub_                                      
.
.
.
.
.
.
.
```
# Managing Process
Managing multiple process
## Changing Process priotity with `nice`
`nice` --> used to influence the priority of a process to the kernel
- we can use `nice` to suggest that a process should be elevated in priority
- values of `nice` ranges from -20 to +19, with zero being default value
- high nice value translate to low priority and low `nice` value translates to high value
- When a process is started it inherits the nice value of it's parents
- The owner can lower the priority but cannot increase it's priority
- the superuser or root user can arbitrarily set the `nice` value to whatever they please

-20                                           0                                          +19
most likely                            Default                                  Least Likely to
receive priority                    `nice` value                            receive priority

- When we start a process you can set the priority level with the `nice` command and then alter the priority after the process has started running with the `renice` command.
- The Syntax for these two commands is slightly different and can be confusing.
- The `nice` command requires that you increment the `nice` value, whereas the `renice` command wants an absolute value for niceness/
### Setting the priority when starting a process
`nice -n -10 <process name>` --> increasing the priority, means allocating more resources
`nice -n 10 <process name>`  --> decreasing the priority 
### Changing the priority of a running process with `renice`
- `renice` command takes absolute values between -20 to +19 and sets the priority to that particular level
- `renice` requires PID of the process you are targeting rather than the name
- only the root user can `renice` a process to a negative value to give it higher priority, but any user can be nice and reduce the priority with `renice`
- We can also use the `top` command to change the `nice` value. With the utility running simply press `R` key and then supply the PID and the `nice` value
## Killing Processes
**Zombie Process** --> At times, a process will consume way too many system resources, exhibit unusual behaviour or worst freeze. 

`kill` --> stop a process to consume unwanted resources
-  has 64 different signals
- Syntax
  `kill signal PID` --> where signal switch is optional. If you don't provide a signal flag it defaults to `SIGTERM` 
### List of common kill signals

| **SIgnal Name** | **Number for Option** | **Description**                                                                                                                                                 |
| --------------- | --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SIGHUP`        | 1                     | known as `Hangup HUP` signal. It stops the designated process and restarts it with the same PID                                                                 |
| `SIGINT`        | 2                     | This is the `Interrupt INT` signal. It is a weak kill signal that isn't guaranteed to work, but it works most of the time.                                      |
| `SIGQUIT`       | 3                     | Known as `core dump` . It terminates the process and saves this info in memory, then it saves this info in the current working directory to a file named `core` |
| `SIGTERM`       | 15                    | This is the `Termination TERM` signal. It is the kill command's default kill signal.                                                                            |
| `SIGKILL`       | 9                     | This is the absolute KILL signal. It forces the process to stop by sending the process's resources to a special device, /dev/null                               |
## Running Processes in the background
To start a command in the background, just append a ampersand (&) to the end of the command
`<Command> &`
## Moving Processes to the foreground
- If we want to move the process running in the background to move to the foreground, use the `fg` command.
- The `fg` command requires a PID of the process.
- if you don't know the PID you can use the `ps` command
`fg <PID>`
# Scheduling Process
`at` --> This command is a daemon -- a background process -- useful to scheduling a job to run once at some point in the future
`crond` --> This command is more suited for scheduling tasks to occur every day, week or month (WE'LL COVER MORE ABOUT THIS COMMAND IN [[16 - Automating tasks with Job Scheduling]])
Syntax:
`at <time to execute the process>`
### Most common `at` time format
![[Pasted image 20240831013038.png]]
- When you enter the `at` daemon with the specified rime, `at` goes into interactive mode and you are greeted with an `at >` prompt. Here is where you enter the command you want to execute at the specified time
```
┌──(deadboy㉿kali)-[~]
└─$ at 7:20                  
warning: commands will be executed using /bin/sh
at Sat Aug 31 07:20:00 2024
at> pwd
```