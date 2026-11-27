"""
=========================================================
Topic : Generator Expressions in Python

Covered:

1. Generator Expression Syntax
2. Generator vs List Comprehension
3. Iterating Generator Expressions
4. Conditional Generator Expressions
5. Memory Efficiency
6. Real-World Example

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# Generator Expression Syntax
# ---------------------------------------------------------

def basic_generator_expression_example():
    separator("1. Basic Generator Expression")

    numbers = (number for number in range(1, 6))

    print(numbers)

    for number in numbers:
        print(number)


# ---------------------------------------------------------
# List Comprehension vs Generator Expression
# ---------------------------------------------------------

def list_vs_generator_example():
    separator("2. List vs Generator")

    list_numbers = [number * 2 for number in range(5)]

    generator_numbers = (number * 2 for number in range(5))

    print("List:", list_numbers)
    print("Generator:", generator_numbers)

    print("Generator Values:")

    for number in generator_numbers:
        print(number)


# ---------------------------------------------------------
# next() with Generator Expression
# ---------------------------------------------------------

def next_function_example():
    separator("3. next() with Generator Expression")

    squares = (number * number for number in range(1, 6))

    print(next(squares))
    print(next(squares))
    print(next(squares))


# ---------------------------------------------------------
# Conditional Generator Expression
# ---------------------------------------------------------

def conditional_generator_example():
    separator("4. Conditional Generator Expression")

    even_numbers = (number for number in range(1, 11) if number % 2 == 0)

    for number in even_numbers:
        print(number)


# ---------------------------------------------------------
# Multiple Conditions
# ---------------------------------------------------------

def multiple_condition_example():
    separator("5. Multiple Conditions")

    values = (
        number
        for number in range(1, 20)
        if number % 2 == 0 and number % 3 == 0
    )

    for value in values:
        print(value)


# ---------------------------------------------------------
# Memory Efficiency
# ---------------------------------------------------------

def memory_efficiency_example():
    separator("6. Memory Efficiency")

    list_values = [number for number in range(100000)]

    generator_values = (number for number in range(100000))

    print("List created with all values in memory.")
    print("Generator creates values one by one.")

    print("First Generator Value:", next(generator_values))


# ---------------------------------------------------------
# Generator Functions with Expression
# ---------------------------------------------------------

def calculate_prices(prices):
    return (price * 1.18 for price in prices)


def generator_function_expression_example():
    separator("7. Processing Data")

    prices = [100, 200, 300]

    updated_prices = calculate_prices(prices)

    for price in updated_prices:
        print(price)


# ---------------------------------------------------------
# Real-World Example
# ---------------------------------------------------------

def real_world_example():
    separator("8. Real-World Data Processing")

    transactions = [
        {"id": 1, "amount": 500},
        {"id": 2, "amount": 1500},
        {"id": 3, "amount": 2500},
        {"id": 4, "amount": 300}
    ]

    large_transactions = (
        transaction
        for transaction in transactions
        if transaction["amount"] > 1000
    )

    for transaction in large_transactions:
        print(transaction)


def main():
    basic_generator_expression_example()
    list_vs_generator_example()
    next_function_example()
    conditional_generator_example()
    multiple_condition_example()
    memory_efficiency_example()
    generator_function_expression_example()
    real_world_example()


if __name__ == "__main__":
    main()