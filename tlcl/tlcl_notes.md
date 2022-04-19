---
title: "The Linux Command Line Notes"
author: Jordan Mandel
date: \today
geometry: margin=2.54cm
---

# 7. Seeing the world as the shell sees it
we had pathname, tilde, arithmetic, brace (takes ranges split by 
`..`, comma separated lists, cartesian products when multiple or nested brace expansions are used), parameter, and command expansion.

## Double Quotes
word splitting (suppression of extra spaces), pathname expansion (ie with wildcards), tilde expansion, and brace expansion are suppressed.

but we can do command substitution (which itself can have expansion), arithmetic expansion, and parameter epansion

note the interesting example of `echo` not outputting some intended line breaks/etc due to word splitting. get around this with double quotes. example of this is `echo $(cal)`.

Can escape the dollar sign in double quotes with a backslash.

## Single Quotes
Single quotes suppress all expansions.

## backslash
Can use it to escape characters, including special characters in file names.
