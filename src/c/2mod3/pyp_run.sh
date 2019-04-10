#!/usr/bin/env zsh

local timestamp=$(date +"%s")
stdbuf -i0 -o0 -e0 pypy3 2mod3.py $* |
    tee /dev/tty > ../solutions/sol_2mod3_"$timestamp"
