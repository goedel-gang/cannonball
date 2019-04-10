"""
Finding a polynomial to fit the line.

The output is consistently:
Matrix([[1/162], [-7/81], [11/27], [-91/162], [-133/162], [103/54], [35/81], [-19/81]])
"""

import random

from sympy import *

C = symbols("C")

def form_matrix(s_values):
    assert len(s_values) == 8
    return Matrix([[s ** i for i in range(7, -1, -1)] for s in s_values])

with open("data.tsv", "r") as data_file:
    data = [list(map(int, line.strip().split())) for line in data_file]

lines = random.sample(data, k=8)
s_values, C_values = zip(*lines)
print(form_matrix(s_values).inv() * Matrix(C_values))
