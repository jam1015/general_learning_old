---
Author: Jordan Mandel
Date: 2023-02-27
Title: Vlime Notes
---

I use `\` to reperesent `<localleader>`. Use your localleader.

# Starting The Server

```
sbcl --load  ~/.local/share/nvim/lazy/vlime/lisp/start-vlime.lisp
```

or wherever the vlime repo is


to connect:

```
\cc
```

or both the above steps combined

```
\rr
```

to list all channels, and choose a connection:

```
\cs
```

to close a connection:

```
\cd
```


to send:

```
\ss
```

or

```
\i
```

folowed by `<cr>`

# Setting the Current Package

```
(in-package :vlime) ; setting it in buffer
(symbol-value (find-symbol "*PACKAGE*" "COMMON-LISP"))  ; the new line
```

or we can do `\p` and press `<CR>` on the package name in the window that appears.

# coding

1. paredit helps with parentheses
2. press `space` or `<cr>` in inset mode in parens and a window may appear with the arglist for current expression
3. there should be autoindentation
4. there is some autocompletion activated by `tab` (I've mapped it to CTRL_j).

`\dda` will show documentation `vlime-mappings-describe`
`\xc` will show cross referencing `vlime-mappings-invoke-xref`
`\wA` will close all windows `vlime-mappings-close-window`

# compiling

press `<CR>` on warning to jump to location

`\of` to compile `vlime-mappings-compile`

in debugger we can press `<CR>` on top of option we want

# Runing/Debugging

can change debug policy:

```
:let g:vlime_compiler_policy = {"DEBUG": 3}
```

can recompile and run generate again for a more detailed error

press `<CR>` on a frame to see more info. they say I should be able to press `d` but it isn't working.

`vlime-mappings-debugger` for more alleged mappings

