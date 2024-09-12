# Using `apt` to handle Software
- `apt` --> Short form of "Advanced Packaging Tool"
- primary command --> `apt-get`

## Searching for a Package
Checking if a package is available in our repository or not:
```Searching
apt-cache search <keyword>
```
## Adding Software
By searching we got to know that the package is available in the repository:
So now we are going to install it:
```Installing
apt-get install <package-name>
```
## Removing Software
IF we  want to remove a software:
```Removing
apt-get remove <package-name>
```
but with this command Configuration files are not removed, which means you can reinstall the package in the future without reconfiguration.

If you want to remove the configuration files at the same time as the package;
``` Purging
apt-get purge <package-name>
```
## Updating Packages
- Updating simply updates the list of packages available for download from the repository
```Updating
apt-get update
```
## Upgrading Packages
 - Upgrading will upgrade the package to the latest version in the repository
```Upgrading
apt-get upgrade
```
# Adding Repositories to Your `sources.lits` File
## Repositories 
- The server that hold the software for particular distributions of Linux are known as *Repositories*
## `Sources.list`
- The repositories your system will search for software are stored in the `sources.list` and we can alter this file to define from which repositories you want to download software.
### Note
- It is recommended to not to use testing, experimental, or unstable repositories in your `sources.list` file because they can download problematic software to your system.
- They can break you system
# Using a GUI based installer
- Synaptic in the GUI based installing software to install packages
```Synaptic
apt-get install synaptic
```
# Installing software with `git`
-  Sometimes software won't be available in our repositories
- we an install those software using their github repository
```git clone
git clone <github URL>
```

