#!/usr/bin/env python3

"""
Python implementation of 2mod3, just to have easy access to arbitrary-precision
integers. This program generates solutions at an alarming rate. Unfortunately
I'm pretty sure it spends most of its time IO bound, but I have to save
solutions so there's not much I can do about it.

It takes the arguments s and n_c. S SHOULD BE CONGRUENT TO 2 MOD 3, and n_c
should be your best estimate for a lower bound on the height of the cannonball
stack which solves s. If you don't know what it should be, leave it blank.

It's probably safer to pick a big-ish value for s.

If you've got nothing, just do eg. python 2mod3.py -s 8 --write-solutions -
An example of advanced usage would be:
python 2mod3.py -s 4524710 -nc 6824327495086 -ncp 6824318445673 --write-solutions -

Unless you give it two values of s, so that it can calculate an initial
difference, it calculates the first two slowly, and then starts optimising.  in
order to make it more idiot proof (because I have to use it) This means it can
take quite a while to get up to speed at first, but when it does, boy has it got
speed.
"""

import argparse
import sys

from itertools import count

# how often to print a progress update
UPDATE_FREQ = 5000

def polygonal(s, n):
    return (n * n * (s - 2) - n * (s - 4)) >> 1

def cannon(s, n):
    return n * (n + 1) * ((s - 2) * (2 * n + 1) - 3 * (s - 4)) // 12

def isqrt(n):
    if n < 2:
        return n
    else:
        small = isqrt(n >> 2) << 1
        large = small + 1
        if large * large > n:
            return small
        else:
            return large

def run_base(base, n_c, args):
    denominator = 2 * base - 4;
    cannonballs = cannon(base, n_c)
    while True:
        discriminant = (base - 4) * (base - 4) + 8 * (base - 2) * cannonballs
        discriminant_sqrt = isqrt(discriminant)
        if discriminant_sqrt * discriminant_sqrt == discriminant:
            numerator = base - 4 + discriminant_sqrt
            if numerator % denominator == 0:
                args.write_solutions.write(
                    ">{} == P({}, {}) == C({}, {})\n".format(
                       cannonballs, base, numerator // denominator, base, n_c))
                break
        n_c += 1
        cannonballs += polygonal(base, n_c)
    return n_c

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-nc", type=int, help="starting value of nc",
                        default=2)
    parser.add_argument("-ncp", type=int, help="previous nc")
    parser.add_argument("-s", type=int, help="starting value of s",
                        default = 8)
    parser.add_argument("--write-solutions", type=argparse.FileType("w"),
                        required=True, help="file to write solutions to")
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()
    print("Finding cannonball numbers where s = 2 mod 3", flush=True)
    if args.ncp is None:
        prev_n_c = n_c = run_base(args.s, args.nc, args)
    else:
        n_c = args.nc
        prev_n_c = args.ncp
    for i, base in enumerate(count(args.s + 3, 3)):
        if i % UPDATE_FREQ == 0:
            print("\r checking num {}".format(base), file=sys.stderr, end="",
                  flush=True)
        _prev = n_c
        # optimisation assuming the curve is strictly convex
        n_c = run_base(base, n_c + n_c - prev_n_c, args)
        prev_n_c = _prev
