"""
Topic:
Python Tuples - Nested Tuples, Methods and Iteration

Concepts Covered:
1. Nested Tuples
2. Accessing Nested Elements
3. Iterating Through Tuples
4. Iterating Through Nested Tuples
5. Tuple Methods
6. Membership Operators
7. Tuple Slicing
8. Real-World Examples

"""

def main():

    # ==================================================
    # 1. Nested Tuples
    # ==================================================

    print("=" * 60)
    print("1. Nested Tuples")
    print("=" * 60)

    students = (
        ("Alice", 21, "Python"),
        ("Bob", 22, "Java"),
        ("Charlie", 20, "AI")
    )

    print(students)


    # ==================================================
    # 2. Accessing Nested Elements
    # ==================================================

    print("\n" + "=" * 60)
    print("2. Accessing Nested Elements")
    print("=" * 60)

    print("First Student:")
    print(students[0])

    print("\nFirst Student Name:")
    print(students[0][0])

    print("\nSecond Student Course:")
    print(students[1][2])

    print("\nThird Student Age:")
    print(students[2][1])


    # ==================================================
    # 3. Iterating Through Tuple
    # ==================================================

    print("\n" + "=" * 60)
    print("3. Tuple Iteration")
    print("=" * 60)

    colors = (
        "Red",
        "Green",
        "Blue"
    )

    for color in colors:
        print(color)


    # ==================================================
    # 4. Iterating Through Nested Tuples
    # ==================================================

    print("\n" + "=" * 60)
    print("4. Nested Tuple Iteration")
    print("=" * 60)

    for student in students:
        print(student)

    print("\nUsing Tuple Unpacking\n")

    for name, age, course in students:
        print(f"Name   : {name}")
        print(f"Age    : {age}")
        print(f"Course : {course}")
        print("-" * 30)


    # ==================================================
    # 5. Tuple Methods
    # ==================================================

    print("\n" + "=" * 60)
    print("5. Tuple Methods")
    print("=" * 60)

    numbers = (
        10,
        20,
        30,
        20,
        40,
        20
    )

    print("Tuple:")
    print(numbers)

    print("\nCount of 20:")
    print(numbers.count(20))

    print("\nIndex of 30:")
    print(numbers.index(30))


    # ==================================================
    # 6. Membership Operators
    # ==================================================

    print("\n" + "=" * 60)
    print("6. Membership Operators")
    print("=" * 60)

    print(20 in numbers)
    print(100 in numbers)
    print(100 not in numbers)


    # ==================================================
    # 7. Tuple Slicing
    # ==================================================

    print("\n" + "=" * 60)
    print("7. Tuple Slicing")
    print("=" * 60)

    values = (
        10,
        20,
        30,
        40,
        50,
        60
    )

    print("Original:")
    print(values)

    print("\nFirst Three:")
    print(values[:3])

    print("\nMiddle:")
    print(values[2:5])

    print("\nReverse:")
    print(values[::-1])


    # ==================================================
    # 8. Real-World Example - Student Records
    # ==================================================

    print("\n" + "=" * 60)
    print("8. Student Records")
    print("=" * 60)

    students = (
        ("John", 89),
        ("David", 95),
        ("Alex", 78),
        ("Sara", 92)
    )

    for name, marks in students:

        print(f"{name:<10} {marks}")


    # ==================================================
    # 9. Real-World Example - Employee Records
    # ==================================================

    print("\n" + "=" * 60)
    print("9. Employee Records")
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
    # 10. Tuple Length
    # ==================================================

    print("\n" + "=" * 60)
    print("10. Tuple Length")
    print("=" * 60)

    print("Number of Employees:")
    print(len(employees))


if __name__ == "__main__":
    main()