#!/usr/bin/env zsh

if [[ -z "$1" ]] then
    echo Need arguments
    exit 1;
elif [[ -z "$2" ]] then
    echo Need arguments
    exit 1;
fi;

local timestamp=$(date +"%s")
stdbuf -i0 -o0 -e0 ./cannonball "$1" "$2" |
    tee /dev/tty > solutions/sol_"$1"_"$2"_"$timestamp"
