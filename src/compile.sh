#!/usr/bin/env zsh

python factcheck.py --files c/solutions/* --write-interesting ../graph/interesting.tsv --write-boring ../graph/boring.tsv --write-all ../graph/all.tsv --write-tex interesting.tex
python get_longest_runs.py --files c/solutions/* --best-file depthtable.tex --2mod3-file 2mod3count.tex
