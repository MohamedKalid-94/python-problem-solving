"""
=========================================================
Custom Calculator Module

Reusable mathematical functions

=========================================================
"""


def add(a, b):

    return a + b



def subtract(a, b):

    return a - b



def multiply(a, b):

    return a * b



def divide(a, b):

    if b == 0:

        raise ValueError(
            "Cannot divide by zero"
        )

    return a / b



def calculate_sum(numbers):

    total = 0


    for number in numbers:

        total += number


    return total