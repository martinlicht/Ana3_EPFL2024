
TEX_FILES = $(wildcard exercise??.tex)
PDF_FILES = $(TEX_FILES:.tex=.pdf)

default: $(PDF_FILES)

clean:
	rm -f *.aux *.log *.out *.synctex.gz 
	rm -f exercise*.pdf 

todolist:
	grep --line-number --color TODO exercise*tex

%.pdf : %.tex
	pdflatex --interaction=nonstopmode $<
