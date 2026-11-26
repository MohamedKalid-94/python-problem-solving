"""
Topic: Nested Loops

Problem:
Print multiplication values from 1 to 3.
"""

for row in range(1, 4):

    for column in range(1, 4):
        print(row * column, end="\t")

    print()