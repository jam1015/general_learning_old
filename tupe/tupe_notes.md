---
Title: "The Unix Programming Environment Notes"
Date: Today
---

sort
cat
grep
# quick note
`ssh -p 5679 jordan@127.0.0.1` is a good way to get into my ubuntu vm.

# some printing commands
- `pr` prints it in a nice way for line printers: `-[n]` will print in columns. `-m` will print multiple files in different columns. `nroff` and `troff` are better formatters.
- there is also `lp` which actually sends to the printer. also `lpr`.
- we have `less` and more
- `wc` can suppress some lines
- `grep` gets lines, comes from `g/regular-expression/p`
 `-v` option gets things that don't match.
 - there is also `sort -rn`, `f` whichis `--ignore-case`
 - `cat` 
 - `tail -[n]` or `tail +[n]` so start at a specific  line.
 - `cmp` to find the first place a file differs. `-l` adds byte by byte
 - `diff` to find specific differences
 - `od` prints it out byte by byte
	- `b` is for octal format, `c` is for character format. `-An` has no offset info. `-o` in two byte units. `h` and `H` are hexadecimal.

- `newgrp`
- `passwd`
- `etc/passwd`
- `etc/group` defines the groups.
login-id:encrypted-passwd:uid:group-id:misc:login-dir:shell
- `s` or `set-uid` means that executors of a file get permissions of the file owner
	- some unix systems change the way it works. so that we can have a fun time and do good things. ie turn off the setuid bit if a file is modified.

- `x` for a directory means it can be searched
- `4` for read, `2` for write `1` for execution
- only root and the owner can change permissions
	- remember that the directory's permissions determine whether or not you can delete the file.

## 2.5: Inodes
- has time of last change, last use, and time inode itself was changed.
- `ls -lut`, `ls -lct` for times or change and use/reading
- `ls -i` to get inode number which is the number the system uses to actually track the file.
	- some way to see the inode number with `od` but I don't see how.

page 59.
