CC=gcc -std=c99
SRC=./src/main.c -I./include
EXEC=tash

all:
	$(CC) -o $(EXEC) $(SRC)

run:
	./$(EXEC)

test:
	bash < ./in/scenario1.txt > bash/bash_answer1.txt
	./$(EXEC) < ./in/scenario1.txt > your/your_answer1.txt
	cmp ./bash/bash_answer1.txt ./your/your_answer1.txt
	bash < ./in/scenario2.txt > bash/bash_answer2.txt
	./$(EXEC) < ./in/scenario2.txt > your/your_answer2.txt
	cmp ./bash/bash_answer2.txt ./your/your_answer2.txt
	bash < ./in/scenario3.txt > bash/bash_answer3.txt
	./$(EXEC) < ./in/scenario3.txt > your/your_answer3.txt
	cmp ./bash/bash_answer3.txt ./your/your_answer3.txt
	bash < ./in/scenario4.txt > bash/bash_answer4.txt
	./$(EXEC) < ./in/scenario4.txt > your/your_answer4.txt
	cmp ./bash/bash_answer4.txt ./your/your_answer4.txt
	bash < ./in/scenario5.txt > bash/bash_answer5.txt
	./$(EXEC) < ./in/scenario5.txt > your/your_answer5.txt
	cmp ./bash/bash_answer5.txt ./your/your_answer5.txt

clean:
	rm your/your_answer* bash/bash_answer* $(EXEC)

latex:
	pdflatex ./docs/report.tex
	mv report.pdf ./docs/  # TODO: Improve this with `pdflatex` option!
	rm report.aux report.log

md:
	mdpdf ./docs/report.md
