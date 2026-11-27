"""
=========================================================
Topic : any() Function in Python

Covered:

1. Basic any()
2. any() with Numbers
3. any() with Strings
4. any() with List of Conditions
5. any() with Generator Expression
6. any() with Dictionary
7. Real-World Example

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# Basic any()
# ---------------------------------------------------------

def basic_any_example():
    separator("1. Basic any()")

    values = [False, False, True, False]

    print(any(values))


# ---------------------------------------------------------
# any() with Numbers
# ---------------------------------------------------------

def numbers_example():
    separator("2. any() with Numbers")

    numbers = [0, 0, 5, 0]

    print(any(numbers))


# ---------------------------------------------------------
# any() with Strings
# ---------------------------------------------------------

def strings_example():
    separator("3. any() with Strings")

    words = ["", "", "Python", ""]

    print(any(words))


# ---------------------------------------------------------
# any() with List of Conditions
# ---------------------------------------------------------

def conditions_example():
    separator("4. any() with Conditions")

    marks = [35, 42, 68, 28, 90]

    passed = any(mark >= 50 for mark in marks)

    print("Any student passed:", passed)


# ---------------------------------------------------------
# any() with Generator Expression
# ---------------------------------------------------------

def generator_expression_example():
    separator("5. Generator Expression")

    numbers = [2, 4, 6, 8, 9]

    has_odd = any(number % 2 != 0 for number in numbers)

    print("Contains Odd Number:", has_odd)


# ---------------------------------------------------------
# any() with Dictionary
# ---------------------------------------------------------

def dictionary_example():
    separator("6. Dictionary Example")

    employee = {
        "name": "Kalid",
        "email": "",
        "phone": ""
    }

    has_contact = any(employee[field] for field in ["email", "phone"])

    print("Contact Available:", has_contact)


# ---------------------------------------------------------
# Real-World Example
# ---------------------------------------------------------

def real_world_example():
    separator("7. Login Permission Check")

    users = [
        {"name": "John", "is_admin": False},
        {"name": "Alice", "is_admin": False},
        {"name": "David", "is_admin": True},
        {"name": "Sara", "is_admin": False}
    ]

    admin_exists = any(user["is_admin"] for user in users)

    print("Administrator Available:", admin_exists)


def main():
    basic_any_example()
    numbers_example()
    strings_example()
    conditions_example()
    generator_expression_example()
    dictionary_example()
    real_world_example()


if __name__ == "__main__":
    main()