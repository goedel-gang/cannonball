#!/usr/bin/env zsh

cd ../src;
./compile.zsh;
cd ../graph;
cat ../src/interesting.tex | sed -e "s/ *& */	/g" -e "s/\\\\//g" > interesting.tsv
cat ../src/boring.tex | sed -e "s/ *& */	/g" -e "s/\\\\//g" > boring.tsv
cat ../src/all.tex | sed -e "s/ *& */	/g" -e "s/\\\\//g" > all.tsv
Rscript graph.R > model.tex
