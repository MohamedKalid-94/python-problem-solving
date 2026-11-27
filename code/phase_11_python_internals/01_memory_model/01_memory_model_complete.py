"""
=========================================================
Topic : Python Memory Model

Covered:

1. Variables and Objects
2. Object Creation
3. Reference Counting
4. Memory Address using id()
5. Multiple References
6. Garbage Collection
7. Memory Optimization Examples

=========================================================
"""

import sys
import gc


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# 1. Variables and Objects
# ---------------------------------------------------------

def variables_and_objects_example():
    separator("1. Variables and Objects")

    number = 100

    print("Value:", number)
    print("Object ID:", id(number))

    print(
        "Python variable stores a reference to an object."
    )


# ---------------------------------------------------------
# 2. Object Creation
# ---------------------------------------------------------

def object_creation_example():
    separator("2. Object Creation")

    name = "Python"

    numbers = [1, 2, 3]

    print("String Object ID:", id(name))
    print("List Object ID:", id(numbers))

    print(
        "Every object has:",
        "\n- Type",
        "\n- Value",
        "\n- Memory Identity"
    )


# ---------------------------------------------------------
# 3. Reference Counting
# ---------------------------------------------------------

def reference_counting_example():
    separator("3. Reference Counting")

    data = [10, 20, 30]

    print(
        "Initial Reference Count:",
        sys.getrefcount(data)
    )

    another_reference = data

    print(
        "After Second Reference:",
        sys.getrefcount(data)
    )

    del another_reference

    print(
        "After Removing Reference:",
        sys.getrefcount(data)
    )


# ---------------------------------------------------------
# 4. Memory Address using id()
# ---------------------------------------------------------

def identity_example():
    separator("4. Memory Identity")

    a = 50
    b = a

    print("a value:", a)
    print("b value:", b)

    print("a id:", id(a))
    print("b id:", id(b))

    print("Same Object:", a is b)


# ---------------------------------------------------------
# 5. Multiple References
# ---------------------------------------------------------

def multiple_reference_example():
    separator("5. Multiple References")

    list1 = [1, 2, 3]

    list2 = list1

    print("Before Modification:")
    print("list1:", list1)
    print("list2:", list2)

    list2.append(4)

    print("\nAfter Modification:")
    print("list1:", list1)
    print("list2:", list2)

    print(
        "\nBoth variables reference the same object."
    )


# ---------------------------------------------------------
# 6. Garbage Collection
# ---------------------------------------------------------

def garbage_collection_example():
    separator("6. Garbage Collection")

    class Student:

        def __del__(self):
            print("Object destroyed")

    student = Student()

    del student

    print(
        "Python automatically manages unused objects."
    )

    gc.collect()


# ---------------------------------------------------------
# 7. Mutable Object Memory Behavior
# ---------------------------------------------------------

def mutable_memory_example():
    separator("7. Mutable Object Memory")

    numbers = [1, 2, 3]

    old_id = id(numbers)

    numbers.append(4)

    new_id = id(numbers)

    print("Old ID:", old_id)
    print("New ID:", new_id)

    print(
        "Same object after modification:",
        old_id == new_id
    )


# ---------------------------------------------------------
# 8. Immutable Object Memory Behavior
# ---------------------------------------------------------

def immutable_memory_example():
    separator("8. Immutable Object Memory")

    name = "Python"

    old_id = id(name)

    name = name + " AI"

    new_id = id(name)

    print("Old ID:", old_id)
    print("New ID:", new_id)

    print(
        "New object created:",
        old_id != new_id
    )


# ---------------------------------------------------------
# 9. Memory Optimization
# ---------------------------------------------------------

def memory_optimization_example():
    separator("9. Memory Optimization")

    # Bad approach
    numbers = [x for x in range(100000)]

    print(
        "List stores all values in memory:",
        len(numbers)
    )

    # Better approach
    generator = (x for x in range(100000))

    print(
        "Generator creates values when required:"
    )

    print(next(generator))
    print(next(generator))


# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    variables_and_objects_example()

    object_creation_example()

    reference_counting_example()

    identity_example()

    multiple_reference_example()

    garbage_collection_example()

    mutable_memory_example()

    immutable_memory_example()

    memory_optimization_example()


if __name__ == "__main__":
    main()