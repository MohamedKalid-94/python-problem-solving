"""
Topic: Nested Loops

Problem:
Print a star pattern.

Output:
*
**
***
****
*****
"""

for row in range(1, 6):

    for column in range(1, row + 1):
        print("*", end="")

    print()