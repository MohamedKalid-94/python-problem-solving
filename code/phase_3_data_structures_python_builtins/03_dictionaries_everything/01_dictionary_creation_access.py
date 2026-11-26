"""
=========================================================
Topic: Python Dictionaries - Creation and Access
=========================================================

A Dictionary is:

✔ Ordered (Python 3.7+)
✔ Mutable
✔ Stores data as Key : Value pairs
✔ Keys must be unique
✔ Values can be duplicated
✔ Fast lookup (Average O(1))

Examples:
Student Records
Employee Details
Configuration Files
JSON Data
API Responses

"""

def main():

    # ==================================================
    # 1. Creating Dictionaries
    # ==================================================

    print("=" * 60)
    print("1. Creating Dictionaries")
    print("=" * 60)

    # Empty dictionary
    empty_dict = {}

    print("Empty Dictionary")
    print(empty_dict)

    print(type(empty_dict))

    # Dictionary with data
    student = {
        "id": 101,
        "name": "Alice",
        "age": 22,
        "course": "Python"
    }

    print("\nStudent Dictionary")
    print(student)

    # Using dict() constructor
    employee = dict(
        id=201,
        name="John",
        role="Developer"
    )

    print("\nEmployee Dictionary")
    print(employee)

    # ==================================================
    # 2. Accessing Values
    # ==================================================

    print("\n" + "=" * 60)
    print("2. Accessing Values")
    print("=" * 60)

    person = {
        "name": "David",
        "age": 30,
        "city": "Chennai"
    }

    print(person)

    print("\nUsing Square Brackets")
    print(person["name"])
    print(person["age"])

    print("\nUsing get()")
    print(person.get("city"))

    # get() returns None if key doesn't exist
    print(person.get("country"))

    # get() with default value
    print(person.get("country", "India"))

    # ==================================================
    # 3. Difference Between [] and get()
    # ==================================================

    print("\n" + "=" * 60)
    print("3. [] vs get()")
    print("=" * 60)

    student = {
        "name": "Alice",
        "marks": 95
    }

    print(student["name"])

    print(student.get("marks"))

    print(student.get("grade"))

    # Uncomment to see KeyError
    # print(student["grade"])

    # ==================================================
    # 4. Dictionary Keys
    # ==================================================

    print("\n" + "=" * 60)
    print("4. Dictionary Keys")
    print("=" * 60)

    laptop = {
        "brand": "Dell",
        "ram": "16 GB",
        "price": 65000
    }

    print(laptop.keys())

    print(list(laptop.keys()))

    # ==================================================
    # 5. Dictionary Values
    # ==================================================

    print("\n" + "=" * 60)
    print("5. Dictionary Values")
    print("=" * 60)

    print(laptop.values())

    print(list(laptop.values()))

    # ==================================================
    # 6. Dictionary Items
    # ==================================================

    print("\n" + "=" * 60)
    print("6. Dictionary Items")
    print("=" * 60)

    print(laptop.items())

    print(list(laptop.items()))

    # ==================================================
    # 7. Length of Dictionary
    # ==================================================

    print("\n" + "=" * 60)
    print("7. Dictionary Length")
    print("=" * 60)

    print(len(laptop))

    # ==================================================
    # 8. Membership Operators
    # ==================================================

    print("\n" + "=" * 60)
    print("8. Membership Operators")
    print("=" * 60)

    print("brand" in laptop)

    print("model" in laptop)

    print("model" not in laptop)

    # Membership checks ONLY keys

    print(65000 in laptop)

    # ==================================================
    # 9. Different Types of Keys
    # ==================================================

    print("\n" + "=" * 60)
    print("9. Valid Dictionary Keys")
    print("=" * 60)

    data = {

        1: "Integer Key",

        3.14: "Float Key",

        True: "Boolean Key",

        "Python": "String Key",

        (10, 20): "Tuple Key"

    }

    print(data)

    # ==================================================
    # 10. Duplicate Keys
    # ==================================================

    print("\n" + "=" * 60)
    print("10. Duplicate Keys")
    print("=" * 60)

    duplicate = {

        "name": "Alice",

        "name": "Bob"

    }

    print(duplicate)

    print("Latest value replaces previous value.")

    # ==================================================
    # 11. Real-World Example
    # ==================================================

    print("\n" + "=" * 60)
    print("11. Employee Record")
    print("=" * 60)

    employee = {

        "id": 101,

        "name": "John",

        "department": "AI",

        "salary": 85000,

        "location": "Bangalore"

    }

    print(employee)

    print()

    print("Employee Name:")
    print(employee["name"])

    print()

    print("Employee Salary:")
    print(employee["salary"])


if __name__ == "__main__":
    main()