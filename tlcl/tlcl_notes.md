---
title: "The Linux Command Line Notes"
author: Jordan Mandel
date: \today
geometry: margin=2.54cm
---
## Ch. 6. Redirection

`ls -l /bin/usr 2> ls-error.txt`
`ls -l /bing/usr > ls-output.txrt 2>&1`
`ls -l /bin/usr &> ls-output.txt`
`ls -l /bin/usr &>> ls-output.txt`
`ls /usr/bin | tee ls.txt | grep zip`

## Ch. 7. Seeing the world as the shell sees it
### Expansion
#### we had pathname:
`ls .[!.]* `
`echo .[!.]*`

#### tilde, 
`ls ~`

#### arithmetic
`echo $(($((5**2)) * 3))`
Can group with parentheses eliminating need for inner expression
`echo $(((5**2) * 3))`

#### brace 

`..`, comma separated lists, cartesian products when multiple or nested brace expansions are used), parameter, and command expansion.

`echo Front-{A,B,C}-Back`
`echo {001..15}`
`echo a{A{1,2},B{3,4}}b`
`mkdir {2007..2009}-{01..12}`

#### parameter
`echo $USER`

can get variables with `printenv | less`

#### command
ehco $USER
`ls -l $(which cp)`
can also use backtics for  command subst5itution

### Quoting
#### Double Quotes
- word splitting (suppression of extra spaces/new lines), pathname expansion (ie with wildcards), tilde expansion, and brace expansion are suppressed; 
	- none of these use the dollar sign
	- Can escape the dollar sign in double quotes with a backslash
	- can also use backtick

- but we can do command substitution (which itself can have expansion), arithmetic expansion, and parameter epansion
	- all of these use the dollar sign followed by parentheses
	- Can escape the dollar sign in double quotes with a backslash

note the interesting example of `echo` not outputting some intended line breaks/etc due to word splitting. get around this with double quotes. example of this is `echo $(cal)` vs `echo "$(cal)"`


#### Single Quotes



Single quotes suppress all expansions.

#### backslash
Can use it to escape characters, including special characters in file names.

for example:
```
sleep 10; echo -e "Time's up\a"
```

We could also do this:

```
sleep 10; echo "Time's up" $'\a'
```
## Ch. 15. Storage Media
there is the `mount` command to see the mounted systems

look in `\etc\fstab`

`journalctl -f`, it can also be `sudo tail -f /var/log/messages` on some systems.


`ls /dev`

codes are: `fd*` for floppy disks.
`hd*` for motherboard storage; alternating m\*ster and sl\*ve. Number for partition.

`lp*` for printer

`sd*` for storage devices like usb drives.

`sr*` for optical drives.
can also see symlinks to device files

there is also `lsblk`

`Bus 001 Device 004: ID 1e4e:0102 Cubeternet GL-UPC822 UVC WebCam`

`fuser /dev/video0`
corresponds to
`/dev/bus/usb/001/004`


there is 
`mount -t iso9660 /dev/sdc /mnt/cdrom`
to actually mount something

ther is also `lsof` and `fuser`

### Creating File Systems

```
sudo umount /dev/sdb1
sudo fdisk /dev/sdb
```
then there are several options

then use `mkfs` to make a new file system.  for example `sudo mkfs -t ext4 /dev/sdb1`

`fsck` can check/repair a file system

`dd` can do a direct copy of data between media.

can be used for `iso` files.

there is also `genisoimage` which can be used to generate iso image from files gathered into a directory.

can mount iso images that are still onyour hard drive: 

`mount -t iso9660 -o loop image.iso /mnt/iso_image`

there is also `wodim` to blank, and to write too.



there is the `dd` command
`genisoimage` for creating something from a collection of files

## Ch 16. Networking

```
ping nsa.gov
```

#### these trace packets across networks

```
traceroute
traceroute -TI
```

```
tracepath
```

#### internal network configuration

to look at network configuration:
```
ip addr
```

to look at network configurations

```
# like ifconfig
netstat -ie
# show kernel internal network settings
netstat -r
```
### transporting files across a network 

#### ftp
login to server (not secure). `lcd` changes directory on local machine. `get [file]` will start the file transfer.
can type `help` to get more info.

#### lftp
better than ftp; use this; but should be using sftp in general anyway.

#### wget

### secure communication

#### ssh
authenticates remote server, encrypts all data sent/received
runs on port (have to learn about ports) 22.

more flexible than ftp or lftp

```
ssh user@remote_host
```

if there is a prloblem it will tell us what line the `~/.ssh/known_hosts` file has the outdated key

can run a single command

```
ssh remote-sys 'ls *' > dirlist.txt
```

to get the x system from remote server

```
ssh -X remote-sys #either X or Y depending on the system
ssh -Y remote-sys
```

#### scp and sftp

```
scp remote-sys:document.txt .
```

or if the remote hostname is different than the local hostname:

```
scp bob@remote-sys:document.txt .
```

```
sftp remote-sys
ls
lcd Desktop
get file.txt
bye
```


there is puTTY for windows but it might have something built-in now.

more reading: `Linus Network Administrator's Guide`

wikipedia articles for ip addresses, host names, URIs.

## Ch. 17. Searching For Files


### easy way with `locate`
locate finds things the easy way:

```
locate bin/zip
```

```
locate zip | grep bin
```

but I might have to do `sudo updatedb`.  Might have to set a cron job.

### hard way with `find`

```
find ~ -type d | wc -l
```

#### Tests

File | Type Description |
| --- | ------------ |
b | Block special device file |
c | Character special device file |
d | Directory |
f | Regular file |
l | Symbolic link |

```
find ~ -type f -name "*.JPG" -size +1M | wc -l
```

The plus sign means 'more than'. Minus sign means less than  Available sizes are: 

```
b 512-byte blocks. This is the default if no unit is specified.
c Bytes.
w 2-byte words.
k Kilobytes (units of 1024 bytes).
M Megabytes (units of 1048576 bytes).
G Gigabytes (units of 1073741824 bytes).
```

here are some more options (can use cmin in man page to find the rest)
```
-cmin n
Match files or directories whose content or attributes were 
last modified exactly n minutes ago. To specify less than n 
minutes ago, use -n, and to specify more than n minutes 
ago, use +n.
```
Numeric arguments above can take `+` and `-`.

#### operators
can use `-and` `-or` `-not` and escaped parentheses.

for example:

```
find ~ \( -type f -not -perm 0600 \) -or \( -type d -not -perm 0700 \)
```
does logical short-circuiting

#### predifiened actions
can perform actions on the found files: `-delete` `-ls` `-print` `-quit` (more in man pages): print is used if nothing is specified

so `find ~` is the same as `find ~ -print`


we can also go

```
find ~ -type f -name '*.bak' -delete
```

the `and` is implied

the logical operators can be used to control the actions;

```
find ~ -type f -and -name '*.bak' -and -print
```

if we put the print-first it would be different; it would print before doing the tests.


#### user-defined actions

instead of `-delete` we can go: `-exec rm '{}' ';'` Have to quote. Semicolon is necessary delimeter.  Braces represent the filepath of the file found. Can use `-ok` rather than `-exec` to get confirmation for each action.

for example: `find ~ -type f -name 'foo*' -ok ls -l '{}' ';'`

#### impriving efficiency
`-exec` uses a new instance of each command for each file found. we can use `xargs` or a certain feature of `find` itself to get thorugh this.

##### the `find` way
replace `';'` with `+` and it will execute on each file.

##### the `xargs` way

```
find ~ -type f -name `foo*` -print | xargs ls -l
```

if too many arguments are given it will start over with next argument after reaching end.

To deal with funny file names we can use the `-print0` which separates with null characters and the `--null` argument to xargs.


```
find ~ -iname '*.jpg' -print0 | xargs --null ls -l
```


#### return to playground

```
mkdir -p playground/dir{001..1000}
touch playground/dir-{001..100}/file-{A-Z}
find playground -type f -name 'file-A'
[me@linuxbox ~]$ find playground -type f -name 'file-B' -exec touch 
find playground -type f -newer playground/timestamp

[me@linuxbox ~]$ find playground \( -type f -not -perm 0600 \) -or \( -type d -not -perm 0700 \)

[me@linuxbox ~]$ find playground \( -type f -not -perm 0600 -exec 
chmod 0600 '{}' ';' \) -or \( -type d -not -perm 0700 -exec chmod 0700 '{}' ';' \)
```

there are more options: `-depth` does depth first actions. `-maxdepth`, `-mindepth`, `-mount` (dont traverse directories on other file systems), `-noleaf` better to to use when using DOS -like file systems.
#### Other options

`-depth`: process files before directory itself

`-maxdepth`, `-mindepth`: how deep to go before performing tests and actions
`-mount` dont go doun mounted file systems
`-noleaf` don't perform optimizations based on the assumption that it is a unix file system

## 18. - Archiving and Backup

### Compressing Files
`gzip`, `gunzip` (and associated options) `zcat`, `zless`

`bzip2`

`tar`

`rsync`

can just go

`gunzip foo.txt` leaving of the `.gz` because it is assumed.


`zcat` uses cat on the zipped file.  there is also `zless`


there is also `bzip` which is better.
`bunzip`
`bzcat`

`bz2recover` for damaged bz2 files.

### archiving

remembering them for long term storage.

```
tar c path
```

c is for create
x is for extract
r is for append
t is for list

[make playground]

tar cf playground.tar playground

tar tf playgorund.tar
tar tvf playground.tar

make directory, change into it

tar xf ../playground.tar


ownership is transferred to decompressor


#### funny pathnames

```
mkdir foo
cd ~
tar cf playground2.tar ~/playground
cd foo
tar xf ../playground2.tar
ls
```
output is `home` because of how the pathnames work.



can go

```
tar xf archive.tar pathname
```

or
```
tar xf ../playground2.tar --wildards 'home/me/playground/dir-*/file-A'
```



can use it with `find` 
```
[me@linuxbox ~]$ find playground -name 'file-A' -exec tar rf 
playground.tar '{}' '+'
```

recall that `+` makes it run only once.


can also make incremental backups; look up more later

look at:

```
[me@linuxbox ~]$ find playground -name 'file-A' | tar cf - --files-
from=- | gzip > playground.tgz
```

`-` means stdin/out

```
[me@linuxbox ~]$ find playground -name 'file-A' | tar czf 
playground.tgz -T -
```
If we had wanted to create a bzip2-compressed archive instead, we could have done
this:
```
[me@linuxbox ~]$ find playground -name 'file-A' | tar cjf 
playground.tbz -T -
```

```
tar over ssh
[me@linuxbox ~]$ mkdir remote-stuff
[me@linuxbox ~]$ cd remote-stuff
[me@linuxbox remote-stuff]$ ssh remote-sys 'tar cf - Documents' | tar
xf -
me@remote-sys’s password:
[me@linuxbox remote-stuff]$ ls
Documents
```


