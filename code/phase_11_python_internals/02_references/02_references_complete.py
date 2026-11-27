"""
=========================================================
Topic : References in Python

Covered:

1. Variables Store References
2. Multiple References to Same Object
3. Reference Sharing
4. Reference Comparison using is
5. Function Arguments and References
6. Reference Behavior with Mutable Objects
7. Reference Behavior with Immutable Objects
8. Real-World Examples

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# 1. Variables Store References
# ---------------------------------------------------------

def variable_reference_example():
    separator("1. Variables Store References")

    value = 100

    print("Value:", value)
    print("Object ID:", id(value))

    print(
        "Variable points to an object stored in memory."
    )


# ---------------------------------------------------------
# 2. Multiple References to Same Object
# ---------------------------------------------------------

def multiple_reference_example():
    separator("2. Multiple References")

    list1 = [10, 20, 30]

    list2 = list1

    print("list1:", list1)
    print("list2:", list2)

    print(
        "Same Object:",
        list1 is list2
    )

    print(
        "list1 ID:",
        id(list1)
    )

    print(
        "list2 ID:",
        id(list2)
    )


# ---------------------------------------------------------
# 3. Reference Sharing
# ---------------------------------------------------------

def reference_sharing_example():
    separator("3. Reference Sharing")

    original = [
        "Python",
        "AI"
    ]

    copy_reference = original

    copy_reference.append("ML")

    print("Original:", original)

    print("Reference Copy:", copy_reference)

    print(
        "Both variables changed the same object."
    )


# ---------------------------------------------------------
# 4. Reference Comparison using is
# ---------------------------------------------------------

def identity_operator_example():
    separator("4. Identity Operator (is)")

    a = [1, 2, 3]

    b = a

    c = [1, 2, 3]


    print("a == b:", a == b)

    print("a is b:", a is b)


    print("\na == c:", a == c)

    print("a is c:", a is c)


# ---------------------------------------------------------
# 5. Function Arguments and References
# ---------------------------------------------------------

def modify_list(data):

    data.append(100)


def function_reference_example():
    separator("5. Function Arguments and References")

    numbers = [1, 2, 3]

    print("Before Function Call:")
    print(numbers)

    modify_list(numbers)

    print("After Function Call:")
    print(numbers)


# ---------------------------------------------------------
# 6. Mutable Object Reference Behavior
# ---------------------------------------------------------

def mutable_reference_example():
    separator("6. Mutable Object Reference")

    user = {
        "name": "Kalid",
        "role": "AI Engineer"
    }

    profile = user

    profile["role"] = "GenAI Engineer"

    print("User:")
    print(user)

    print("\nProfile:")
    print(profile)


# ---------------------------------------------------------
# 7. Immutable Object Reference Behavior
# ---------------------------------------------------------

def immutable_reference_example():
    separator("7. Immutable Object Reference")

    a = 10

    b = a

    print("Before Change")

    print("a:", a)
    print("b:", b)

    b = 20

    print("\nAfter Change")

    print("a:", a)
    print("b:", b)

    print(
        "New object created because integer is immutable."
    )


# ---------------------------------------------------------
# 8. Function Reassignment Example
# ---------------------------------------------------------

def reassign_reference(data):

    data = [100, 200, 300]

    print(
        "Inside Function:",
        data
    )


def reassignment_example():
    separator("8. Reference Reassignment")

    numbers = [1, 2, 3]

    reassign_reference(numbers)

    print(
        "Outside Function:",
        numbers
    )


# ---------------------------------------------------------
# 9. Real-World Example
# ---------------------------------------------------------

def real_world_example():
    separator("9. Real-World Example - Configuration Sharing")

    config = {
        "database": "PostgreSQL",
        "cache": "Redis",
        "environment": "production"
    }

    service_config = config

    service_config["environment"] = "development"

    print("Main Config:")
    print(config)

    print("\nService Config:")
    print(service_config)


# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    variable_reference_example()

    multiple_reference_example()

    reference_sharing_example()

    identity_operator_example()

    function_reference_example()

    mutable_reference_example()

    immutable_reference_example()

    reassignment_example()

    real_world_example()


if __name__ == "__main__":
    main()