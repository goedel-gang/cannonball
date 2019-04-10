"""
The quest to find the biggest!!!
"""

import os
import sys
import argparse

from math import log

C = lambda s: (s**2 - 4*s - 2)*(s**2 - 4*s + 1)*(s**3 - 6*s**2 + 3*s + 19) // 162

def takeoff(i):
    """
    Make i get bigger a lot faster, and do some calculations
    """
    while True:
        i *= i
        s = i * 3 + 2
        fname = "solutions/{:.10e}".format(log(s))
        if not os.path.isfile(fname):
            print("\rexp({:.10e})".format(log(s)), file=sys.stderr, flush=True,
                                          end="")
            v = C(s)
            print("\rwxp({:.10e})".format(log(s)), file=sys.stderr, flush=True,
                                          end="")
            with open(fname, "w") as sol_file:
                print(v, file=sol_file)

def get_args():
    parser = argparse.ArgumentParser(description=__doc__)
    # float so we can have scientific notation
    parser.add_argument("--start", type=float, default=9,
                        help="initial multiple of 3")
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()
    takeoff(int(args.start))
