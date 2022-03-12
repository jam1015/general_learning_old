---
Title: "The Unix Programming Environment Notes"
Date: Today
---

sort
cat
grep

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

- `newgrp`
- `passwd`

