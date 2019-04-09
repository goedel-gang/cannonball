#!/usr/bin/env python3

"""
Program to verify polygonal cannonball numbers and then do a little
post-processing.
"""

import argparse

from cannonball import polygonal
from re import findall
from itertools import chain

def cannonball(s, n):
    """
    Derived cubic nth term of cannonball numbers.
    """
    return n * (n + 1) * ((2 * n + 1) * (s - 2) - 3 * (s - 4)) // 12

def check_line(line):
    C, s, n_P, _, n_C = map(int, findall(r"\d+", line))
    if not (C == cannonball(s, n_C) == polygonal(s, n_P)):
        raise ValueError("line {!r} incorrect".format(line))
    return s, C, n_P, n_C

def check_files(files):
    solutions = set()
    for line in chain.from_iterable(files):
        if line.startswith(">"):
            solutions.add(check_line(line))
    output_solutions(solutions)

def output_solutions(solutions_):
    solutions = list(sorted(solutions_))
    # write the output as LaTeX. We're not here to be pretty, so might as well
    # play a few rounds of code golf.
    for solution in solutions:
        print((" {} ".join("&" * 5)[2:-1] + r"\\").format(*solution))

def get_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--files", type=argparse.FileType("r"),
                        nargs="*", help="list of files to read")
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()
    check_files(args.files)
