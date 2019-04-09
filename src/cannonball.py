#!/usr/bin/env python3

"""
Finding cannonball numbers that are equal to a polygonal number of the same
base. See https://www.youtube.com/watch?v=q6L06pyt9CA

This file is basically the same as cannonball.c but much slower. It provides a
few useful definitions, a proof of concept and not much else.
"""

# constant for the upper bound of cannonball numbers to check
MAX_CHECK = 10 ** 18
# constant for the highest base to check
MAX_BASE = 31266

def polygonal(s, n):
    return (n * n * (s - 2) - n * (s - 4)) >> 1

def isqrt(n):
    if n < 2:
        return n
    else:
        small = isqrt(n >> 2) << 1
        large = small + 1
        if large * large > n:
            return small
        else:
            return large;

def verify(base, p_n, c_n):
    assert (polygonal(base, p_n) ==
            sum(polygonal(base, i) for i in range(1, c_n + 1)))
    print("v ", end="")

def check_base(base, max_val):
    denominator = 2 * base - 4;
    i = 2
    cannonballs = 1 + polygonal(base, 2)
    while cannonballs < max_val:
        discriminant = (base - 4) ** 2 + 8 * (base - 2) * cannonballs
        discriminant_sqrt = isqrt(discriminant)
        if discriminant_sqrt ** 2 == discriminant:
            numerator = base - 4 + discriminant_sqrt;
            if numerator % denominator == 0:
                verify(base, numerator // denominator, i)
                print("{} == P({}, {}) == C({}, {})".format(
                       cannonballs, base, numerator // denominator, base, i))
        i += 1
        cannonballs += polygonal(base, i)

if __name__ == "__main__":
    print("Finding polygonal cannonball numbers < {}, with base < {}".format(
           MAX_CHECK, MAX_BASE))
    for i in range(3, MAX_BASE):
        check_base(i, MAX_CHECK)
