"""
=========================================================
Topic : all() Function in Python

Covered:

1. Basic all()
2. all() with Numbers
3. all() with Strings
4. all() with List of Conditions
5. all() with Generator Expression
6. all() with Dictionary
7. Real-World Example

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# Basic all()
# ---------------------------------------------------------

def basic_all_example():
    separator("1. Basic all()")

    values = [True, True, True, True]

    print(all(values))


# ---------------------------------------------------------
# all() with Numbers
# ---------------------------------------------------------

def numbers_example():
    separator("2. all() with Numbers")

    numbers = [10, 20, 30, 40]

    print(all(numbers))

    numbers = [10, 20, 0, 40]

    print(all(numbers))


# ---------------------------------------------------------
# all() with Strings
# ---------------------------------------------------------

def strings_example():
    separator("3. all() with Strings")

    words = ["Python", "AI", "ML"]

    print(all(words))

    words = ["Python", "", "ML"]

    print(all(words))


# ---------------------------------------------------------
# all() with List of Conditions
# ---------------------------------------------------------

def conditions_example():
    separator("4. all() with Conditions")

    marks = [65, 72, 81, 90]

    all_passed = all(mark >= 50 for mark in marks)

    print("All Students Passed:", all_passed)


# ---------------------------------------------------------
# all() with Generator Expression
# ---------------------------------------------------------

def generator_expression_example():
    separator("5. Generator Expression")

    numbers = [2, 4, 6, 8, 10]

    all_even = all(number % 2 == 0 for number in numbers)

    print("All Numbers Even:", all_even)


# ---------------------------------------------------------
# all() with Dictionary
# ---------------------------------------------------------

def dictionary_example():
    separator("6. Dictionary Example")

    employee = {
        "name": "Kalid",
        "email": "kalid@example.com",
        "phone": "9876543210"
    }

    details_complete = all(employee.values())

    print("All Details Available:", details_complete)


# ---------------------------------------------------------
# Real-World Example
# ---------------------------------------------------------

def real_world_example():
    separator("7. Student Eligibility Check")

    students = [
        {"name": "John", "attendance": 85},
        {"name": "Alice", "attendance": 92},
        {"name": "David", "attendance": 78},
        {"name": "Sara", "attendance": 88}
    ]

    eligible = all(student["attendance"] >= 75 for student in students)

    print("All Students Eligible:", eligible)


def main():
    basic_all_example()
    numbers_example()
    strings_example()
    conditions_example()
    generator_expression_example()
    dictionary_example()
    real_world_example()


if __name__ == "__main__":
    main()