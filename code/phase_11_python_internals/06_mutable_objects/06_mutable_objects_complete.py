"""
=========================================================
Topic : Mutable Objects in Python

Covered:

1. What are Mutable Objects?
2. List Mutation
3. Dictionary Mutation
4. Set Mutation
5. Object Identity After Mutation
6. Mutable Objects with References
7. Mutable Objects in Functions
8. Real-World Examples

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# 1. What are Mutable Objects?
# ---------------------------------------------------------

def mutable_definition():
    separator("1. Mutable Object Definition")

    print(
        """
Mutable objects are objects whose values
can be changed after creation.

Examples:

- list
- dictionary
- set
- bytearray

The object identity remains the same
after modification.
        """
    )


# ---------------------------------------------------------
# 2. List Mutation
# ---------------------------------------------------------

def list_mutation_example():
    separator("2. List Mutation")

    numbers = [1, 2, 3]

    print("Before:")
    print(numbers)

    print("ID Before:")
    print(id(numbers))


    numbers.append(4)

    print("\nAfter:")
    print(numbers)

    print("ID After:")
    print(id(numbers))


    print(
        "\nSame Object:",
        id(numbers)
    )


# ---------------------------------------------------------
# 3. Dictionary Mutation
# ---------------------------------------------------------

def dictionary_mutation_example():

    separator(
        "3. Dictionary Mutation"
    )


    employee = {

        "name":"Kalid",

        "role":"Python Developer"

    }


    print(
        "Before:"
    )

    print(employee)


    employee["role"] = (
        "AI Engineer"
    )


    employee["experience"] = 8


    print(
        "\nAfter:"
    )

    print(employee)



# ---------------------------------------------------------
# 4. Set Mutation
# ---------------------------------------------------------

def set_mutation_example():

    separator(
        "4. Set Mutation"
    )


    technologies = {

        "Python",
        "SQL",
        "AI"

    }


    print(
        "Before:"
    )

    print(technologies)


    technologies.add(
        "GenAI"
    )


    technologies.remove(
        "SQL"
    )


    print(
        "\nAfter:"
    )

    print(technologies)



# ---------------------------------------------------------
# 5. Object Identity After Mutation
# ---------------------------------------------------------

def identity_after_mutation():

    separator(
        "5. Identity After Mutation"
    )


    data = [
        10,
        20,
        30
    ]


    old_id = id(data)


    data.append(
        40
    )


    new_id = id(data)


    print(
        "Old ID:",
        old_id
    )


    print(
        "New ID:",
        new_id
    )


    print(
        "Same Object:",
        old_id == new_id
    )



# ---------------------------------------------------------
# 6. Mutable Objects with References
# ---------------------------------------------------------

def reference_example():

    separator(
        "6. Mutable Objects and References"
    )


    original = {

        "skills":[
            "Python",
            "SQL"
        ]

    }


    reference = original


    reference["skills"].append(
        "AI"
    )


    print(
        "Original:"
    )

    print(original)


    print(
        "\nReference:"
    )

    print(reference)



# ---------------------------------------------------------
# 7. Mutable Objects in Functions
# ---------------------------------------------------------

def add_skill(skills):

    skills.append(
        "Machine Learning"
    )



def function_mutation_example():

    separator(
        "7. Mutable Objects in Functions"
    )


    skills = [

        "Python",
        "SQL"

    ]


    print(
        "Before Function:"
    )

    print(skills)


    add_skill(
        skills
    )


    print(
        "\nAfter Function:"
    )

    print(skills)



# ---------------------------------------------------------
# 8. Mutable Default Argument Problem
# ---------------------------------------------------------

def add_item(item, items=[]):

    items.append(item)

    return items



def mutable_default_argument_example():

    separator(
        "8. Mutable Default Argument Problem"
    )


    print(
        add_item("Python")
    )


    print(
        add_item("AI")
    )


    print(
        """
Problem:
Default list is created once and
shared between function calls.
        """
    )



# ---------------------------------------------------------
# 9. Avoid Mutable Default Argument
# ---------------------------------------------------------

def safe_add_item(item, items=None):

    if items is None:

        items = []


    items.append(item)

    return items



def safe_solution_example():

    separator(
        "9. Safe Solution"
    )


    print(
        safe_add_item("Python")
    )


    print(
        safe_add_item("AI")
    )



# ---------------------------------------------------------
# 10. Real-World Example
# ---------------------------------------------------------

def real_world_example():

    separator(
        "10. Real-World Example - AI Pipeline State"
    )


    pipeline_state = {

        "documents": [],

        "embeddings": [],

        "status":"started"

    }


    pipeline_state["documents"].append(
        "python.pdf"
    )


    pipeline_state["embeddings"].append(
        [0.12,0.34,0.56]
    )


    pipeline_state["status"] = (
        "completed"
    )


    print(
        pipeline_state
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    mutable_definition()

    list_mutation_example()

    dictionary_mutation_example()

    set_mutation_example()

    identity_after_mutation()

    reference_example()

    function_mutation_example()

    mutable_default_argument_example()

    safe_solution_example()

    real_world_example()



if __name__ == "__main__":

    main()