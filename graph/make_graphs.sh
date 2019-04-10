#!/usr/bin/env zsh

echo compiling
cd ../src;
./compile.sh;
cd ../graph;
echo making extract
./make_extract.sh;
echo graphing
Rscript graph.R > model.tex
