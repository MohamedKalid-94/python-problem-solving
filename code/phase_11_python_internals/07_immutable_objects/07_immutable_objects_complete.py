"""
=========================================================
Topic : Immutable Objects in Python

Covered:

1. What are Immutable Objects?
2. Integer Immutability
3. String Immutability
4. Tuple Immutability
5. Object Identity with Immutable Objects
6. Immutable Objects and References
7. Hashable Immutable Objects
8. Real-World Examples

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# 1. What are Immutable Objects?
# ---------------------------------------------------------

def immutable_definition():
    separator("1. Immutable Object Definition")

    print(
        """
Immutable objects are objects whose value
cannot be changed after creation.

If we modify them, Python creates
a new object.

Examples:

- int
- float
- bool
- str
- tuple
- frozenset
        """
    )


# ---------------------------------------------------------
# 2. Integer Immutability
# ---------------------------------------------------------

def integer_immutability_example():
    separator("2. Integer Immutability")

    number = 100

    old_id = id(number)

    print("Before:")
    print(number)
    print("ID:", old_id)


    number = number + 50


    new_id = id(number)


    print("\nAfter:")
    print(number)
    print("ID:", new_id)


    print(
        "\nNew Object Created:",
        old_id != new_id
    )


# ---------------------------------------------------------
# 3. String Immutability
# ---------------------------------------------------------

def string_immutability_example():

    separator(
        "3. String Immutability"
    )


    text = "Python"


    old_id = id(text)


    print(
        "Before:"
    )

    print(text)


    text = text + " AI"


    new_id = id(text)


    print(
        "\nAfter:"
    )

    print(text)


    print(
        "\nNew Object Created:",
        old_id != new_id
    )



# ---------------------------------------------------------
# 4. Tuple Immutability
# ---------------------------------------------------------

def tuple_immutability_example():

    separator(
        "4. Tuple Immutability"
    )


    languages = (
        "Python",
        "Java",
        "Go"
    )


    print(
        "Original Tuple:"
    )

    print(languages)


    try:

        languages[0] = "C++"

    except TypeError as error:

        print(
            "\nError:",
            error
        )



# ---------------------------------------------------------
# 5. Object Identity
# ---------------------------------------------------------

def identity_example():

    separator(
        "5. Identity with Immutable Objects"
    )


    a = 10

    b = a


    print(
        "a ID:",
        id(a)
    )


    print(
        "b ID:",
        id(b)
    )


    print(
        "Same Object:",
        a is b
    )



# ---------------------------------------------------------
# 6. Immutable Objects and References
# ---------------------------------------------------------

def reference_example():

    separator(
        "6. Immutable References"
    )


    x = 100

    y = x


    print(
        "Before Change"
    )

    print(
        "x:",
        x
    )

    print(
        "y:",
        y
    )


    y = 200


    print(
        "\nAfter Change"
    )


    print(
        "x:",
        x
    )


    print(
        "y:",
        y
    )


    print(
        "\nOriginal object is not modified."
    )



# ---------------------------------------------------------
# 7. Hashable Immutable Objects
# ---------------------------------------------------------

def hashing_example():

    separator(
        "7. Immutable Objects and Hashing"
    )


    name = "Python"


    number = 100


    tuple_data = (
        1,
        2,
        3
    )


    print(
        "String Hash:",
        hash(name)
    )


    print(
        "Integer Hash:",
        hash(number)
    )


    print(
        "Tuple Hash:",
        hash(tuple_data)
    )


# ---------------------------------------------------------
# 8. Immutable Objects as Dictionary Keys
# ---------------------------------------------------------

def dictionary_key_example():

    separator(
        "8. Immutable Objects as Keys"
    )


    user_data = {

        "name":"Kalid",

        101:"Employee ID",

        (1,2):"Coordinates"

    }


    print(
        user_data
    )


# ---------------------------------------------------------
# 9. Mutable Inside Immutable Object
# ---------------------------------------------------------

def tuple_with_mutable_object_example():

    separator(
        "9. Tuple with Mutable Object"
    )


    data = (

        [1,2,3],

        "Python"

    )


    data[0].append(
        4
    )


    print(
        data
    )


    print(
        """
Tuple cannot change its references,
but mutable objects inside it can change.
        """
    )



# ---------------------------------------------------------
# 10. Real-World Example
# ---------------------------------------------------------

def real_world_example():

    separator(
        "10. Real-World Example - AI Configuration"
    )


    model_name = "GPT"


    version = "5.0"


    print(
        "Model:",
        model_name
    )


    print(
        "Version:",
        version
    )


    print(
        """
Strings are immutable,
so configuration values are safely stored
without accidental modification.
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    immutable_definition()

    integer_immutability_example()

    string_immutability_example()

    tuple_immutability_example()

    identity_example()

    reference_example()

    hashing_example()

    dictionary_key_example()

    tuple_with_mutable_object_example()

    real_world_example()



if __name__ == "__main__":

    main()