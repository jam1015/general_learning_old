---
date: \today
title: Ansi Codes
author: Jordan Mandel
---

`cat` this document to see the ansi codes to their work.

`ESC` sequences that work on my zsh are

- `\033`
- `\u001b`
- `\x1B`
- `\e`

Append `[` to get `CSI` control sequence introducer that starts  control sequence. 

There are other ANSI codes that you put between `\[` and `\]`. A lot of these might not work in ZSH.

For zsh you need single quotes and to prepend a dollar sign for colors.

To change colors in zsh it is `\033[arg;arg;arg;` where the args can be found in a table. Can then reset them. Bright colors not the same as bold colors.

Note `90-97` and `100-107` for rbight.

also: `[48;5;{1-255}m` or `[48;2;{r};{g};{b}m` 

Should wrap in `\[` and `\]` for non printing commands; size of visible prompt. So do it for anything that doesn't move the cursor or to things that move the cursor to weird places.
Can also wrap codes in `%{ ... %}` for zsh. But it looks like it's better to avoid ansi codes in zsh because some don't work.


