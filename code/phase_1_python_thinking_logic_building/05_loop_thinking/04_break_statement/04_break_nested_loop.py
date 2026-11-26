"""
Topic: break Statement

Problem:
Break the inner loop.
"""

for row in range(1, 4):

    for column in range(1, 6):

        if column == 3:
            break

        print(column, end=" ")

    print()