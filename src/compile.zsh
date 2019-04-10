#!/usr/bin/env zsh

python factcheck.py --files c/solutions/* --write-interesting interesting.tex --write-boring boring.tex --write-all all.tex
