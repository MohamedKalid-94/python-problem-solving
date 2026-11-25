"""
Topic: extend() and Concatenation

Problem:
Combine two lists.
"""

list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1.extend(list2)

print(list1)

combined = list1 + [7, 8]

print(combined)