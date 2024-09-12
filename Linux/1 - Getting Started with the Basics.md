ab# The Linux Filesystem
**/root** --> Home directory of the all-powerful root users
**/etc** --> Generally contains Linux Configuration files -- Files that control when and how the program start up
**/home** --> User's home directory
**/mnt** --> where other filesystems are attached or mounted to the filesystem
**/media** --> where CDs and other USB medias are attached or mounted to the filesystem
**/bin** --> where application binaries (the equivalent of the executables in Microsoft windows) reside
**/lib** --> Where you'll find libraries
****
# Basic Commands in Linux
`pwd` --> shows your Present working directory
`whoami` --> Shows as whom you are logged in as
# Navigating the Linux Filesystem
### Changing directories with cd
`cd <directory>` --> takes you to the respective directory
`cd ..` -->we use .. to move up by one level (or we can say we move up to parent directory)
`cd .. ..` --> moving up by two level (same can be done for moving up three or more time as well)
`cd /` --> directly moving up to the root directory
### Listing the Contents of the directories with ls
`ls <directory>` --> lists the contents of the specific directory
`ls -l` --> (stands for long listing) used for knowing more info about the files
`ls -a` --> (stands for all) used for making hidden files visible
both the flags can be combined like `ls -la
### Getting Help
`--help` ==> double dash is used with a word like help
`-h` ==>single dash are used with single letters
`-?` ==> in some cases this can also be used
The above commands can be used for any command, applications or utility
Mostly all the application support the above three commands but if in some case one is not working then try to use other.
### Referencing Man pages
`man <content name>` -->Display more information about the commands, applications and the utilities

# Finding Stuff 
### Searching with `Locate` 
`locate <KEYWORD>` --> Goes through entire filesystem and locate every occurences of the word
- using `locate` can be overwhelming, giving too much info
- `locate` uses a database that is usually only updated once a day. it we create a file a min or an hour ago, it might not appear in the list till the next day
### Finding binaries with `whereis` 
`whereis <KEYWORD>` --> used to locate binaries of the given keyword, it is also used for locating it's source and man pages if it's available.
```
┌──(deadboy㉿kali)-[~]
└─$ whereis aircrack-ng
aircrack-ng: /usr/bin/aircrack-ng /usr/include/aircrack-ng /usr/share/man/man1/aircrack-ng.1.gz
```
### Finding Binaries in the PATH  Variable with `which`
`which <KEYWORD>` --> this command is specific as it returns the location of the binaries in the PATH Variable
```
┌──(deadboy㉿kali)-[~]
└─$ which aircrack-ng  
/usr/bin/aircrack-ng
```
### Performing more powerful searches with `find`
`find` command is the most powerful and flexible  of the searching utilites.
It is capable of beginning your search in any direction and in various no of parameters
- Basic syntax of `find` :
`find <directory> <option> <expression>`
- Example
`find / -type f -name apache` 
directory in which to start the search --> /
specify the type of the file --> here f for ordinary file
name of file I'm searching for --> apache2
Note:
- Unlike some other searches find only display exact search matches.
- if apache2 will have an extension line apache2.conf even then we won't get them in the result
- we can use wildcards to remedy these issues
- Example: `find /etc -type f --name apache2.*`
#### Quick look at Wildcards
Suppose we have a directory which stores the following files:
cat, bat, hat, what

1. ? wildcard
when we will search with the ?at we will find the file bat, cat, hat but not what because it has 2 words before at.

2.  [  , ] wildcard
when we will seach with [c, b]at we will get the file cat and bat because those are the only files which contains c and b followed by at

3. * wildcard
when using asterisk * wildcard it doesn't have any limits when searching for *at we will get all the files cat bat hat and what

### Filtering with `grep`
`grep <keyword>` --> search for the particular keyword among the files

- Piping ( | ) --> Taking output from one command an send it as input to the another command
- `ps` --> used to display information about processes running on the machine
```
┌──(deadboy㉿kali)-[~]
└─$ ps aux | grep apache2
deadboy   134079  0.0  0.0   6872  2048 pts/0    S+   21:28   0:00 grep --color=auto apache2
```
when we put `ps aux` we got so many outputs but when we filtered out the apache2 one we were left with only this one

# Modifying files and directories
## Creating Files
files can be created with various commands but the two important ones are :
1. `cat` --> usually `cat` command is used to display the contents of file but it can be used to create small files as well
2. `touch` --> another and most used command to create files are touch command it always creates a blank file
for creating bigger files always use text editors like vim
### Concatenation with cat
`cat` command is used to display content of the files
but to create a file with `cat` command we should use redirect `>`
To add or append more content into the file we use double redirect `>>`
using redirect `>` on a existing will overwrite the content of the file
*Demo* 
```
┌──(deadboy㉿kali)-[~]
└─$ cat > cat          
We are now using cat command to create files
                                                                                           
┌──(deadboy㉿kali)-[~]
└─$ cat cat  
We are now using cat command to create files
                                                                                           
┌──(deadboy㉿kali)-[~]
└─$ cat >> cat
we're now using the double redirect to append this line into the file
                                                                                           
┌──(deadboy㉿kali)-[~]
└─$ cat cat   
We are now using cat command to create files
we're now using the double redirect to append this line into the file
                                                                                           
┌──(deadboy㉿kali)-[~]
└─$ cat > cat 
Now we're overwriting into our file using redirect
                                                                                           
┌──(deadboy㉿kali)-[~]
└─$ cat cat
Now we're overwriting into our file using redirect

```
### File Creation with touch
Originally the `touch` command was created to change some of the files details, such as date it was created or modified.
But if a file doesn't exists we can use `touch` to create a file
```
┌──(deadboy㉿kali)-[~/CyberSecurity/Linux Basics for Hackers/Commands]
└─$ touch touch               
                                                                                           
┌──(deadboy㉿kali)-[~/CyberSecurity/Linux Basics for Hackers/Commands]
└─$ ls -l      
total 0
-rw-r--r-- 1 deadboy deadboy 0 Aug  6 21:54 touch
```
when we wrote `ls -l` the size of the file touch was 0 because `touch` commands creates a blank file
## Creating a directory
`mkdir` --> stands for make directory (This command is used to create new directory)
## Copying a file
`cp` --> This command is used to copy files into the new directory
`cp <oldfile name> <path were you want to copy/if you want you can give new name to the file by writing the name at the end of the path>`
## Renaming a file
Linux doesn't have a command solely for renaming a file 
to rename a we use `mv` command
`mv` command is usually used to move files from one location to the another location but it can also be used to rename the files
```
┌──(deadboy㉿kali)-[~/CyberSecurity/Linux Basics for Hackers/Commands]
└─$ touch rename
                                                                                           
┌──(deadboy㉿kali)-[~/CyberSecurity/Linux Basics for Hackers/Commands]
└─$ mv rename rename2          
```
## Removing a file
To remove a file we can use `rm` command
```
┌──(deadboy㉿kali)-[~/CyberSecurity/Linux Basics for Hackers/Commands]
└─$ rm rename2         
```
## Removing a directory
`rmdir` command is used to remove a directory
but `rmdir` won't delete a non-empty directory
it will give you a warning so won't delete something important accidentally
But if you want to remove a directory along with it's content we should use:
`rm -r <directory name>` 
```
┌──(deadboy㉿kali)-[~/CyberSecurity/Linux Basics for Hackers/Commands]
└─$ rmdir newdirectory 
rmdir: failed to remove 'newdirectory': Directory not empty
                                                                                           
┌──(deadboy㉿kali)-[~/CyberSecurity/Linux Basics for Hackers/Commands]
└─$ rm -r newdirectory 

```
