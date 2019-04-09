#!/usr/bin/env zsh

cd ../src;
./compile.zsh;
cd ../graph;
cat ../src/tab.tex | sed -e "s/ *& */	/g" -e "s/\\\\//g" > solutions.tsv
Rscript graph.R > model.tex
