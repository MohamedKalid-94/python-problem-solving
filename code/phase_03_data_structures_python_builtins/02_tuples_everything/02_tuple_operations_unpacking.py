"""
Topic:
Python Tuples - Operations and Unpacking

Concepts Covered:
1. Tuple Packing
2. Tuple Unpacking
3. Multiple Assignment
4. Swapping Variables
5. Joining Tuples
6. Repeating Tuples
7. Membership Operators
8. Tuple Methods
9. Built-in Functions

"""

def main():

    # ==================================================
    # 1. Tuple Packing
    # ==================================================

    print("=" * 60)
    print("1. Tuple Packing")
    print("=" * 60)

    # Parentheses are optional
    person = "John", 25, "Engineer"

    print("Packed Tuple:")
    print(person)

    print(type(person))


    # ==================================================
    # 2. Tuple Unpacking
    # ==================================================

    print("\n" + "=" * 60)
    print("2. Tuple Unpacking")
    print("=" * 60)

    student = ("Alice", 22, "Python")

    name, age, course = student

    print("Name   :", name)
    print("Age    :", age)
    print("Course :", course)


    # ==================================================
    # 3. Multiple Assignment
    # ==================================================

    print("\n" + "=" * 60)
    print("3. Multiple Assignment")
    print("=" * 60)

    x, y, z = 10, 20, 30

    print("x =", x)
    print("y =", y)
    print("z =", z)


    # ==================================================
    # 4. Swapping Variables
    # ==================================================

    print("\n" + "=" * 60)
    print("4. Swapping Variables")
    print("=" * 60)

    a = 100
    b = 200

    print("Before Swap")
    print("a =", a)
    print("b =", b)

    a, b = b, a

    print("\nAfter Swap")
    print("a =", a)
    print("b =", b)


    # ==================================================
    # 5. Joining Tuples
    # ==================================================

    print("\n" + "=" * 60)
    print("5. Joining Tuples")
    print("=" * 60)

    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)

    joined = tuple1 + tuple2

    print(joined)


    # ==================================================
    # 6. Repeating Tuples
    # ==================================================

    print("\n" + "=" * 60)
    print("6. Repeating Tuples")
    print("=" * 60)

    values = ("Python",)

    print(values * 5)


    # ==================================================
    # 7. Membership Operators
    # ==================================================

    print("\n" + "=" * 60)
    print("7. Membership Operators")
    print("=" * 60)

    fruits = (
        "Apple",
        "Orange",
        "Banana",
        "Mango"
    )

    print("Apple" in fruits)

    print("Grapes" in fruits)

    print("Kiwi" not in fruits)


    # ==================================================
    # 8. Tuple Methods
    # ==================================================

    print("\n" + "=" * 60)
    print("8. Tuple Methods")
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
    # 9. Built-in Functions
    # ==================================================

    print("\n" + "=" * 60)
    print("9. Built-in Functions")
    print("=" * 60)

    values = (
        5,
        10,
        15,
        20
    )

    print("Length :", len(values))
    print("Maximum:", max(values))
    print("Minimum:", min(values))
    print("Sum     :", sum(values))


    # ==================================================
    # 10. Extended Unpacking
    # ==================================================

    print("\n" + "=" * 60)
    print("10. Extended Unpacking")
    print("=" * 60)

    numbers = (
        10,
        20,
        30,
        40,
        50
    )

    first, *middle, last = numbers

    print("First :", first)
    print("Middle:", middle)
    print("Last  :", last)


    # ==================================================
    # 11. Practical Example
    # ==================================================

    print("\n" + "=" * 60)
    print("11. Practical Example")
    print("=" * 60)

    employee = (
        101,
        "David",
        "AI Engineer",
        85000
    )

    emp_id, name, role, salary = employee

    print("Employee ID :", emp_id)
    print("Name        :", name)
    print("Role        :", role)
    print("Salary      :", salary)


if __name__ == "__main__":
    main()