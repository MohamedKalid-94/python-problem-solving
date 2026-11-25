"""
Topic: Deep vs Shallow Copy

Problem:
Compare shallow and deep copies.
"""

import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

original[0][0] = 100

print("Original :", original)
print("Shallow  :", shallow)
print("Deep     :", deep)
