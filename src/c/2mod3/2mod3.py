#!/usr/bin/env python3

"""
Python implementation of 2mod3, just to have easy access to arbitrary-precision
integers.
"""

import argparse

from itertools import count

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

def run_base(base, n_c):
    denominator = 2 * base - 4;
    cannonballs = cannon(base, n_c)
    while True:
        discriminant = (base - 4) * (base - 4) + 8 * (base - 2) * cannonballs
        discriminant_sqrt = isqrt(discriminant)
        if discriminant_sqrt * discriminant_sqrt == discriminant:
            numerator = base - 4 + discriminant_sqrt
            if numerator % denominator == 0:
                print(">{} == P({}, {}) == C({}, {})".format(
                       cannonballs, base, numerator // denominator, base, n_c), flush=True)
                break
        n_c += 1
        cannonballs += polygonal(base, n_c)
    return n_c

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-nc", type=int, help="starting value of nc",
                        default=2)
    parser.add_argument("-s", type=int, help="starting value of s",
                        default = 8)
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()
    print("Finding cannonball numbers where s = 2 mod 3")
    n_c = args.nc
    for base in count(args.s, 3):
        n_c = run_base(base, n_c)
