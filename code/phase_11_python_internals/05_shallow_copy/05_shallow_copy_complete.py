"""
=========================================================
Topic : Shallow Copy in Python

Covered:

1. What is Shallow Copy?
2. copy.copy()
3. Outer Object Copy
4. Nested Object Reference Sharing
5. Shallow Copy with Lists
6. Shallow Copy with Dictionaries
7. Shallow Copy vs Deep Copy
8. Real-World Applications

=========================================================
"""

import copy


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# 1. What is Shallow Copy?
# ---------------------------------------------------------

def shallow_copy_definition():
    separator("1. Shallow Copy Definition")

    print(
        """
Shallow copy creates a new outer object,
but nested objects are still shared.

Characteristics:

- New outer object
- Nested objects share references
- Faster than deep copy
- Changes in nested objects affect original
        """
    )


# ---------------------------------------------------------
# 2. Basic Shallow Copy Example
# ---------------------------------------------------------

def basic_shallow_copy_example():
    separator("2. Basic Shallow Copy Example")

    original = [1, 2, 3]

    copied = copy.copy(original)

    copied.append(4)

    print("Original:")
    print(original)

    print("\nCopied:")
    print(copied)

    print(
        "\nSame Object:",
        original is copied
    )


# ---------------------------------------------------------
# 3. Nested List Example
# ---------------------------------------------------------

def nested_list_example():
    separator("3. Nested List Shallow Copy")

    original = [
        [1, 2],
        [3, 4]
    ]

    copied = copy.copy(original)


    copied[0].append(100)


    print("Original:")
    print(original)


    print("\nCopied:")
    print(copied)


# ---------------------------------------------------------
# 4. Identity Check
# ---------------------------------------------------------

def identity_check_example():
    separator("4. Identity Check")


    original = [
        ["Python", "AI"],
        ["ML", "Data"]
    ]


    copied = copy.copy(original)


    print(
        "Outer Object Same:",
        original is copied
    )


    print(
        "Nested Object Same:",
        original[0] is copied[0]
    )


# ---------------------------------------------------------
# 5. Shallow Copy using copy() Method
# ---------------------------------------------------------

def list_copy_method_example():
    separator("5. List copy() Method")


    skills = [
        "Python",
        "SQL",
        "AI"
    ]


    copied_skills = skills.copy()


    copied_skills.append(
        "GenAI"
    )


    print("Original Skills:")

    print(skills)


    print("\nCopied Skills:")

    print(copied_skills)



# ---------------------------------------------------------
# 6. Dictionary Shallow Copy
# ---------------------------------------------------------

def dictionary_shallow_copy_example():

    separator(
        "6. Dictionary Shallow Copy"
    )


    employee = {

        "name":"Kalid",

        "skills":[
            "Python",
            "AI"
        ]

    }


    copied_employee = copy.copy(
        employee
    )


    copied_employee["skills"].append(
        "LangChain"
    )


    print(
        "Original Employee:"
    )

    print(employee)


    print(
        "\nCopied Employee:"
    )

    print(copied_employee)



# ---------------------------------------------------------
# 7. Shallow Copy vs Deep Copy
# ---------------------------------------------------------

def shallow_vs_deep_example():

    separator(
        "7. Shallow Copy vs Deep Copy"
    )


    original = [

        [
            1,
            2
        ]

    ]


    shallow = copy.copy(
        original
    )


    deep = copy.deepcopy(
        original
    )


    shallow[0].append(
        50
    )


    deep[0].append(
        100
    )


    print(
        "Original:"
    )

    print(original)


    print(
        "\nShallow:"
    )

    print(shallow)


    print(
        "\nDeep:"
    )

    print(deep)



# ---------------------------------------------------------
# 8. Performance Example
# ---------------------------------------------------------

def performance_example():

    separator(
        "8. Performance Concept"
    )


    print(
        """
Shallow Copy:

- Faster
- Uses less memory
- Suitable when nested objects
  do not need independence


Deep Copy:

- Slower
- Uses more memory
- Creates complete independent copy
        """
    )



# ---------------------------------------------------------
# 9. Real-World Example
# ---------------------------------------------------------

def real_world_example():

    separator(
        "9. Real-World Example - AI Pipeline Configuration"
    )


    pipeline_config = {

        "model":"LLM",

        "parameters":{

            "temperature":0.7,

            "top_p":0.9

        },

        "steps":[
            "Load",
            "Split",
            "Embed"
        ]

    }


    test_config = copy.copy(
        pipeline_config
    )


    test_config["parameters"]["temperature"] = 0.2


    test_config["steps"].append(
        "Retrieve"
    )


    print(
        "Production Config:"
    )

    print(
        pipeline_config
    )


    print(
        "\nTest Config:"
    )

    print(
        test_config
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    shallow_copy_definition()

    basic_shallow_copy_example()

    nested_list_example()

    identity_check_example()

    list_copy_method_example()

    dictionary_shallow_copy_example()

    shallow_vs_deep_example()

    performance_example()

    real_world_example()



if __name__ == "__main__":

    main()
    