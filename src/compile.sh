#!/usr/bin/env zsh

python factcheck.py --files c/solutions/* --write-interesting interesting.tex --write-boring boring.tex --write-all all.tex
python get_longest_runs.py --files c/solutions/* --best-file depthtable.tex --2mod3-file 2mod3count.tex
