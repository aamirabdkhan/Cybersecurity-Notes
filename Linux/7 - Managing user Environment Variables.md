There are 2 types of variables - ***shell*** and ***environment*** 

**Environment Variables** --> System wide variables built into your systems and interface that control the way your system looks, acts and feels to the user, and they are inherited by any child shells or processes.

**Shell Variables** --> typically listed in lowercase and are only valid in the shell they are set in.

**Variables**
- SImply strings in key-value pairs
- each will look like `key=value` 
- In cases where there are multiple values, they will look like `key=value1:value2` 
# Viewing and modifying Environment Variables
`env` --> view all your default environment variables
```env
┌──(deadboy㉿kali)-[~]
└─$ env
COLORFGBG=15;0
COLORTERM=truecolor
COMMAND_NOT_FOUND_INSTALL_PROMPT=1
DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus
DESKTOP_SESSION=lightdm-xsession
DISPLAY=:0.0
```
- always uppercase, such as `HOME, PATH, SHELL` 
## Viewing all Environment Variables
To view all environment variables, including shell variables, local variables, and shell functions such as any user-defined variables and command aliases, use the `set` command
This command will list all environement variables unique to your system, which in most cases will give you an output so long you won't be able to view it all.
```set
┌──(deadboy㉿kali)-[~]
└─$ set | more                                                     
'!'=0
'#'=0
'$'=11544
'*'=(  )
-=3569JXghiks
0=/usr/bin/zsh
'?'=0
@=(  )
ARGC=0
CDPATH=''
COLORFGBG='15;0'
COLORTERM=truecolor
COLUMNS=124
COMMAND_NOT_FOUND_INSTALL_PROMPT=1
CPUTYPE=x86_64
```
 - In this way the list of variables will fill up one screen. line by line and then stop
	 - Press `ENTER` to view the next line
	 - Press `q` to exit
## Filtering for Particular Variables
```
┌──(deadboy㉿kali)-[~]
└─$ set | grep HISTSIZE
HISTSIZE=1000
```
`HISTSIZE` --> This variable contains the maximum number of commands your command history file will store
- These are the commands you've previously and can be recalled with `up and down` arrow
- `HISTSIZE` doesn't store the commands themselves, just the number of them that can be stored
- The above example indicates the terminal will store your last 1000 commands by default
## Changing Variable values for a Session
```
┌──(deadboy㉿kali)-[~]
└─$ HISTSIZE=0
```
## Making variable Value changes permanent
- When we change an environment variable that change only occurs in that particular environment. In this case the environment is the bash shell session
- This means that when you close the terminal, any changes you made are lost
`export` --> This command is user to make the permanent changes
This command will `export` the new value from your current environment (the bash shell) to the rest of the system, making it available in very environment until you change and export it again

Variables are strings so before making any changes store the previous values in a file
```
┌──(deadboy㉿kali)-[~]
└─$ echo $HISTSIZE> ~/valueofHISTSIZE.txt
```

IF you want to be more cautious and create a txt file with all the current settings, you can save the output of the `set` command to a text file with a command like this one:
```
┌──(deadboy㉿kali)-[~]
└─$ set> ~/valueofALLon01012017.txt    
```
Making the change permanent by entering the`export` and then the name of the variable you changed 
```
┌──(deadboy㉿kali)-[~]
└─$ HISTSIZE=0
                                                                                                                            
┌──(deadboy㉿kali)-[~]
└─$ export HISTSIZE
```
Now the `HISTSIZE` variable will still be set to 0 when you leave this environment and enter another environment.
To reset the variable
```
┌──(deadboy㉿kali)-[~]
└─$ HISTSIZE=1000
                                                                                                                            
┌──(deadboy㉿kali)-[~]
└─$ export HISTSIZE
```
# Changing your Shell Prompt
We can change the name in the default shell program by setting the value for the `PS1` variable
The `PS1` variable has a set of placeholders for info you wan to display in the prompt, including
- `\u` --> The name of the current user
- `\h` --> The hostname
- `\w` --> The base name of the current working directory
**Changing the prompt in the terminal**
```
┌──(deadboy㉿kali)-[~]
└─$ PS1="Noob: #"
                                                                                                                            
Noob: #pwd
/home/deadboy
```
- Now everytime we user this terminal we be reminded that we are "Noob"
- to save the changes to be permanent just use the `export PS1` 

**Making our terminal look like Windows `cmd` prompt**
`\w` is not working in my command prompt look for something on google
# Changing your `PATH`
`PATH` variables --> Controls where in your system your shell will look for commands you enter such as `grep, ls, echo` etc.
- Most commands are located in `sbin` or `bin` directory like `usr/local/bin` or `usr/local/sbin`
- If the bash shell doesn't find commands in the `PATH` variables then it'll say command does not found, even if the command exist in some another folder
```
aiktc@aiktc:~$ echo $PATH
/usr/lib/jvm/java-8-openjdk-amd64/bin:/home/aiktc/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/home/aiktc//hadoop-2.7.3/bin:/bin:/bin
```
- These are the directories where your terminal will search for any commands
- Each directory is separated by a colon (:)
- Don't forget to put `$` before the `PATH` . When we put `$` before a variable, we are asking the system for the content of the variable
## Adding to the `PATH` variable
Suppose we downloaded a *newhackingtool* in the `root/newhackingtool` directory, we could only use commands from this tool whenever we are in the `root/newhackingtool` directory
- To be able to use *newhackingtool* without navigating to it's directory we have to add `root/newhackingtool` directory to the `PATH` variable
- Syntax
```
kali> PATH=$PATH:/root/newhackingtool
```
- we can check the `PATH` after executing this command we will see the above directory has been appended and now we can use the *newhackingtool* 's commands from anywhere
NOTE:
- Adding you frequent use directories can be useful but remember not to add many directories as the `PATH` variable searches through every directory, adding too many directories will slow down your terminal
## How not to add to the `PATH` variable
Don't write the directory adding command in the following way
```
kali> PATH=root/newhackingtool
```
if you use this command, your `PATH` variable will only contain the `root/newhackingtool` file and not the main system binaries directory such as `/bin or /sbin` and others which holds other commands. 
If we do this then our system commands such `ls, cd, echo` etc will not work and we'll receive command does not found error.
Remember we want to append to the `PATH` variable and not replace it.
If you are in doubt save the orignal content of the `PATH` variable to a new file.

# Creating a user defined variable
- Creating our variable can be useful when  you are doing some more advanced shell scripting or find you're using long command that you are tired of typing over and over
Syntax for creating new variable
`name of your variable` followed by the assignment symbol (`=`) and then `the value to put in the variable`
```
┌──(deadboy㉿kali)-[~]
└─$ MYNEWVARIABLE="I am Noob"
```
To see the value in that variable use the `echo` command and the `$` content symbol with the variable name
```
┌──(deadboy㉿kali)-[~]
└─$ echo $MYNEWVARIABLE 
I am Noob
```
- Just like our system environment variables, user-defined variables must be exported to persist to new sessions.
- If you want to delete any variable use the `unset` command
- Always think before deleting a variable because your system will work different afterwards.
```
┌──(deadboy㉿kali)-[~]
└─$ unset MYNEWVARIABLE 

┌──(deadboy㉿kali)-[~]
└─$ echo $MYNEWVARIABLE

┌──(deadboy㉿kali)-[~]
└─$ 
```
-  When you `unset` `MYNEWVARIABLE` you delete the variable along with it's value. If you echo on that same variable, Linux will return a blank line
