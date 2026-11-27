"""
=========================================================
Topic : Higher-Order Functions in Python

Covered:

1. Function as an Argument
2. Function Returning Another Function
3. Lambda with Higher-Order Function
4. Custom Calculator
5. Callback Functions
6. Built-in Higher-Order Functions
7. Real-World Example

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# Function as an Argument
# ---------------------------------------------------------

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def calculate(operation, a, b):
    return operation(a, b)


def function_argument_example():
    separator("1. Function as an Argument")

    print("Addition:", calculate(add, 10, 5))
    print("Subtraction:", calculate(subtract, 10, 5))


# ---------------------------------------------------------
# Function Returning Another Function
# ---------------------------------------------------------

def multiplier(factor):

    def multiply(number):
        return number * factor

    return multiply


def returning_function_example():
    separator("2. Function Returning Another Function")

    double = multiplier(2)
    triple = multiplier(3)

    print("Double of 10:", double(10))
    print("Triple of 10:", triple(10))


# ---------------------------------------------------------
# Lambda with Higher-Order Function
# ---------------------------------------------------------

def lambda_example():
    separator("3. Lambda with Higher-Order Function")

    numbers = [10, 20, 30, 40]

    doubled = list(map(lambda number: number * 2, numbers))

    print(doubled)


# ---------------------------------------------------------
# Custom Calculator
# ---------------------------------------------------------

def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def calculator_example():
    separator("4. Custom Calculator")

    print("Multiply:", calculate(multiply, 6, 4))
    print("Divide:", calculate(divide, 20, 5))


# ---------------------------------------------------------
# Callback Functions
# ---------------------------------------------------------

def completed():
    print("Task Completed Successfully")


def execute_task(callback):

    print("Executing Task...")
    callback()


def callback_example():
    separator("5. Callback Function")

    execute_task(completed)


# ---------------------------------------------------------
# Built-in Higher-Order Functions
# ---------------------------------------------------------

def builtin_functions_example():
    separator("6. Built-in Higher-Order Functions")

    numbers = [1, 2, 3, 4, 5]

    squares = list(map(lambda x: x * x, numbers))
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

    print("Squares:", squares)
    print("Even Numbers:", even_numbers)


# ---------------------------------------------------------
# Real-World Example
# ---------------------------------------------------------

def apply_discount(price):
    return round(price * 0.90, 2)


def process_prices(function, prices):
    return list(map(function, prices))


def real_world_example():
    separator("7. E-Commerce Discount System")

    prices = [1000, 2500, 3200, 4500]

    discounted_prices = process_prices(
        apply_discount,
        prices
    )

    print("Original Prices :", prices)
    print("Discounted Prices:", discounted_prices)


# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():
    function_argument_example()
    returning_function_example()
    lambda_example()
    calculator_example()
    callback_example()
    builtin_functions_example()
    real_world_example()


if __name__ == "__main__":
    main()