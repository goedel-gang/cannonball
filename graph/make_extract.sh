#!/usr/bin/env zsh

head -n 1000 all.tsv > all_extract.tsv
tail -n 1000 all.tsv >> all_extract.tsv
cut -f 1-2 all_extract.tsv | tr -s $"\t" " & " | sed "s/$/ \\\\\\\\/g" > all_extract.tex
wc -l all.tsv > all_linecount.tex
