"""
=========================================================
Topic : Key Functions in Python

Covered:

1. Basic key Function
2. Sorting Strings by Length
3. Sorting Tuples
4. Sorting Dictionaries
5. key with min()
6. key with max()
7. Real-World Example

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# Basic key Function
# ---------------------------------------------------------

def basic_key_example():
    separator("1. Basic key Function")

    numbers = [-10, 5, -3, 20, -15]

    result = sorted(numbers, key=abs)

    print(result)


# ---------------------------------------------------------
# Sorting Strings by Length
# ---------------------------------------------------------

def string_length_example():
    separator("2. Sorting Strings by Length")

    languages = [
        "Python",
        "C",
        "Java",
        "JavaScript",
        "Go"
    ]

    result = sorted(languages, key=len)

    print(result)


# ---------------------------------------------------------
# Sorting Tuples
# ---------------------------------------------------------

def tuple_sorting_example():
    separator("3. Sorting Tuples")

    students = [
        ("John", 85),
        ("Alice", 92),
        ("David", 76),
        ("Sara", 88)
    ]

    sorted_students = sorted(
        students,
        key=lambda student: student[1]
    )

    print(sorted_students)


# ---------------------------------------------------------
# Sorting Dictionaries
# ---------------------------------------------------------

def dictionary_sorting_example():
    separator("4. Sorting Dictionaries")

    employees = [
        {"name": "John", "salary": 55000},
        {"name": "Alice", "salary": 72000},
        {"name": "David", "salary": 48000},
        {"name": "Sara", "salary": 65000}
    ]

    sorted_employees = sorted(
        employees,
        key=lambda employee: employee["salary"]
    )

    for employee in sorted_employees:
        print(employee)


# ---------------------------------------------------------
# key with min()
# ---------------------------------------------------------

def minimum_example():
    separator("5. key with min()")

    words = [
        "Python",
        "AI",
        "MachineLearning",
        "RAG"
    ]

    shortest = min(words, key=len)

    print("Shortest Word:", shortest)


# ---------------------------------------------------------
# key with max()
# ---------------------------------------------------------

def maximum_example():
    separator("6. key with max()")

    words = [
        "Python",
        "AI",
        "MachineLearning",
        "RAG"
    ]

    longest = max(words, key=len)

    print("Longest Word:", longest)


# ---------------------------------------------------------
# Real-World Example
# ---------------------------------------------------------

def real_world_example():
    separator("7. Student Ranking System")

    students = [
        {"name": "John", "marks": 82},
        {"name": "Alice", "marks": 95},
        {"name": "David", "marks": 76},
        {"name": "Sara", "marks": 89}
    ]

    ranking = sorted(
        students,
        key=lambda student: student["marks"],
        reverse=True
    )

    print("Student Rankings")
    print("-" * 40)

    for rank, student in enumerate(ranking, start=1):
        print(
            f"{rank}. {student['name']} - {student['marks']} Marks"
        )


def main():
    basic_key_example()
    string_length_example()
    tuple_sorting_example()
    dictionary_sorting_example()
    minimum_example()
    maximum_example()
    real_world_example()


if __name__ == "__main__":
    main()