"""
=========================================================
Topic : sorted() Function in Python

Covered:

1. Basic sorted()
2. Ascending Order
3. Descending Order
4. Sorting Strings
5. Sorting Tuples
6. Sorting Dictionary Data
7. Real-World Example

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# Basic sorted()
# ---------------------------------------------------------

def basic_sorted_example():
    separator("1. Basic sorted()")

    numbers = [5, 2, 8, 1, 9, 3]

    result = sorted(numbers)

    print(result)


# ---------------------------------------------------------
# Ascending Order
# ---------------------------------------------------------

def ascending_order_example():
    separator("2. Ascending Order")

    marks = [78, 92, 65, 84, 55]

    print(sorted(marks))


# ---------------------------------------------------------
# Descending Order
# ---------------------------------------------------------

def descending_order_example():
    separator("3. Descending Order")

    marks = [78, 92, 65, 84, 55]

    print(sorted(marks, reverse=True))


# ---------------------------------------------------------
# Sorting Strings
# ---------------------------------------------------------

def sorting_strings_example():
    separator("4. Sorting Strings")

    languages = [
        "Python",
        "Java",
        "C",
        "Go",
        "Rust"
    ]

    print(sorted(languages))


# ---------------------------------------------------------
# Sorting Tuples
# ---------------------------------------------------------

def sorting_tuples_example():
    separator("5. Sorting Tuples")

    students = [
        ("John", 85),
        ("Alice", 92),
        ("David", 76),
        ("Sara", 88)
    ]

    result = sorted(students)

    print(result)


# ---------------------------------------------------------
# Sorting Dictionary Data
# ---------------------------------------------------------

def sorting_dictionary_example():
    separator("6. Sorting Dictionary Data")

    student_marks = {
        "John": 85,
        "Alice": 92,
        "David": 76,
        "Sara": 88
    }

    print("Sorted Keys:")
    print(sorted(student_marks))

    print("\nSorted Values:")
    print(sorted(student_marks.values()))

    print("\nSorted Items:")
    print(sorted(student_marks.items()))


# ---------------------------------------------------------
# Real-World Example
# ---------------------------------------------------------

def real_world_example():
    separator("7. Employee Salary Report")

    employees = [
        {"name": "John", "salary": 55000},
        {"name": "Alice", "salary": 72000},
        {"name": "David", "salary": 48000},
        {"name": "Sara", "salary": 65000}
    ]

    sorted_employees = sorted(
        employees,
        key=lambda employee: employee["salary"],
        reverse=True
    )

    print("Employees Sorted by Salary")

    print("-" * 40)

    for employee in sorted_employees:
        print(
            employee["name"],
            "- ₹",
            employee["salary"]
        )


def main():
    basic_sorted_example()
    ascending_order_example()
    descending_order_example()
    sorting_strings_example()
    sorting_tuples_example()
    sorting_dictionary_example()
    real_world_example()


if __name__ == "__main__":
    main()