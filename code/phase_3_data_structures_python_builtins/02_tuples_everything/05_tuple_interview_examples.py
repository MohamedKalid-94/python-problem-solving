"""
=========================================================
Topic: Tuple Interview Examples and Real-World Problems
=========================================================

This file covers:

1. Swapping Variables
2. Returning Multiple Values from Functions
3. Using Tuples as Dictionary Keys
4. Finding Maximum and Minimum
5. Sorting List of Tuples
6. Employee Records
7. Coordinates Example
8. Enumerate (Returns Tuples)
9. Zip (Creates Tuples)
10. Frequently Asked Interview Questions

"""

def calculate(a, b):
    """
    Return multiple values.

    Python automatically packs them into a tuple.
    """

    return a + b, a - b, a * b


def main():

    # ==================================================
    # 1. Swapping Variables
    # ==================================================

    print("=" * 60)
    print("1. Swapping Variables")
    print("=" * 60)

    x = 10
    y = 20

    print("Before Swap")
    print("x =", x)
    print("y =", y)

    x, y = y, x

    print("\nAfter Swap")
    print("x =", x)
    print("y =", y)


    # ==================================================
    # 2. Returning Multiple Values
    # ==================================================

    print("\n" + "=" * 60)
    print("2. Returning Multiple Values")
    print("=" * 60)

    result = calculate(15, 5)

    print(result)

    addition, subtraction, multiplication = result

    print()

    print("Addition       :", addition)
    print("Subtraction    :", subtraction)
    print("Multiplication :", multiplication)


    # ==================================================
    # 3. Tuple as Dictionary Key
    # ==================================================

    print("\n" + "=" * 60)
    print("3. Tuple as Dictionary Key")
    print("=" * 60)

    seats = {

        (1, 1): "Reserved",

        (1, 2): "Available",

        (2, 1): "Reserved"

    }

    print(seats)

    print()

    print("Seat (1,2):")

    print(seats[(1, 2)])


    # ==================================================
    # 4. Maximum and Minimum
    # ==================================================

    print("\n" + "=" * 60)
    print("4. Maximum and Minimum")
    print("=" * 60)

    marks = (
        85,
        92,
        78,
        95,
        88
    )

    print("Marks:")

    print(marks)

    print()

    print("Highest:", max(marks))

    print("Lowest :", min(marks))

    print("Total  :", sum(marks))

    print("Average:", sum(marks) / len(marks))


    # ==================================================
    # 5. Sorting List of Tuples
    # ==================================================

    print("\n" + "=" * 60)
    print("5. Sorting List of Tuples")
    print("=" * 60)

    students = [

        ("Alice", 85),

        ("David", 95),

        ("Bob", 78),

        ("Chris", 90)

    ]

    print("Original")

    print(students)

    print()

    students.sort(key=lambda student: student[1])

    print("Sorted by Marks")

    print(students)


    # ==================================================
    # 6. Employee Records
    # ==================================================

    print("\n" + "=" * 60)
    print("6. Employee Records")
    print("=" * 60)

    employees = (

        (101, "Alice", "Developer"),

        (102, "Bob", "Tester"),

        (103, "Chris", "Manager")

    )

    for emp_id, name, role in employees:

        print(f"ID   : {emp_id}")
        print(f"Name : {name}")
        print(f"Role : {role}")
        print("-" * 25)


    # ==================================================
    # 7. Coordinates Example
    # ==================================================

    print("\n" + "=" * 60)
    print("7. Coordinates")
    print("=" * 60)

    point = (25, 75)

    x, y = point

    print("X =", x)

    print("Y =", y)


    # ==================================================
    # 8. Enumerate Returns Tuples
    # ==================================================

    print("\n" + "=" * 60)
    print("8. Enumerate")
    print("=" * 60)

    languages = [

        "Python",

        "Java",

        "C++"

    ]

    for index, language in enumerate(languages):

        print(index, language)


    # ==================================================
    # 9. Zip Creates Tuples
    # ==================================================

    print("\n" + "=" * 60)
    print("9. Zip Function")
    print("=" * 60)

    names = [

        "Alice",

        "Bob",

        "Chris"

    ]

    ages = [

        24,

        26,

        30

    ]

    for data in zip(names, ages):

        print(data)


    # ==================================================
    # 10. Interview Practice
    # ==================================================

    print("\n" + "=" * 60)
    print("10. Interview Practice")
    print("=" * 60)

    data = (

        10,

        20,

        30,

        40,

        50

    )

    print("Length :", len(data))

    print("Maximum:", max(data))

    print("Minimum:", min(data))

    print("Count of 20:", data.count(20))

    print("Index of 30:", data.index(30))


if __name__ == "__main__":
    main()