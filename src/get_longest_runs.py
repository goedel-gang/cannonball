#!/usr/bin/env python3

"""
Finding largest numbers - of course it's probably monstrously inefficient, but
this program really isn't the bottleneck.
"""

import argparse

from re import findall

def get_longest_runs(files):
    best = {}
    best_2m3 = 0
    for sol_file in files:
        if sol_file.name.count("_") == 3:
            depth = sol_file.name.split("_")[1]
            solutions = [line for line in sol_file if line.startswith(">")]
            if solutions:
                _, furthest, *_ = map(int, findall(r"\d+", solutions[-1]))
            else:
                furthest = 0
            if depth not in best:
                best[depth] = furthest
            elif furthest > best[depth]:
                best[depth] = furthest
        elif sol_file.name.count("_") == 2:
            solutions = [line for line in sol_file if line.startswith(">")]
            if solutions:
                _, furthest, *_ = map(int, findall(r"\d+", solutions[-1]))
            else:
                furthest = 0
            if furthest > best_2m3:
                best_2m3 = furthest
    return best, best_2m3

def fmt_val(v):
    if "e" in v:
        base, exponent = v.split("e")
        return r"\({}^{{{}}}\)".format(base, exponent)
    return v

def format_furthest(best, best_2m3, args):
    for depth, furthest in sorted(best.items(), key=lambda x: float(x[0])):
        print(r"{} & {} \\".format(fmt_val(depth), furthest),
              file=args.best_file)
    print("{}-gon".format(best_2m3), file=vars(args)["2mod3_file"])

def get_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--best-file", type=argparse.FileType("w"),
                        required=True, help="file to write best to")
    parser.add_argument("--2mod3-file", type=argparse.FileType("w"),
                        required=True, help="file to best 2m3 run to")
    parser.add_argument("--files", type=argparse.FileType("r"), required=True,
                        nargs="+", help="Files to search for solutions")
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()
    format_furthest(*get_longest_runs(args.files), args)
