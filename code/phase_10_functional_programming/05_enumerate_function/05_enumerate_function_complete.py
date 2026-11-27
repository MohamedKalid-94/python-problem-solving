"""
=========================================================
Topic : enumerate() Function in Python

Covered:

1. Basic enumerate()
2. enumerate() with Start Index
3. Iterating with Index and Value
4. Converting enumerate to List
5. enumerate() with String
6. enumerate() with Dictionary
7. Real-World Example

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# Basic enumerate()
# ---------------------------------------------------------

def basic_enumerate_example():
    separator("1. Basic enumerate()")

    languages = ["Python", "Java", "C++", "Go"]

    result = enumerate(languages)

    print(list(result))


# ---------------------------------------------------------
# enumerate() with Start Index
# ---------------------------------------------------------

def start_index_example():
    separator("2. enumerate() with Start Index")

    fruits = ["Apple", "Banana", "Orange"]

    for index, fruit in enumerate(fruits, start=1):
        print(index, "-", fruit)


# ---------------------------------------------------------
# Iterating with Index and Value
# ---------------------------------------------------------

def index_value_example():
    separator("3. Iterating with Index and Value")

    cities = ["Bangalore", "Chennai", "Mumbai", "Delhi"]

    for index, city in enumerate(cities):
        print(f"Index: {index}, City: {city}")


# ---------------------------------------------------------
# Converting enumerate to List
# ---------------------------------------------------------

def list_conversion_example():
    separator("4. Convert enumerate() to List")

    colors = ["Red", "Green", "Blue"]

    result = list(enumerate(colors))

    print(result)


# ---------------------------------------------------------
# enumerate() with String
# ---------------------------------------------------------

def string_example():
    separator("5. enumerate() with String")

    text = "Python"

    for index, character in enumerate(text):
        print(index, "->", character)


# ---------------------------------------------------------
# enumerate() with Dictionary
# ---------------------------------------------------------

def dictionary_example():
    separator("6. enumerate() with Dictionary")

    student = {
        "Name": "Kalid",
        "Age": 28,
        "Course": "Python"
    }

    for index, (key, value) in enumerate(student.items(), start=1):
        print(index, "-", key, ":", value)


# ---------------------------------------------------------
# Real-World Example
# ---------------------------------------------------------

def real_world_example():
    separator("7. Student Rank List")

    students = [
        "John",
        "Alice",
        "David",
        "Sara",
        "Kalid"
    ]

    print("Rank List")
    print("-" * 30)

    for rank, student in enumerate(students, start=1):
        print(f"Rank {rank}: {student}")


def main():
    basic_enumerate_example()
    start_index_example()
    index_value_example()
    list_conversion_example()
    string_example()
    dictionary_example()
    real_world_example()


if __name__ == "__main__":
    main()