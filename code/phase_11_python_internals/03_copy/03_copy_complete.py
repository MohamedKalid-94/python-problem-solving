"""
=========================================================
Topic : Copy in Python

Covered:

1. Assignment Copy
2. Reference Copy Behavior
3. Shallow Copy Introduction
4. Deep Copy Introduction
5. copy() Method
6. List Copy Techniques
7. Copy with Nested Objects
8. Real-World Example

=========================================================
"""

import copy


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# 1. Assignment Copy
# ---------------------------------------------------------

def assignment_copy_example():
    separator("1. Assignment Copy")

    original = [1, 2, 3]

    copied = original

    print("Original:", original)
    print("Copied:", copied)

    print(
        "Same Object:",
        original is copied
    )


# ---------------------------------------------------------
# 2. Reference Copy Behavior
# ---------------------------------------------------------

def reference_copy_behavior():
    separator("2. Reference Copy Behavior")

    numbers = [10, 20, 30]

    reference = numbers

    reference.append(40)

    print("Original:", numbers)

    print("Reference:", reference)

    print(
        "Both variables point to same list."
    )


# ---------------------------------------------------------
# 3. Shallow Copy Introduction
# ---------------------------------------------------------

def shallow_copy_intro():
    separator("3. Shallow Copy Introduction")

    original = [1, 2, 3]

    copied = original.copy()

    copied.append(4)

    print("Original:", original)

    print("Copied:", copied)

    print(
        "Different Objects:",
        original is copied
    )


# ---------------------------------------------------------
# 4. Deep Copy Introduction
# ---------------------------------------------------------

def deep_copy_intro():
    separator("4. Deep Copy Introduction")

    original = [
        [1, 2],
        [3, 4]
    ]

    copied = copy.deepcopy(original)

    copied[0].append(100)

    print("Original:")
    print(original)

    print("\nDeep Copy:")
    print(copied)


# ---------------------------------------------------------
# 5. copy() Method
# ---------------------------------------------------------

def copy_method_example():
    separator("5. List copy() Method")

    fruits = [
        "Apple",
        "Banana",
        "Orange"
    ]

    new_fruits = fruits.copy()

    new_fruits.append("Mango")

    print("Original:", fruits)

    print("New:", new_fruits)


# ---------------------------------------------------------
# 6. Copy using Slicing
# ---------------------------------------------------------

def slicing_copy_example():
    separator("6. Copy using Slicing")

    numbers = [1, 2, 3, 4]

    copied = numbers[:]

    copied.append(5)

    print("Original:", numbers)

    print("Copied:", copied)


# ---------------------------------------------------------
# 7. Copy with Nested Objects
# ---------------------------------------------------------

def nested_object_copy_example():
    separator("7. Copy with Nested Objects")

    original = [
        ["Python", "AI"],
        ["ML", "Data"]
    ]

    shallow = copy.copy(original)

    shallow[0].append("GenAI")

    print("Original:")
    print(original)

    print("\nShallow Copy:")
    print(shallow)


# ---------------------------------------------------------
# 8. Dictionary Copy
# ---------------------------------------------------------

def dictionary_copy_example():
    separator("8. Dictionary Copy")

    employee = {
        "name": "Kalid",
        "skills": [
            "Python",
            "AI"
        ]
    }

    copied_employee = employee.copy()

    copied_employee["name"] = "Mohamed"

    print("Original:")
    print(employee)

    print("\nCopied:")
    print(copied_employee)


# ---------------------------------------------------------
# 9. Copy Comparison
# ---------------------------------------------------------

def comparison_example():
    separator("9. Copy Comparison")

    original = [1, 2, 3]

    assignment = original

    shallow = copy.copy(original)

    deep = copy.deepcopy(original)


    print(
        "Assignment:",
        original is assignment
    )

    print(
        "Shallow:",
        original is shallow
    )

    print(
        "Deep:",
        original is deep
    )


# ---------------------------------------------------------
# 10. Real-World Example
# ---------------------------------------------------------

def real_world_example():
    separator("10. Real-World Example - AI Configuration")

    model_config = {
        "model": "LLM",
        "parameters": {
            "temperature": 0.7,
            "max_tokens": 1000
        }
    }

    backup_config = copy.deepcopy(model_config)

    backup_config["parameters"]["temperature"] = 0.2


    print("Original Configuration:")
    print(model_config)

    print("\nBackup Configuration:")
    print(backup_config)


# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    assignment_copy_example()

    reference_copy_behavior()

    shallow_copy_intro()

    deep_copy_intro()

    copy_method_example()

    slicing_copy_example()

    nested_object_copy_example()

    dictionary_copy_example()

    comparison_example()

    real_world_example()


if __name__ == "__main__":
    main()