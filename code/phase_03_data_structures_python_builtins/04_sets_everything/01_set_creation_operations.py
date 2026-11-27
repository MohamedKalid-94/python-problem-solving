"""
=========================================================
Topic: Python Sets - Creation and Basic Operations
=========================================================

A Set is:

✔ Unordered
✔ Mutable
✔ Stores Unique Values
✔ No Duplicate Elements
✔ Fast Membership Testing (Average O(1))

Common Uses

• Remove duplicates
• Fast lookup
• Membership testing
• Mathematical set operations
• Finding common elements

"""

def main():

    # ==================================================
    # 1. Creating Sets
    # ==================================================

    print("=" * 60)
    print("1. Creating Sets")
    print("=" * 60)

    numbers = {10, 20, 30, 40}

    print(numbers)

    print(type(numbers))


    # ==================================================
    # 2. Empty Set
    # ==================================================

    print("\n" + "=" * 60)
    print("2. Empty Set")
    print("=" * 60)

    empty_set = set()

    print(empty_set)

    print(type(empty_set))

    # {} creates an empty dictionary, NOT a set.

    empty_dictionary = {}

    print(empty_dictionary)

    print(type(empty_dictionary))


    # ==================================================
    # 3. Duplicate Values
    # ==================================================

    print("\n" + "=" * 60)
    print("3. Duplicate Values")
    print("=" * 60)

    values = {

        10,

        20,

        20,

        30,

        30,

        40

    }

    print(values)

    print()

    print("Duplicate values are automatically removed.")


    # ==================================================
    # 4. Creating Set from List
    # ==================================================

    print("\n" + "=" * 60)
    print("4. List to Set")
    print("=" * 60)

    numbers = [

        10,

        20,

        20,

        30,

        30,

        40

    ]

    unique_numbers = set(numbers)

    print(unique_numbers)


    # ==================================================
    # 5. Creating Set from String
    # ==================================================

    print("\n" + "=" * 60)
    print("5. String to Set")
    print("=" * 60)

    language = "programming"

    letters = set(language)

    print(letters)


    # ==================================================
    # 6. Membership Operators
    # ==================================================

    print("\n" + "=" * 60)
    print("6. Membership Testing")
    print("=" * 60)

    fruits = {

        "Apple",

        "Orange",

        "Banana"

    }

    print(fruits)

    print()

    print("Apple" in fruits)

    print("Mango" in fruits)

    print("Mango" not in fruits)


    # ==================================================
    # 7. Length of Set
    # ==================================================

    print("\n" + "=" * 60)
    print("7. Length of Set")
    print("=" * 60)

    print(len(fruits))


    # ==================================================
    # 8. Iterating Through Set
    # ==================================================

    print("\n" + "=" * 60)
    print("8. Iterating Through Set")
    print("=" * 60)

    for fruit in fruits:

        print(fruit)


    # ==================================================
    # 9. Set with Different Data Types
    # ==================================================

    print("\n" + "=" * 60)
    print("9. Different Data Types")
    print("=" * 60)

    data = {

        100,

        3.14,

        "Python",

        True,

        (10, 20)

    }

    print(data)


    # ==================================================
    # 10. Real-World Example
    # ==================================================

    print("\n" + "=" * 60)
    print("10. Remove Duplicate Students")
    print("=" * 60)

    students = [

        "Alice",

        "Bob",

        "Chris",

        "Alice",

        "David",

        "Bob"

    ]

    print("Original List")

    print(students)

    unique_students = set(students)

    print()

    print("Unique Students")

    print(unique_students)


if __name__ == "__main__":
    main()