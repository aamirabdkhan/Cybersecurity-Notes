# Different types of Users
Root --> All power user
	Root user is part of the root group
Groups --> Collection of users
# Granting permissions
Three levels of permission:
1. `r` --> Permission to read. Permission to only open and view the files
2. `w` --> Permission to write. Allow users to view and edit the files
3. `x` --> Permission to execute. Allow users to execute the files (Not necessarily view or edit it.)
## Granting ownership to an individual User
`chown` --> To move ownership of a file to a different user so that they have the ability to control permissions
Syntax:
```chown
chown <user> <file>
```
## Granting ownership to a Group
`chgrp` --> To transfer ownership of a file from one group to another
Syntax:
```chgrp
chgrp <group> <file>
```
# Checking Permissions
To find out what permissions are granted to what users for a file or directory use `ls -l` command 
```
┌──(deadboy㉿kali)-[~]
└─$ ls -l                             
total 28504
1  2        3    4                  5    6            7
------------------------------------------------------------------
-rw-r--r--  1 deadboy deadboy     1171 Aug 13 15:36  16_super.py
drwxr-xr-x  6 deadboy deadboy     4096 Mar 19 00:06  BASH
drwxr-xr-x 12 deadboy deadboy     4096 Aug 12 14:55  CyberSecurity
drwxr-xr-x  2 deadboy deadboy     4096 Jul 23 18:18  Desktop
drwxr-xr-x  2 deadboy deadboy     4096 Mar  7 07:24  Documents
drwxr-xr-x  2 deadboy deadboy     4096 Jul 25 13:53  Downloads
drwxr-xr-x  4 deadboy deadboy     4096 Apr  3 12:06 'Kali Practice'
drwxr-xr-x  2 deadboy deadboy     4096 Mar  7 07:24  Music
drwxr-xr-x  2 deadboy deadboy     4096 Apr  6 11:32  Pictures
drwxr-xr-x  2 deadboy deadboy     4096 Mar  7 07:24  Public
drwxr-xr-x  2 deadboy deadboy     4096 Mar  7 07:24  Templates
drwxr-xr-x  2 deadboy deadboy     4096 Mar  7 07:24  Videos
-rw-r--r--  1 deadboy deadboy 29112320 Jul 25 13:29  backup.tar
-rw-r--r--  1 deadboy deadboy       51 Aug  6 21:49  cat
drwxr-xr-x  4 deadboy deadboy     4096 Mar  7 08:10  go
```
On each line we get information about:
1. The file type
	   `d` --> dictionary
	   dash(`-`) --> file
2. The permissions on the file for owner groups and users resp
	   owner --> First 3 set
	   Group --> middle 3 set
	   other users --> last 3 set
	   if any of the `rwx` is replaced with `-` then that permission is not granted to the respective users
1. The number of link (Topic is beyond our book)
2. The owner of the file
3. The size of the file in  bytes
4. When the file was created or modified 
5. The name of the file
# Changing Permissions
`chmod` --> This command is use to change the permissions
## Changing permissions with Decimal Notation
We are going to use binary and octal to grant permissions of file
#### Binary Representation
On and OFF switches are represented by 1 and 0 resp
#### Octal Representation
Octal --> an eight digit number system which starts with 0 and ends with 7

An octal digit represents a set of three binary digits, meaning we can represent an entire `rwx` set with one digit

## Binary and Octal representation of permissions

| **Binary** | **Octal** | **rwx** |
| ---------- | --------- | ------- |
| 000        | 0         | ---     |
| 001        | 1         | --x     |
| 010        | 2         | -w-     |
| 011        | 3         | -wx     |
| 100        | 4         | r--     |
| 101        | 5         | r-x     |
| 110        | 6         | rw-     |
| 111        | 7         | rwx     |
So if we wanted to represent all permissions for the owner, group and all users we could write 7 7 7
Example:
```
chmod 777 filename
```
## Changing permissions with UGO 
UGO --> stands for user(owner), groups and others
Syntax
-  Enter the chmod command and then the users you want to change permissions for, providing u for user, g for groups and o for others followed by one of the three operators
	1. - Remove a permission
	2. + Add a permission
	3. = sets a permission
- After the operator include the permission you want to add or remove (rwx) and then filename
```
chmod u-x filename
# The above command removes the execute permissions for the user(owner)
```

## Giving Root execute permission on a New Tool
```
chmod 766 <toolname>
```

# Setting more secure default permission with Masks
- Linux automatically assigns base permissions - usually 666 for files and 777 for directories
- You can change the default permissions allocated to files and directories created by each user with the `umask`
- `umask` --> This method represents the permissions you want to remove from the base permission on a file or directory to make them more secure
- `umask` are subtracted from the actual base permissions 
# Special Permissions
## Granting Temporary Root Permissions with SUID
SUID (set user ID) bit basically says that any user can execute the file with the permissions of the owner but those permissions don't extend beyond the use of that file

### Setting up SUID
To set the SUID bit,
- enter a 4 before the regular permissions, so a file with a resulting permission of 644 is represented as 4644 when the SUID bit is set
```
chmod 4644 filename
```
## Granting the Root User's Group Permissions SGID
SGID also granst temporary permissions but it grante the permissions of the file owner's group, rather than the file's owner
- This means that with SGID bit set someone without execute permission can execute a file if the owner belongs to the group that has permissions to execute that file
- SGID is represented by 2
```
chmod 2544 filename
```

## The outmoded Sticky Bit
The sticky bit is a permission bit that ypu can set on a directory to allow a user to delete or renmae files within that directory