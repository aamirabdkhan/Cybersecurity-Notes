 # What is Compressing?
Compression --> makes data smaller, thereby requiring less storage capacity and making the data easier to transmit.

- Lossy Compression --> Very effective in reducing the size of the files, but the integrity of the information is lost. In other words, files after compression is not exactly as the  orignal.
	- works great for graphics, video and audio files where small difference is hardly noticeable --- mp3, mp4, png, jpg are all lossy compression algo
# Tarring files together
`tar` --> stands for tape archive, a reference to the prehistoric days of computing when systems used tape to store data..
- The `tar` command creates a single file from many files , which is referred to as an **archive, tar file or tarball** 
SYNTAX
`tar -cvf <new name>.tar <file1> <file2> <file3> ....` 
`c` --> create
`v` --> stand for verbose (optional in this case) lists the files that tar is dealing with
`f` --> write to the following file. will also work for reading from files
`t` --> content list

Displaying the content of the tar file without extracting
`tar -tvf <file>.tar`

Extracting the content from the tar file
`tar -xvf <filename>.tar`

Extracting files silently meaning without showing any output
`tar -xf <filename>.tar`

# Compressing Files
With tar we have archived the file but it's output is bigger than the original files combined
Linux have several tools for compressing
- `gzip` - which uses extension `.tar.gz` or `.tgz`
- `bzip2` - which uses extension `.tar.bz2`
- `compress` - which uses extension `.tar.z`
They all use different compression algos and have different compression ratios
In general
- `compress` is the fastest but resultant files are larger
- `bzip2` is the slowest but the resultant files are the smallest
- `gzip` falls somewhere in the between
## Compressing with `gzip`
`gzip` stands for GNU zip
`gunzip` stands for GNU unzip

Compressing a files using gzip:
`gzip filename.*`
- we used the `*` wildcard extension, this tells Linux that the command should apply to any file that begins with filename with any file extension
- after the command we can see with long listing that the has been replaced by `filename.tar.gz`

Decompressing the same files:
`gunzip filename.*`

`gzip` can also be used to extract `.zip`  files

## Compressing with `bzip2`
- works similarly like `gzip` but has better compression ratios meaning that the resultant file will be even smaller

Compressing the file
`bzip2 filename.*`
- extension is now `.tar.bz2`

Decompressing the file:
`bunzip2 filename.*`

## Compressing with `compress`
-  least commonly used but easy to remember

Compressing the file:
`compress filename.*`
- extension is now `.tar.Z` (with an uppercase Z)

Decompress the file:
`uncompress filename.*`
# Creating bit-by-bit or Physical copies of storage devices
`dd` --> This command makes a bit-by-bit copy of a file, a filesystem or even an entire hard drive
- This means that even deleted files are copied
- One should not use it for day-to-day task for copying files and storage files because it is too slow

Basic Syntax:
`dd if=inputfile of=outputfile`

Example --> Making a flash copy of hardrive `sdb` 
`dd if=/dev/sdb of=/root/flashcopy`

breaking down the whole command
- `dd` --> Physical copy command
- `if` --> designates your input file
- `/dev/sdb` --> representing your flash drive in the `/dev` directory
- `of` --> designates your output file
- `/root/flashcopy` --> name of the file you want to copy the physical copy to

- There are numerous options available to use with the `dd` command
- most useful ones are:
	- `noerror` --> Continues to copy even if errors are encountered
	- `bs` (block size) --> allows you to determine the block size (number of bytes  read/written per block) of the data being copied. 
		- By default it is set to 512 bytes but it can be changed to speed up the process
		- Typically this would be set to the sector size of the device most often 4KB(4096 bytes) 

Command with the above options
`dd if=/dev/sdb of=/root/flashcopy bs=4096 conv:noerror`
