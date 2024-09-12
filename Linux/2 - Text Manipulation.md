# Viewing Files
As mentioned in Chp1 we used `cat` command to display contents of the file but when it comes to large files it's not the most convinient command to display contents of those files as it will every thing of that file.
Even if the files contain 10000 files

## Taking the Head
`head` --> This command is used to view the first few lines of a file
- by default it displays first 10 lines of a file 
- but we can view more or less with the help of the dash (-)
Syntax:
```
head -n <filename>
# here n is the number of lines you want to view
```
Demo:
```┌──(deadboy㉿kali)-[/etc/snort]
└─$ head community-sid-msg.map 
# Copyright 2005 Sourcefire, Inc. All Rights Reserved.
# This file is licensed under the GNU General Public License.
# Please see the file LICENSE in this directory for more details.
# Id SID -> MSG map

100000100 || COMMUNITY EXPLOIT Windows Acrobat Reader Activex Overflow Flowbit || cve,2004-0629 || bugtraq,10947
100000101 || COMMUNITY EXPLOIT Windows Acrobat Reader Activex Overflow Exploit || cve,2004-0629 || bugtraq,10947
100000102 || COMMUNITY GAME Halocon Denial of Service Empty UDP Packet || bugtraq,12281
100000103 || COMMUNITY GAME Breed Game Server Denial of Service Empty UDP Packet || bugtraq,12262
100000104 || COMMUNITY GAME Amp II 3D Game Server Denial of Service Empty UDP Packet || bugtraq,12192
                                                                                           
┌──(deadboy㉿kali)-[/etc/snort]
└─$ head -3 community-sid-msg.map 
# Copyright 2005 Sourcefire, Inc. All Rights Reserved.
# This file is licensed under the GNU General Public License.
# Please see the file LICENSE in this directory for more details.
```
## Grabbing the tail
`tail` --> This command works similar to the head command but this command display the last few lines of a line
- by default it displays the last 10 of the file
- but we can view more or less with the help of the dash (-)
Syntax:
```
tail -n <filename>
# here n is the number of lines you want to view
```
Demo:
```
┌──(deadboy㉿kali)-[/etc/snort]
└─$ tail community-sid-msg.map 
100000925 || COMMUNITY-WEB-PHP ADP Forum Attempted Password Recon || url,www.milw0rm.com/exploits/3053
100000926 || COMMUNITY-WEB-PHP EasyNews PRO News Attempted Password Recon || url,www.milw0rm.com/exploits/3039
100000927 || COMMUNITY MISC Microsoft Messenger phishing attempt - corrupted registry || url,www.microsoft.com/windowsxp/using/security/learnmore/stopspam.mspx
100000928 || COMMUNITY EXPLOIT LANDesk Management Suite Alerting Service buffer overflow || bugtraq,23483 || cve,2007-1674
100000929 || COMMUNITY WEB-PHP Xoops module Articles SQL Injection Exploit || url,www.securityfocus.com/archive/1/463916
100000930 || COMMUNITY WEB-PHP Drake CMS 404.php Local File Include Vulnerability || bugtraq,23215
100000931 || COMMUNITY WEB-PHP Softerra Time-Assistant remote include attempt || bugtraq,23203
100000932 || COMMUNITY WEB-PHP Softerra Time-Assistant remote include attempt || bugtraq,23203
100000933 || COMMUNITY WEB-PHP Aardvark button/settings_sql.php File Include Vulnerability || url,securityfocus.com/archive/1/464351
100000934 || COMMUNITY WEB-PHP Aardvark button/new_day.php File Include Vulnerability || url,securityfocus.com/archive/1/464351
                                                                                           
┌──(deadboy㉿kali)-[/etc/snort]
└─$ tail -3 community-sid-msg.map 
100000932 || COMMUNITY WEB-PHP Softerra Time-Assistant remote include attempt || bugtraq,23203
100000933 || COMMUNITY WEB-PHP Aardvark button/settings_sql.php File Include Vulnerability || url,securityfocus.com/archive/1/464351
100000934 || COMMUNITY WEB-PHP Aardvark button/new_day.php File Include Vulnerability || url,securityfocus.com/archive/1/464351

```
## Numbering the Lines
`nl` --> This command is useful in numbering the lines of a file
Syntax:
```
nl <filename?
```
demo:
```
┌──(deadboy㉿kali)-[/etc/snort]
└─$ nl balanced.lua        
     1  ---------------------------------------------------------------------------
     2  -- balanced connectivity and security policy
     3  -- use with -c snort.lua --tweaks balanced
     4  ---------------------------------------------------------------------------
       
     5  arp_spoof = nil
       
     6  detection = { pcre_override = false }
       
     7  http_inspect.request_depth = 300
     8  http_inspect.response_depth = 500
       
     9  port_scan = nil
       
    10  stream_ip.min_frag_length = 16
       
    11  table.insert(
    12      binder, 1, -- add http port binding to appease the perf gods
    13      { when = { proto = 'tcp', ports = '80', role='server' }, use = { type = 'http_inspect' } })
```

# Filtering with grep
we can use `grep` command to view line with a specific word
Demo:
```
──(deadboy㉿kali)-[/etc/snort]
└─$ cat community-sid-msg.map| grep access
100000174 || COMMUNITY WEB-IIS RSA WebAgent access || cve,2005-1118 || bugtraq,13168
100000179 || COMMUNITY WEB-MISC SMC TRACE access || url,www.kb.cert.org/vuls/id/867593
100000183 || COMMUNITY WEB-ATTACKS SAP WAS syscmd access || url,www.cybsec.com/vuln/CYBSEC_Security_Advisory_Multiple_XSS_in_SAP_WAS.pdf
100000184 || COMMUNITY WEB-MISC JBoss JMXInvokerServlet access || url,online.securityfocus.com/archive/1/415707
100000186 || COMMUNITY WEB-PHP phpinfo access || bugtraq,5789 || cve,2002-1149 || url,www.osvdb.org/displayvuln.php?osvdb_id=3356
.
.
.
.
```
## Hacker Challenge: using `grep, nl, head, tail`
Do it later


# Using sed to Find and Replace
`sed` --> This command is used to search and replace a word with and another word
Syntax:
Changing Every Occurrences of the given word
```
sed s/orignal_word/new_word/g <orignal filename> > <file where you want to save the new result>

# here s means we are searching the word
# g means we want the replacement gloabally which means every occurrences will get changed
```
Changing the First Occurrence of the word
```
sed s/orignal_word/new_word/ <orignal filename> > <file where you want to save the new result>

# In this command we replaced the g
```
Changing the specific occurrence of the word
```
sed s/orignal_word/new_word/2 <orignal filename> > <file where you want to save the new result>

# IN this command we replaces the second occurrence of the word by writing 2
```
# Viewing Files with more and less
`cat` command is useful when creating a file or displaying a small file. when dealt with large files `cat` commands just scrolls through every page of the file and stops at the last line

That's were we use `more` and `less` command
## Controlling the display with `more
`more` --> This command display a page of a file once at a time to view the next page we press `ENTER` . and to quit press `q`
- This command has the same utitlity as the `man`page
Syntax:
`more <filename>`

## Displaying and Filtering with less
`less` --> This command is very similar to `more` command but with some additional functionality
- In `less` command we can not even scroll through the page but we can even filter for a specific terms
### Filtering words in the less command
1. press `/` this will allow you to enter the word you want to filter
2. Type your word and press `ENTER`
3. Now you will see all the occurrences of the word in the colour press `n` , this will take you to the next occurrence of the given word
DOUBT: The filtering works only on the words that are visible on the screen, if a word is in the file but it is not visible on the screen then it will not filter that word.