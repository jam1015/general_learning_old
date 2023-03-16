---
title: Example Markdown
author: Jordan Mandel
date: today
  md_document:
    variant: markdown_strict
---

FIRST LEVEL
=======================

```
pandoc markdown_example.md -s -f markdown_strict -t pdf -o markdown_notes.pdf --pdf-engine wkhtmltopdf
```

second_level
========================

Sphinx of black quartz judge my vow.


# First Level


### Third level

> here we go with editing a line  
>> another block quote  
>> does it double?  
>> I hope so  
> ok enough  
> done  

#### fourth level 



I feel normal
 
*I feel angry*

**I feel infuriated**


+ So far some things seem not to work
+ nested block quotes are among them
+ above we see we don't insert a line break after a fourth level header
- will have to check out pandoc markdown (as opposed to strict markdown) to fix

1. I hope that markdown will help me write better documents.

2. Maybe I'll move on to LaTeX.

	Latex is a nice typesetting system.  

	I hope to use it someday.

	See, multiple paragraphs.
	

Here we go with a [complete classic](https://www.cnn.com/ "an overrated news outlet"). Adding a title doesn't seem to work for now [ladeedaa][1]


[1]: https://www.cnn.com/ "CNN"



If you want your page to validate under XHTML 1.0 Strict,
you've got to put paragraph tags in your blockquotes:

```
<blockquote>/
<p>For example.</p>  
</blockquote>  
```


now we put in some images. ![groggy](./grog.jpg "alcohol")

can we insert another pic?

![mountain][2]

[2]: ./everest.jpg "tall"
