"""
Topic:
Tuple vs List - Memory, Performance and Mutability

Concepts Covered:
1. List vs Tuple
2. Mutability
3. Memory Usage
4. Performance
5. Hashability
6. Dictionary Keys
7. id() Function
8. Practical Examples
9. Interview Questions

"""

import sys
import time


def main():

    # ==================================================
    # 1. Creating List and Tuple
    # ==================================================

    print("=" * 60)
    print("1. Creating List and Tuple")
    print("=" * 60)

    my_list = [10, 20, 30, 40]
    my_tuple = (10, 20, 30, 40)

    print("List :", my_list)
    print("Tuple:", my_tuple)


    # ==================================================
    # 2. Mutability
    # ==================================================

    print("\n" + "=" * 60)
    print("2. Mutability")
    print("=" * 60)

    print("Before Modification")

    print(my_list)

    my_list[0] = 100

    print("After Modification")

    print(my_list)

    print("\nTuple cannot be modified.")

    # Uncomment to see the error

    # my_tuple[0] = 100


    # ==================================================
    # 3. Memory Usage
    # ==================================================

    print("\n" + "=" * 60)
    print("3. Memory Usage")
    print("=" * 60)

    print("List Memory (Bytes):")
    print(sys.getsizeof(my_list))

    print()

    print("Tuple Memory (Bytes):")
    print(sys.getsizeof(my_tuple))

    print()

    print("Tuple generally uses less memory.")


    # ==================================================
    # 4. Performance Comparison
    # ==================================================

    print("\n" + "=" * 60)
    print("4. Performance")
    print("=" * 60)

    start = time.perf_counter()

    values = [i for i in range(100000)]

    end = time.perf_counter()

    print("List Creation Time:")
    print(end - start)

    start = time.perf_counter()

    values = tuple(i for i in range(100000))

    end = time.perf_counter()

    print()

    print("Tuple Creation Time:")
    print(end - start)

    print()

    print("Tuples are usually faster to create and iterate.")


    # ==================================================
    # 5. Memory Address
    # ==================================================

    print("\n" + "=" * 60)
    print("5. Memory Address")
    print("=" * 60)

    list1 = [1, 2, 3]
    tuple1 = (1, 2, 3)

    print("List ID :")
    print(id(list1))

    print()

    print("Tuple ID:")
    print(id(tuple1))


    # ==================================================
    # 6. Hashability
    # ==================================================

    print("\n" + "=" * 60)
    print("6. Hashability")
    print("=" * 60)

    coordinates = (10, 20)

    print("Hash Value:")

    print(hash(coordinates))

    print()

    print("Tuple is hashable because all elements are immutable.")

    print()

    # Uncomment to see the error

    # hash([10,20])


    # ==================================================
    # 7. Dictionary Keys
    # ==================================================

    print("\n" + "=" * 60)
    print("7. Tuple as Dictionary Key")
    print("=" * 60)

    locations = {

        (0, 0): "Origin",

        (1, 2): "Point A",

        (5, 8): "Point B"

    }

    print(locations)

    print()

    print(locations[(1, 2)])


    # ==================================================
    # 8. List Cannot Be Dictionary Key
    # ==================================================

    print("\n" + "=" * 60)
    print("8. Why List Cannot Be Dictionary Key")
    print("=" * 60)

    print("Lists are mutable.")

    print()

    print("Mutable objects cannot be hashed.")

    # Uncomment to see error

    # dictionary = {
    #     [1,2]: "Invalid"
    # }


    # ==================================================
    # 9. Practical Example
    # ==================================================

    print("\n" + "=" * 60)
    print("9. Practical Example")
    print("=" * 60)

    employee = (
        101,
        "Alice",
        "Developer",
        80000
    )

    print(employee)

    print()

    print("Employee records should not change frequently.")

    print("Tuple is a good choice.")


    # ==================================================
    # 10. Summary
    # ==================================================

    print("\n" + "=" * 60)
    print("10. Summary")
    print("=" * 60)

    print("List  -> Mutable")
    print("Tuple -> Immutable")

    print()

    print("List  -> More Memory")
    print("Tuple -> Less Memory")

    print()

    print("List  -> Cannot be Dictionary Key")
    print("Tuple -> Can be Dictionary Key (if immutable)")


if __name__ == "__main__":
    main()