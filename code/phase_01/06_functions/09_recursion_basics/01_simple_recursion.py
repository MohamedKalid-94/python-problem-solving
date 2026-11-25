"""
Topic: Simple Recursion

Problem:
Print numbers from 1 to 5 using recursion.
"""


def display(number):

    if number > 5:
        return

    print(number)

    display(number + 1)


display(1)