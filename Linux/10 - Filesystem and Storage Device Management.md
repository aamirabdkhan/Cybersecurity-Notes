Linux follows a tree structure with `/` at the top

# The Device Directory `/dev` 
-  Linux has a special directory that contains files representing each attached device..
-  `sda1, sda2, sda3` are the hard drive and it's partition
- `sdb. sdb1` is the USB flash drive and it's partition
## How Linux Represents Storage Devices
- Linux used logical labels for drives that are then mounted on the filesystem.
- These labels will vary depending on where the drives are mounted, meaning same hard drive might have different labels at different times, depending on where and when it's mounted
- Previously Floppy disk were represented as `fda` and hard drive as `hda` 
- The newer SerialATA (SATA) Interface drives and Small Computer System Interface (SCSI) hard drives are represented as `sda` 
Device Naming System
**Device File Description**

| `sda`     | First SATA hard drive      |
| --------- | -------------------------- |
| **`sdb`** | **Second SATA hard drive** |
| **`sdc`** | **Third SATA hard drive**  |
| **`sdd`** | **Fourth SATA hard drive** |
## Drive Parititons
**Partitions Description**

| **`sda1`** | First partition (1) on the first (a) SATA drive      |
| ---------- | ---------------------------------------------------- |
| **`sda2`** | **Second partition (2) on the first (a) SATA drive** |
and so on
`fdisk -l` --> View partitions on your Linux System to see which ones you have and how much capacity is available on each
### Files Types
1. `HPFS` --> High Performance File System
2. `NTFS` --> New Technology File System
3. `exFAT` --> Extended File Allocation Table
These are not native to Linux, but rather to macOS and Windows Systems.
- Filesystem might indicate what kind of machine the drive was formatted on.
- New version of windows use NTFS filesystem, whereas older windows system use File Allocation Table (FAT) systems.
- Linux uses a number of different type of filesystems, but the most common are ext2, ext3, and ext4. These are all iteration of the ext (or extended) filesystem, with ext4 being the latest
## Character and Block Devices
```
┌──(deadboy㉿kali)-[/dev]
└─$ ls -l
total 0
crw-r--r--  1 root root     10,   235 Sep 11 09:46 autofs
drwxr-xr-x  2 root root           260 Sep 11 10:07 block
drwxr-xr-x  2 root root           100 Sep 11 10:06 bsg
crw-------  1 root root     10,   234 Sep 11 09:46 btrfs-control
drwxr-xr-x  3 root root            60 Sep 11 09:46 bus
lrwxrwxrwx  1 root root             3 Sep 11 09:47 cdrom -> sr0
drwxr-xr-x  2 root root          3840 Sep 11 10:07 char
crw--w----  1 root tty       5,     1 Sep 11 09:47 console
lrwxrwxrwx  1 root root            11 Sep 11 09:46 core -> /proc/kcore
crw-------  1 root root     10,   125 Sep 11 09:46 cpu_dma_latency
crw-------  1 root root     10,   203 Sep 11 09:46 cuse
drwxr-xr-x  9 root root           180 Sep 11 09:46 disk
drwxr-xr-x  3 root root           100 Sep 11 09:46 dri
crw-------  1 root root    243,     0 Sep 11 09:46 drm_dp_aux0
```
The following letters represent the two ways that devices transfer data in and out
1. `c` --> stands for character and these devices are known as character devices.
   External devices that interact with the system by sending and receiving data character by character, such as mice or keyboards, are character devices
2. `b` --> stands for block devices. 
   They communicate in blocks of data (multiple bytes at a time and include devices like hard drives and DVD drives).

## List block devices and information with `lsblk`
`lsblk` --> stands for list block
Lists some basic info about each block devices listed in `/dev`
The result is similar to the output of `fdisk -l` but it will also display devices with multiple partitions in a kind of tree, showing each device with it's partitions as branches
```
┌──(deadboy㉿kali)-[/dev]
└─$ lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINTS
sda      8:0    0 931.5G  0 disk 
├─sda1   8:1    0   100M  0 part /boot/efi
├─sda2   8:2    0    16M  0 part 
├─sda3   8:3    0 230.9G  0 part 
├─sda4   8:4    0   2.8G  0 part 
├─sda5   8:5    0   500M  0 part 
├─sda6   8:6    0   350G  0 part 
├─sda7   8:7    0 300.6G  0 part /
└─sda8   8:8    0  46.6G  0 part [SWAP]
sdb      8:16   0 111.8G  0 disk 
sr0     11:0    1   1.2G  0 rom  

# We see sda with it's branches sda1, sda2, etc
```

does not require root privileges to run

`MOUNTPOINTS` --> This is the partition at which the drive was attached to the filesystem
# Mounting and Unmounting
The two main mount points in LINUX are `/mnt` and `/media` 
As a general rule internal hard drives are mounted at `/mnt` and external USB devices are mounted at `/media` 
## Mounting Storage devices yourself
To mount a drive
- use `mount` command
- The mount point for the device should be an empty directory
	- If we mount a device in a directory that has subdirectories and files the mounted device will cover the contents of the directory, making them invisble and unavailable
`mount /dev/sdb1/mnt` --> internal storage
`mount /dev/sdc1/media` --> external storage

The filesystems that are mounted on a system are kept in a file at `/etc/fstab` ( short for filesystem table) , which is read by the system at every bootup
## Unmounting with `umount`
Eject is the another word for Unmount

Unmount a second hard drive:
- use `umount` command
- followed by the file entry of the device in the `/dev` directory such as `/dev/sdb`
`umount /dev/sdb`

You cannot unmount a device that is busy so if the system is reading or writing to the device you will just receive an error

# Monitoring Filesystems
## Getting Information on Mounted Disks
`df` --> stand for disk free will provide us with basic informationn on any hard disks or mounted devices, such as CD, DVD and flash drives including how much space is being used and how much is available

```
┌──(deadboy㉿kali)-[/dev]
└─$ df sdb
Filesystem     1K-blocks  Used Available Use% Mounted on
udev             1927084     0   1927084   0% /dev
```
## Checking for Errors
`fsck` --> Filesystem check, checks the filesystem for errors and repairs the damage, it possible or else puts the bad area into a bad blocks to mark it as bad.

It' s important to note that you must unmount the drive before running the filesystem check.
if you fail to do so you will receive an error
`umount <device>`
`fsck -p <device>`
56