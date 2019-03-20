CC=gcc -std=c99
SRC=./src/main.c -I./include
EXEC=tash

all:
	$(CC) -o $(EXEC) $(SRC)

run:
	./$(EXEC)

test:
	bash < ./in/scenario1.txt > bash_answer1.txt
	./$(EXEC) < ./in/scenario1.txt > your_answer1.txt
	cmp ./bash_answer1.txt ./your_answer1.txt
	bash < ./in/scenario2.txt > bash_answer2.txt
	./$(EXEC) < ./in/scenario2.txt > your_answer2.txt
	cmp ./bash_answer2.txt ./your_answer2.txt
	bash < ./in/scenario3.txt > bash_answer3.txt
	./$(EXEC) < ./in/scenario3.txt > your_answer3.txt
	cmp ./bash_answer3.txt ./your_answer3.txt
	bash < ./in/scenario4.txt > bash_answer4.txt
	./$(EXEC) < ./in/scenario4.txt > your_answer4.txt
	cmp ./bash_answer4.txt ./your_answer4.txt
	bash < ./in/scenario5.txt > bash_answer5.txt
	./$(EXEC) < ./in/scenario5.txt > your_answer5.txt
	cmp ./bash_answer5.txt ./your_answer5.txt

clean:
	rm your_answer* bash_answer* $(EXEC)

latex:
	pdflatex ./docs/report.tex
	mv report.pdf ./docs/  # TODO: Improve this with `pdflatex` option!
	rm report.aux report.log

md:
	mdpdf ./docs/report.md
