"""
=========================================================
Topic: Python Dictionaries - Update, Delete and Methods
=========================================================

Concepts Covered:
1. Adding Key-Value Pairs
2. Updating Existing Values
3. update()
4. setdefault()
5. pop()
6. popitem()
7. del Statement
8. clear()
9. copy()
10. fromkeys()
11. Real-World Examples

"""

def main():

    # ==================================================
    # 1. Adding New Items
    # ==================================================

    print("=" * 60)
    print("1. Adding New Items")
    print("=" * 60)

    student = {
        "id": 101,
        "name": "Alice"
    }

    print("Original Dictionary")
    print(student)

    student["age"] = 22
    student["course"] = "Python"

    print("\nAfter Adding")
    print(student)


    # ==================================================
    # 2. Updating Existing Values
    # ==================================================

    print("\n" + "=" * 60)
    print("2. Updating Existing Values")
    print("=" * 60)

    student["age"] = 23
    student["course"] = "AI"

    print(student)


    # ==================================================
    # 3. update()
    # ==================================================

    print("\n" + "=" * 60)
    print("3. update()")
    print("=" * 60)

    employee = {
        "id": 201,
        "name": "John"
    }

    print("Before Update")
    print(employee)

    employee.update({
        "department": "AI",
        "salary": 85000
    })

    print("\nAfter update()")
    print(employee)

    employee.update({
        "salary": 90000
    })

    print("\nUpdated Salary")
    print(employee)


    # ==================================================
    # 4. setdefault()
    # ==================================================

    print("\n" + "=" * 60)
    print("4. setdefault()")
    print("=" * 60)

    laptop = {
        "brand": "Dell"
    }

    print(laptop)

    # Adds key because it doesn't exist
    laptop.setdefault("RAM", "16 GB")

    print("\nAfter setdefault()")
    print(laptop)

    # Does nothing because key exists
    laptop.setdefault("RAM", "32 GB")

    print("\nExisting Key")
    print(laptop)


    # ==================================================
    # 5. pop()
    # ==================================================

    print("\n" + "=" * 60)
    print("5. pop()")
    print("=" * 60)

    person = {
        "name": "David",
        "age": 30,
        "city": "Chennai"
    }

    print(person)

    removed = person.pop("age")

    print("\nRemoved Value:", removed)

    print(person)

    # pop with default value
    value = person.pop("country", "Not Found")

    print("\nCountry:", value)


    # ==================================================
    # 6. popitem()
    # ==================================================

    print("\n" + "=" * 60)
    print("6. popitem()")
    print("=" * 60)

    product = {
        "id": 1,
        "name": "Laptop",
        "price": 65000
    }

    print(product)

    last_item = product.popitem()

    print("\nRemoved Item")
    print(last_item)

    print("\nRemaining Dictionary")
    print(product)


    # ==================================================
    # 7. del Statement
    # ==================================================

    print("\n" + "=" * 60)
    print("7. del Statement")
    print("=" * 60)

    car = {
        "brand": "Toyota",
        "model": "Innova",
        "year": 2024
    }

    print(car)

    del car["year"]

    print("\nAfter del")
    print(car)


    # ==================================================
    # 8. clear()
    # ==================================================

    print("\n" + "=" * 60)
    print("8. clear()")
    print("=" * 60)

    marks = {
        "Math": 95,
        "Science": 90
    }

    print(marks)

    marks.clear()

    print("\nAfter clear()")
    print(marks)


    # ==================================================
    # 9. copy()
    # ==================================================

    print("\n" + "=" * 60)
    print("9. copy()")
    print("=" * 60)

    original = {
        "A": 1,
        "B": 2
    }

    copied = original.copy()

    print("Original")
    print(original)

    print("\nCopied")
    print(copied)

    copied["A"] = 100

    print("\nAfter Modification")

    print("Original")
    print(original)

    print("Copied")
    print(copied)


    # ==================================================
    # 10. fromkeys()
    # ==================================================

    print("\n" + "=" * 60)
    print("10. fromkeys()")
    print("=" * 60)

    keys = [
        "Python",
        "Java",
        "AI"
    ]

    courses = dict.fromkeys(keys, "Available")

    print(courses)


    # ==================================================
    # 11. Real-World Example
    # ==================================================

    print("\n" + "=" * 60)
    print("11. Employee Database")
    print("=" * 60)

    employee = {
        "id": 101,
        "name": "Alice",
        "department": "Software",
        "salary": 75000
    }

    print("Original")
    print(employee)

    employee["salary"] = 85000

    employee["location"] = "Bangalore"

    employee.pop("department")

    print("\nUpdated Employee")
    print(employee)


if __name__ == "__main__":
    main()