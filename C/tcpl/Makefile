cpama_notes.pdf: cpama_notes.md
	pandoc cpama_notes.md -f markdown -t pdf -o cpama_notes.pdf --pdf-engine pdflatex --highlight-style=tango

scanf_test: scanf_test.c
	gcc -O -Wall -W -pedantic -ansi -std=c17 -o scanf_test scanf_test.c
