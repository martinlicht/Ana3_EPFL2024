default : exam

clean:
	rm -f *.aux *.backup *.bak *.bbl *.blg *.dat foo *.gz *.idx *.ilg *.ind *.log *.nav *.out *.snm *.pdf *.toc 

indent: 
	for Datei in *.tex; do latexindent $$Datei --overwrite; done 

check: 
	for Datei in *.tex; do lacheck $$Datei; done 
	grep -e 'TODO|FIXME' *.tex;:
	grep -Eo '(\b.+) \1\b' *.tex;: 

spelling: 
	for Datei in *.tex; do ispell -t $$Datei; done

substitutions:
	#for texfile in ./*tex; do echo $$texfile && ../latexdisp.pl $$texfile > temp.tex; mv temp.tex $$texfile; done
	sed -i -e 's \.\$$ \$$\. g' ./*tex 
	sed -i -e 's ,\$$ \$$, g' ./*tex 
	sed -i -e 's2 \\eqref2~\\eqref2g' ./*tex 
	sed -i -e 's2 \\ref2~\\ref2g' ./*tex 
	sed -i -e 's2 \\cite2~\\cite2g' ./*tex 

quick: 
	pdflatex -shell-escape -synctex=1 -interaction=nonstopmode exam.tex

exam: 
	pdflatex -shell-escape -synctex=1 -interaction=nonstopmode exam.tex 
	# bibtex exam
	pdflatex -shell-escape -synctex=1 -interaction=nonstopmode exam.tex 
	pdflatex -shell-escape -synctex=1 -interaction=nonstopmode exam.tex
