#!/usr/bin/env zsh

local timestamp=$(date +"%s")
python3 2mod3.py $* --write-solutions ../solutions/sol_2mod3_"$timestamp"
