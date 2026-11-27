"""
=========================================================
Topic: Dictionary Interview Examples
=========================================================

Concepts Covered

1. Character Frequency
2. Word Frequency
3. Find Maximum Value
4. Merge Dictionaries
5. Sort Dictionary
6. Invert Dictionary
7. Group Data
8. Count Duplicate Elements
9. Real-World Example
10. Most Asked Interview Questions

"""

from collections import defaultdict


def main():

    # ==================================================
    # 1. Character Frequency
    # ==================================================

    print("=" * 60)
    print("1. Character Frequency")
    print("=" * 60)

    text = "python"

    frequency = {}

    for character in text:

        frequency[character] = frequency.get(character, 0) + 1

    print(frequency)


    # ==================================================
    # 2. Word Frequency
    # ==================================================

    print("\n" + "=" * 60)
    print("2. Word Frequency")
    print("=" * 60)

    sentence = "python is easy python is powerful"

    words = sentence.split()

    word_frequency = {}

    for word in words:

        word_frequency[word] = word_frequency.get(word, 0) + 1

    print(word_frequency)


    # ==================================================
    # 3. Find Maximum Value
    # ==================================================

    print("\n" + "=" * 60)
    print("3. Highest Salary")
    print("=" * 60)

    employees = {

        "Alice": 75000,

        "Bob": 90000,

        "Chris": 82000,

        "David": 95000

    }

    highest_employee = max(employees, key=employees.get)

    print("Highest Paid Employee")

    print(highest_employee)

    print(employees[highest_employee])


    # ==================================================
    # 4. Merge Dictionaries
    # ==================================================

    print("\n" + "=" * 60)
    print("4. Merge Dictionaries")
    print("=" * 60)

    dictionary1 = {

        "A": 1,

        "B": 2

    }

    dictionary2 = {

        "C": 3,

        "D": 4

    }

    merged = dictionary1 | dictionary2

    print(merged)


    # ==================================================
    # 5. Sort Dictionary by Key
    # ==================================================

    print("\n" + "=" * 60)
    print("5. Sort by Key")
    print("=" * 60)

    products = {

        "Mouse": 600,

        "Laptop": 65000,

        "Keyboard": 1200

    }

    sorted_keys = dict(sorted(products.items()))

    print(sorted_keys)


    # ==================================================
    # 6. Sort Dictionary by Value
    # ==================================================

    print("\n" + "=" * 60)
    print("6. Sort by Value")
    print("=" * 60)

    sorted_values = dict(

        sorted(

            products.items(),

            key=lambda item: item[1]

        )

    )

    print(sorted_values)


    # ==================================================
    # 7. Invert Dictionary
    # ==================================================

    print("\n" + "=" * 60)
    print("7. Invert Dictionary")
    print("=" * 60)

    countries = {

        "IN": "India",

        "US": "United States",

        "JP": "Japan"

    }

    inverted = {

        value: key

        for key, value in countries.items()

    }

    print(inverted)


    # ==================================================
    # 8. Group Students
    # ==================================================

    print("\n" + "=" * 60)
    print("8. Group Students")
    print("=" * 60)

    students = [

        ("Alice", "Python"),

        ("Bob", "AI"),

        ("Chris", "Python"),

        ("David", "Java")

    ]

    grouped = defaultdict(list)

    for name, course in students:

        grouped[course].append(name)

    print(dict(grouped))


    # ==================================================
    # 9. Count Duplicate Numbers
    # ==================================================

    print("\n" + "=" * 60)
    print("9. Duplicate Detection")
    print("=" * 60)

    numbers = [

        10,

        20,

        30,

        20,

        10,

        10,

        40

    ]

    frequency = {}

    for number in numbers:

        frequency[number] = frequency.get(number, 0) + 1

    duplicates = {}

    for key, value in frequency.items():

        if value > 1:

            duplicates[key] = value

    print(frequency)

    print()

    print("Duplicates")

    print(duplicates)


    # ==================================================
    # 10. Inventory Example
    # ==================================================

    print("\n" + "=" * 60)
    print("10. Inventory Management")
    print("=" * 60)

    inventory = {

        "Laptop": 10,

        "Mouse": 35,

        "Keyboard": 20

    }

    print("Before Sale")

    print(inventory)

    inventory["Laptop"] -= 1

    inventory["Mouse"] += 10

    print()

    print("After Update")

    print(inventory)


if __name__ == "__main__":
    main()