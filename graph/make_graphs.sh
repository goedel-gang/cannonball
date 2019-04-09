#!/usr/bin/env zsh

cat ../src/tab.tex | sed -e "s/ *& */	/g" -e "s/\\\\//g" > solutions.tsv
Rscript graph.R
