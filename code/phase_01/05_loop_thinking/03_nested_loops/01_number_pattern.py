"""
Topic: Nested Loops

Problem:
Print a simple number pattern.

Output:
1
12
123
1243
12345
"""

for row in range(1, 6):

    for column in range(1, row + 1):
        print(column, end="")

    print()