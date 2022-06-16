---
title: "The Linux Command Line Notes"
author: Jordan Mandel
date: \today
geometry: margin=2.54cm
---
# 6. Redirection

`ls -l /bin/usr 2> ls-error.txt`
`ls -l /bing/usr > ls-output.txrt 2>&1`
`ls -l /bin/usr &> ls-output.txt`
`ls -l /bin/usr &>> ls-output.txt`
`ls /usr/bin | tee ls.txt | grep zip`

# 7. Seeing the world as the shell sees it
## Expansion
### we had pathname:
`ls .[!.]* `
`echo .[!.]*`

### tilde, 
`ls ~`

### arithmetic
`echo $(($((5**2)) * 3))`
Can group with parentheses eliminating need for inner expression
`echo $(((5**2) * 3))`

### brace 

`..`, comma separated lists, cartesian products when multiple or nested brace expansions are used), parameter, and command expansion.

`echo Front-{A,B,C}-Back`
`echo {001..15}`
`echo a{A{1,2},B{3,4}}b`
`mkdir {2007..2009}-{01..12}`

### parameter
`echo $USER`

can get variables with `printenv | less`

### command
ehco $USER
`ls -l $(which cp)`
can also use backtics for  command subst5itution

## Quoting
### Double Quotes
- word splitting (suppression of extra spaces/new lines), pathname expansion (ie with wildcards), tilde expansion, and brace expansion are suppressed; 
	- none of these use the dollar sign
	- Can escape the dollar sign in double quotes with a backslash
	- can also use backtick

- but we can do command substitution (which itself can have expansion), arithmetic expansion, and parameter epansion
	- all of these use the dollar sign
	- Can escape the dollar sign in double quotes with a backslash

note the interesting example of `echo` not outputting some intended line breaks/etc due to word splitting. get around this with double quotes. example of this is `echo $(cal)` vs `echo "$(cal)"`


### Single Quotes



Single quotes suppress all expansions.

### backslash
Can use it to escape characters, including special characters in file names.
