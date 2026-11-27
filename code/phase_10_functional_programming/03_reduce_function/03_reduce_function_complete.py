"""
=========================================================
Topic : reduce() Function in Python

Covered:

1. Basic reduce()
2. reduce() with Lambda
3. reduce() with User-Defined Function
4. Finding Maximum Value
5. String Concatenation
6. Multiplication of Numbers
7. Real-World Example

=========================================================
"""

from functools import reduce


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# Basic reduce()
# ---------------------------------------------------------

def add(x, y):
    return x + y


def basic_reduce_example():
    separator("1. Basic reduce()")

    numbers = [10, 20, 30, 40]

    total = reduce(add, numbers)

    print("Sum:", total)


# ---------------------------------------------------------
# reduce() with Lambda
# ---------------------------------------------------------

def lambda_reduce_example():
    separator("2. reduce() with Lambda")

    numbers = [1, 2, 3, 4, 5]

    result = reduce(lambda x, y: x + y, numbers)

    print("Sum:", result)


# ---------------------------------------------------------
# reduce() with User-Defined Function
# ---------------------------------------------------------

def multiply(x, y):
    return x * y


def user_defined_function_example():
    separator("3. User-Defined Function")

    numbers = [2, 3, 4, 5]

    product = reduce(multiply, numbers)

    print("Product:", product)


# ---------------------------------------------------------
# Finding Maximum Value
# ---------------------------------------------------------

def maximum(x, y):
    return x if x > y else y


def maximum_value_example():
    separator("4. Finding Maximum Value")

    numbers = [45, 78, 12, 98, 35]

    max_number = reduce(maximum, numbers)

    print("Maximum:", max_number)


# ---------------------------------------------------------
# String Concatenation
# ---------------------------------------------------------

def concatenate_strings_example():
    separator("5. String Concatenation")

    words = ["Python", "is", "powerful"]

    sentence = reduce(lambda x, y: x + " " + y, words)

    print(sentence)


# ---------------------------------------------------------
# Multiplication of Numbers
# ---------------------------------------------------------

def multiplication_example():
    separator("6. Multiplication")

    numbers = [1, 2, 3, 4, 5]

    result = reduce(lambda x, y: x * y, numbers)

    print("Result:", result)


# ---------------------------------------------------------
# Real-World Example
# ---------------------------------------------------------

def real_world_example():
    separator("7. Shopping Cart Total")

    prices = [499, 999, 1499, 250]

    total_bill = reduce(lambda x, y: x + y, prices)

    print("Total Bill:", total_bill)


def main():
    basic_reduce_example()
    lambda_reduce_example()
    user_defined_function_example()
    maximum_value_example()
    concatenate_strings_example()
    multiplication_example()
    real_world_example()


if __name__ == "__main__":
    main()