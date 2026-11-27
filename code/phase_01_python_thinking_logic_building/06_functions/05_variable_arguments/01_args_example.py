"""
Topic: *args

Problem:
Accept multiple numbers.
"""


def add_numbers(*numbers):

    total = 0

    for number in numbers:
        total += number

    print("Sum:", total)


add_numbers(10, 20, 30, 40)