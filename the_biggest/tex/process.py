from sys import stdin

from itertools import zip_longest

def chunk(it, n, fv):
    return zip_longest(*[iter(it)] * n, fillvalue=fv)

num = filter(str.isdigit, stdin.read())

print(r"\seqsplit{%")
for line in chunk(chunk(num, 6, ""), 11, ""):
    print(" ".join(map("".join, line)) + "%")
print("}")
