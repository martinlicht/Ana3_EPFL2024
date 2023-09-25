
default: exercises

clean:
	rm -f *.aux *.log *.out *.synctex.gz 
	rm -f exercise*.pdf 

todolist:
	grep --line-number --color TODO exercise*tex

exercises:
	pdflatex exercise00.tex
	pdflatex exercise01.tex
	pdflatex exercise02.tex
	pdflatex exercise03.tex
	pdflatex exercise04.tex
	pdflatex exercise05.tex
	pdflatex exercise06.tex
	pdflatex exercise07.tex
	pdflatex exercise08.tex
	pdflatex exercise09.tex
	pdflatex exercise10.tex
	pdflatex exercise11.tex
	pdflatex exercise12.tex
	pdflatex exercise13.tex
