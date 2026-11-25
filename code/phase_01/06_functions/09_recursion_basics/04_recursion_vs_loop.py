"""
Topic: Recursion vs Loop

Problem:
Print numbers using recursion and a loop.
"""


def recursion(number):

    if number > 5:
        return

    print(number)

    recursion(number + 1)


print("Using Recursion")

recursion(1)

print()

print("Using Loop")

for number in range(1, 6):
    print(number)