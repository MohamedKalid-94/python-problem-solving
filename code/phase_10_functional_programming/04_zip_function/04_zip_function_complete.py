"""
=========================================================
Topic : zip() Function in Python

Covered:

1. Basic zip()
2. Iterating over zip()
3. zip() with Multiple Iterables
4. Converting zip to Dictionary
5. Unzipping Data
6. Different Length Iterables
7. Real-World Example

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# Basic zip()
# ---------------------------------------------------------

def basic_zip_example():
    separator("1. Basic zip()")

    names = ["John", "Alice", "David"]
    ages = [25, 30, 28]

    result = zip(names, ages)

    print(list(result))


# ---------------------------------------------------------
# Iterating over zip()
# ---------------------------------------------------------

def iterate_zip_example():
    separator("2. Iterating over zip()")

    names = ["Python", "Java", "C++"]
    years = [1991, 1995, 1985]

    for language, year in zip(names, years):
        print(language, "-", year)


# ---------------------------------------------------------
# zip() with Multiple Iterables
# ---------------------------------------------------------

def multiple_iterables_example():
    separator("3. Multiple Iterables")

    names = ["John", "Alice", "David"]
    ages = [25, 30, 28]
    cities = ["London", "Paris", "New York"]

    result = zip(names, ages, cities)

    for name, age, city in result:
        print(name, age, city)


# ---------------------------------------------------------
# Converting zip() to Dictionary
# ---------------------------------------------------------

def zip_to_dictionary_example():
    separator("4. zip() to Dictionary")

    keys = ["name", "age", "city"]
    values = ["Kalid", 28, "Bangalore"]

    person = dict(zip(keys, values))

    print(person)


# ---------------------------------------------------------
# Unzipping Data
# ---------------------------------------------------------

def unzip_example():
    separator("5. Unzipping Data")

    students = [
        ("John", 80),
        ("Alice", 90),
        ("David", 85)
    ]

    names, marks = zip(*students)

    print("Names:", names)
    print("Marks:", marks)


# ---------------------------------------------------------
# Different Length Iterables
# ---------------------------------------------------------

def different_length_example():
    separator("6. Different Length Iterables")

    numbers = [1, 2, 3]
    letters = ["A", "B"]

    result = zip(numbers, letters)

    print(list(result))

    print("\nzip() stops when the shortest iterable is exhausted.")


# ---------------------------------------------------------
# Real-World Example
# ---------------------------------------------------------

def real_world_example():
    separator("7. Student Report")

    students = ["John", "Alice", "David", "Sara"]
    marks = [82, 91, 76, 88]
    grades = ["A", "A+", "B+", "A"]

    report = zip(students, marks, grades)

    print("Student Report")
    print("-" * 40)

    for student, mark, grade in report:
        print(f"Name : {student}")
        print(f"Marks: {mark}")
        print(f"Grade: {grade}")
        print("-" * 40)


def main():
    basic_zip_example()
    iterate_zip_example()
    multiple_iterables_example()
    zip_to_dictionary_example()
    unzip_example()
    different_length_example()
    real_world_example()


if __name__ == "__main__":
    main()