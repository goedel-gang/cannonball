#!/usr/bin/env python3

"""
Program to verify polygonal cannonball numbers and then do a little
post-processing.

It's probably quite slow, but in the big O sense, this program is basically
constant time compared to some of the other computation that's happening.
"""

import argparse
import sys

from cannonball import polygonal
from re import findall
from itertools import chain
from math import log10, inf

# how often to write a progress report to STDOUT
UPDATE_FREQ = 100000

def cannonball(s, n):
    """
    Derived cubic nth term of cannonball numbers.
    """
    return n * (n + 1) * ((2 * n + 1) * (s - 2) - 3 * (s - 4)) // 12

def check_line(line):
    """
    Parse and check one line, just by extracting all present integers with some
    regex.
    """
    C, s, n_P, _, n_C = map(int, findall(r"\d+", line))
    if not (C == cannonball(s, n_C) == polygonal(s, n_P)):
        raise ValueError("line {!r} incorrect".format(line))
    return s, C, n_P, n_C

def check_files(files, args):
    """
    Parse and check all the solutions in each file
    """
    interesting = set()
    boring = set()
    for i, line in enumerate(chain.from_iterable(files)):
        if i % UPDATE_FREQ == 0:
            print("\rchecking line {}".format(i), file=sys.stderr, end="",
                  flush=True)
        if line.startswith(">"):
            sol = check_line(line)
            if is_boring(sol):
                boring.add(sol)
            else:
                interesting.add(sol)
    output_solutions(boring, interesting, args)

def is_boring(sol):
    """
    The idea here is to not display the dull ones
    """
    s, C, n_P, n_C = sol
    return (s > 100 and
            s % 3 == 2 and
            log10(C) > -3 + 7 * log10(s) and
            log10(C) < -2.5 + 7.5 * log10(s))

def tsv_solution(solution):
    """
    Format a solution as a TSV line
    """
    return "\t".join(map(str, solution)) + "\n"

def fmt_solution(sol):
    """
    write the output as LaTeX. We're not here to stand around and look pretty,
    so might as well play a few rounds of code golf.
    """
    return (" {} ".join("&" * 5)[2:-1] + r"\\" + "\n").format(*sol)

def output_solutions(boring, interesting, args):
    """
    Write solutions to a LaTeX table
    """
    for solution in sorted(interesting):
        tsv = tsv_solution(solution)
        args.write_interesting.write(tsv)
        args.write_all.write(tsv)
        args.write_tex.write(fmt_solution(solution))
    print("\rsorting...", file=sys.stderr, end="", flush=True)
    for i, solution in enumerate(sorted(boring)):
        if i % UPDATE_FREQ == 0:
            print("\rwriting s={}".format(solution[1]), file=sys.stderr,
                  flush=True, end="")
        tsv = tsv_solution(solution)
        args.write_boring.write(tsv)
        args.write_all.write(tsv)

def get_args():
    """
    Get arguments from command line
    """
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--files", type=argparse.FileType("r"), required=True,
                        nargs="+", help="list of files to read")
    parser.add_argument("--write-tex", type=argparse.FileType("w"),
                        required=True,
                        help="File to write TeX table to")
    parser.add_argument("--write-interesting", type=argparse.FileType("w"),
                        required=True,
                        help="File to write table of interesting data to")
    parser.add_argument("--write-boring", type=argparse.FileType("w"),
                        required=True,
                        help="File to write boring data to")
    parser.add_argument("--write-all", type=argparse.FileType("w"),
                        required=True,
                        help="File to write all data to")
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()
    check_files(args.files, args)
