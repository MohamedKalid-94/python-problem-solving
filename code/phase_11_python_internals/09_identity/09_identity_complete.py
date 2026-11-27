"""
=========================================================
Topic : Identity in Python

Covered:

1. What is Object Identity?
2. id() Function
3. is Operator
4. Difference Between == and is
5. Identity with Immutable Objects
6. Identity with Mutable Objects
7. Object Interning
8. Identity in Functions
9. Real-World Applications

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# 1. What is Object Identity?
# ---------------------------------------------------------

def identity_definition():
    separator("1. Object Identity Definition")

    print(
        """
Object identity represents the unique existence
of an object in Python memory.

Every object has:

1. Type
2. Value
3. Identity

Identity can be checked using:

id()
is operator
        """
    )


# ---------------------------------------------------------
# 2. id() Function
# ---------------------------------------------------------

def id_function_example():
    separator("2. id() Function Example")


    number = 100

    text = "Python"


    print(
        "Number:",
        number
    )

    print(
        "Number ID:",
        id(number)
    )


    print(
        "\nText:",
        text
    )

    print(
        "Text ID:",
        id(text)
    )



# ---------------------------------------------------------
# 3. is Operator
# ---------------------------------------------------------

def is_operator_example():

    separator(
        "3. is Operator"
    )


    list1 = [
        1,
        2,
        3
    ]


    list2 = list1


    list3 = [
        1,
        2,
        3
    ]


    print(
        "list1 is list2:",
        list1 is list2
    )


    print(
        "list1 is list3:",
        list1 is list3
    )



# ---------------------------------------------------------
# 4. Difference Between == and is
# ---------------------------------------------------------

def equality_vs_identity_example():

    separator(
        "4. == vs is"
    )


    a = [
        10,
        20
    ]


    b = [
        10,
        20
    ]


    print(
        "a == b:",
        a == b
    )


    print(
        "a is b:",
        a is b
    )


    print(
        """
== checks values.

is checks whether both variables
point to the same object.
        """
    )



# ---------------------------------------------------------
# 5. Identity with Immutable Objects
# ---------------------------------------------------------

def immutable_identity_example():

    separator(
        "5. Immutable Object Identity"
    )


    a = 100

    b = 100


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


    print(
        """
Python may reuse objects for
small immutable values.
        """
    )



# ---------------------------------------------------------
# 6. Identity with Mutable Objects
# ---------------------------------------------------------

def mutable_identity_example():

    separator(
        "6. Mutable Object Identity"
    )


    list1 = [
        "Python",
        "AI"
    ]


    list2 = list1


    list3 = [
        "Python",
        "AI"
    ]


    print(
        "list1 is list2:",
        list1 is list2
    )


    print(
        "list1 is list3:",
        list1 is list3
    )


    list2.append(
        "ML"
    )


    print(
        "\nlist1:",
        list1
    )


    print(
        "list2:",
        list2
    )



# ---------------------------------------------------------
# 7. Object Interning
# ---------------------------------------------------------

def object_interning_example():

    separator(
        "7. Object Interning"
    )


    a = "Python"

    b = "Python"


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


    print(
        """
Python may optimize memory by
reusing immutable objects.
        """
    )



# ---------------------------------------------------------
# 8. Identity in Functions
# ---------------------------------------------------------

def modify_data(data):

    print(
        "Inside Function ID:",
        id(data)
    )


def function_identity_example():

    separator(
        "8. Identity in Functions"
    )


    values = [
        1,
        2,
        3
    ]


    print(
        "Outside Function ID:",
        id(values)
    )


    modify_data(
        values
    )



# ---------------------------------------------------------
# 9. None Identity Check
# ---------------------------------------------------------

def none_identity_example():

    separator(
        "9. Checking None"
    )


    value = None


    print(
        value is None
    )


    print(
        """
Best practice:

Use:

value is None

instead of:

value == None
        """
    )



# ---------------------------------------------------------
# 10. Real-World Example
# ---------------------------------------------------------

def real_world_example():

    separator(
        "10. Real-World Example - Cache Object"
    )


    cache = {

        "model":
        "LLM",

        "version":
        "1.0"

    }


    active_cache = cache


    print(
        "Same Cache Object:",
        cache is active_cache
    )


    active_cache["version"] = "2.0"


    print(
        cache
    )


    print(
        """
Identity understanding helps avoid
unexpected shared state bugs in
backend and AI systems.
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    identity_definition()

    id_function_example()

    is_operator_example()

    equality_vs_identity_example()

    immutable_identity_example()

    mutable_identity_example()

    object_interning_example()

    function_identity_example()

    none_identity_example()

    real_world_example()



if __name__ == "__main__":

    main()