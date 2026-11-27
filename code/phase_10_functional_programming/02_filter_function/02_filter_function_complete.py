"""
=========================================================
Topic : filter() Function in Python

Covered:

1. Basic filter()
2. filter() with Lambda
3. filter() with User-Defined Function
4. Filtering Strings
5. Filtering Dictionary Data
6. Removing Empty Values
7. Real-World Example

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# Basic filter()
# ---------------------------------------------------------

def is_even(number):
    return number % 2 == 0


def basic_filter_example():
    separator("1. Basic filter()")

    numbers = [1, 2, 3, 4, 5, 6]

    even_numbers = filter(is_even, numbers)

    print(list(even_numbers))


# ---------------------------------------------------------
# filter() with Lambda
# ---------------------------------------------------------

def lambda_filter_example():
    separator("2. filter() with Lambda")

    numbers = [10, 15, 20, 25, 30]

    result = filter(lambda number: number > 20, numbers)

    print(list(result))


# ---------------------------------------------------------
# filter() with User-Defined Function
# ---------------------------------------------------------

def is_pass(mark):
    return mark >= 50


def user_defined_function_example():
    separator("3. User-Defined Function")

    marks = [35, 50, 67, 42, 89, 95]

    passed_students = filter(is_pass, marks)

    print(list(passed_students))


# ---------------------------------------------------------
# Filtering Strings
# ---------------------------------------------------------

def string_filter_example():
    separator("4. Filtering Strings")

    names = [
        "Python",
        "",
        "AI",
        "",
        "Machine Learning",
        "RAG"
    ]

    valid_names = filter(None, names)

    print(list(valid_names))


# ---------------------------------------------------------
# Filtering Dictionary Data
# ---------------------------------------------------------

def dictionary_filter_example():
    separator("5. Filtering Dictionary Data")

    students = [
        {"name": "John", "marks": 80},
        {"name": "Alice", "marks": 45},
        {"name": "David", "marks": 72},
        {"name": "Sara", "marks": 39}
    ]

    passed_students = filter(lambda student: student["marks"] >= 50, students)

    print(list(passed_students))


# ---------------------------------------------------------
# Removing Empty Values
# ---------------------------------------------------------

def remove_empty_values_example():
    separator("6. Removing Empty Values")

    data = [0, "", None, "Python", [], 100, False, "AI"]

    cleaned_data = filter(None, data)

    print(list(cleaned_data))


# ---------------------------------------------------------
# Real-World Example
# ---------------------------------------------------------

def real_world_example():
    separator("7. E-Commerce Order Filter")

    orders = [
        {"id": 101, "amount": 250},
        {"id": 102, "amount": 1200},
        {"id": 103, "amount": 3500},
        {"id": 104, "amount": 500}
    ]

    high_value_orders = filter(lambda order: order["amount"] >= 1000, orders)

    print(list(high_value_orders))


def main():
    basic_filter_example()
    lambda_filter_example()
    user_defined_function_example()
    string_filter_example()
    dictionary_filter_example()
    remove_empty_values_example()
    real_world_example()


if __name__ == "__main__":
    main()