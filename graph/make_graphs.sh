#!/usr/bin/env zsh

echo compiling
cd ../src;
./compile.sh;
cd ../graph;
head -n 10000 > all_extract.tsv
tail -n 10000 >> all_extract.tsv
wc -l all.tsv > all_linecount.tex
echo graphing
Rscript graph.R > model.tex
