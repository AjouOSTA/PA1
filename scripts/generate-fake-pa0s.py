#!/usr/bin/python3

import os

PA0_root = '2019-1-PA0'

if PA0_root not in os.listdir():
    os.mkdir(PA0_root)

os.chdir(PA0_root)

from uuid import UUID, uuid4
import random as rd

rd.seed(201120000)

files_in_PA0_root = set(os.listdir())

for _ in range(3):
    fake_student_id = str(UUID(int=rd.getrandbits(128)))

    if fake_student_id in files_in_PA0_root:
        continue

    os.mkdir(fake_student_id)

    os.mkdir(os.path.join(fake_student_id, 'in'))
    os.mkdir(os.path.join(fake_student_id, 'out'))

    sample0_path_v = fake_student_id, 'out', 'sample0.txt'
    sample1_path_v = fake_student_id, 'out', 'sample1.txt'
    sample2_path_v = fake_student_id, 'out', 'sample2.txt'

    sample0_path = os.path.join(*sample0_path_v)
    sample1_path = os.path.join(*sample1_path_v)
    sample2_path = os.path.join(*sample2_path_v)

    def create_empty_file(path):
        open(path, 'w').close()

    def create_write_any(path):
        with open(path, 'w') as f:
            f.write(str(uuid4()))

    create_empty_file(sample0_path) if rd.random() > 0.5 else create_write_any(sample0_path)
    create_empty_file(sample1_path) if rd.random() > 0.5 else create_write_any(sample1_path)
    create_empty_file(sample2_path) if rd.random() > 0.5 else create_write_any(sample2_path)
    
    Makefile_str = '''CC=gcc -std=c99
SRC=course_sched.c
EXEC=course_sched

all:
	$(CC) -o $(EXEC) $(SRC)

run:
	./$(EXEC) ./in/everytime0.csv
	./$(EXEC) ./in/everytime1.csv
	./$(EXEC) ./in/everytime2.csv

test:
	./$(EXEC) ./in/everytime0.csv > myout0.txt
	./$(EXEC) ./in/everytime1.csv > myout1.txt
	./$(EXEC) ./in/everytime2.csv > myout2.txt
	cmp myout0.txt ./out/sample0.txt
	cmp myout1.txt ./out/sample1.txt
	cmp myout2.txt ./out/sample2.txt

latex:
	pdflatex ./docs/report.tex
	mv report.pdf ./docs/  # TODO: Improve this with `pdflatex` option!
	rm report.aux report.log

md:
	mdpdf ./docs/report.md
    
    '''

    with open(os.path.join(fake_student_id, 'Makefile'), 'w') as f_makefile:
        f_makefile.write(Makefile_str)

    course_sched_src = '''#include <stdio.h>

int main() {
    printf(\"It's fake, dude.\\n\");
}
'''
    with open(os.path.join(fake_student_id, 'course_sched.c'), 'w') as f_src:
        f_src.write(course_sched_src)


