"""
Finding a polynomial to fit the line.

The output is consistently:
Matrix([[1/162], [-7/81], [11/27], [-91/162], [-133/162], [103/54], [35/81], [-19/81]])
Matrix([[1/9], [-2/3], [1/3], [19/9]])
Matrix([[1/3], [-4/3], [-2/3]])
"""

import random

from sympy import *

C = symbols("C")

def form_matrix(s_values):
    return Matrix([[s ** i for i in reversed(range(len(s_values)))]
                        for s in s_values])

with open("data.tsv", "r") as data_file:
    data = [list(map(int, line.strip().split())) for line in data_file]

lines = random.sample(data, k=8)
s_values, C_values, *_ = zip(*lines)
print(form_matrix(s_values).inv() * Matrix(C_values))

lines = random.sample(data, k=4)
s_values, _, n_P_values, _ = zip(*lines)
print(form_matrix(s_values).inv() * Matrix(n_P_values))

lines = random.sample(data, k=3)
s_values, _, _, n_C_values = zip(*lines)
print(form_matrix(s_values).inv() * Matrix(n_C_values))
