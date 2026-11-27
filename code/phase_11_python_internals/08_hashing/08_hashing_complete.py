"""
=========================================================
Topic : Hashing in Python

Covered:

1. What is Hashing?
2. hash() Function
3. Hashable Objects
4. Non-Hashable Objects
5. Hashing with Dictionary
6. Hashing with Set
7. Hash Consistency
8. Custom Object Hashing
9. Real-World Applications

=========================================================
"""


def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------
# 1. What is Hashing?
# ---------------------------------------------------------

def hashing_definition():
    separator("1. Hashing Definition")

    print(
        """
Hashing converts an object into a fixed-size
integer value called a hash value.

Hash values are used for:

- Dictionary keys
- Set elements
- Fast lookup operations
- Data integrity checking

Hashable objects should be:

- Immutable
- Have a stable hash value
        """
    )


# ---------------------------------------------------------
# 2. hash() Function
# ---------------------------------------------------------

def hash_function_example():
    separator("2. hash() Function")

    values = [
        10,
        "Python",
        3.14,
        (1, 2, 3)
    ]

    for value in values:

        print(
            value,
            "=>",
            hash(value)
        )


# ---------------------------------------------------------
# 3. Hashable Objects
# ---------------------------------------------------------

def hashable_objects_example():
    separator("3. Hashable Objects")

    print(
        """
Common hashable objects:

- int
- float
- string
- tuple (only immutable values)
- frozenset
        """
    )


    tuple_data = (
        "Python",
        "AI"
    )


    print(
        "Tuple Hash:",
        hash(tuple_data)
    )



# ---------------------------------------------------------
# 4. Non-Hashable Objects
# ---------------------------------------------------------

def non_hashable_objects_example():

    separator(
        "4. Non-Hashable Objects"
    )


    print(
        """
Non-hashable objects:

- list
- dictionary
- set

Reason:

They are mutable, so their contents
can change and hash value cannot remain stable.
        """
    )


    try:

        numbers = [1,2,3]

        print(
            hash(numbers)
        )

    except TypeError as error:

        print(
            "Error:",
            error
        )



# ---------------------------------------------------------
# 5. Hashing with Dictionary
# ---------------------------------------------------------

def dictionary_hash_example():

    separator(
        "5. Dictionary Uses Hashing"
    )


    employee = {

        "id":101,

        "name":"Kalid",

        "role":"AI Engineer"

    }


    print(
        employee["name"]
    )


    print(
        """
Dictionary internally uses hash values
for fast key lookup.
        """
    )



# ---------------------------------------------------------
# 6. Hashing with Set
# ---------------------------------------------------------

def set_hash_example():

    separator(
        "6. Set Uses Hashing"
    )


    technologies = {

        "Python",
        "AI",
        "ML"

    }


    technologies.add(
        "GenAI"
    )


    print(
        technologies
    )


    print(
        """
Sets use hashing to store
unique values.
        """
    )



# ---------------------------------------------------------
# 7. Hash Consistency
# ---------------------------------------------------------

def hash_consistency_example():

    separator(
        "7. Hash Consistency"
    )


    value = "Python"


    hash1 = hash(value)

    hash2 = hash(value)


    print(
        "Hash 1:",
        hash1
    )


    print(
        "Hash 2:",
        hash2
    )


    print(
        "Same Hash:",
        hash1 == hash2
    )



# ---------------------------------------------------------
# 8. Hash Collision
# ---------------------------------------------------------

def hash_collision_example():

    separator(
        "8. Hash Collision"
    )


    print(
        """
Hash collision occurs when two different
objects produce the same hash value.

Python handles collisions internally
using equality comparison.
        """
    )


# ---------------------------------------------------------
# 9. Custom Object Hashing
# ---------------------------------------------------------

class Employee:

    def __init__(self, employee_id):

        self.employee_id = employee_id


    def __hash__(self):

        return hash(
            self.employee_id
        )


    def __eq__(self, other):

        return (
            self.employee_id ==
            other.employee_id
        )



def custom_hash_example():

    separator(
        "9. Custom Object Hashing"
    )


    employee1 = Employee(101)

    employee2 = Employee(101)


    print(
        "Employee 1 Hash:",
        hash(employee1)
    )


    print(
        "Employee 2 Hash:",
        hash(employee2)
    )


    print(
        "Equal:",
        employee1 == employee2
    )



# ---------------------------------------------------------
# 10. Real-World Example
# ---------------------------------------------------------

def real_world_example():

    separator(
        "10. Real-World Example - Cache System"
    )


    cache = {

        "user_101":
        "Profile Data",

        "document_001":
        "Embedding Vector"

    }


    key = "user_101"


    print(
        cache[key]
    )


    print(
        """
AI systems use hashing in:

- Caching
- Vector indexing
- Database lookup
- Duplicate detection
        """
    )



# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    hashing_definition()

    hash_function_example()

    hashable_objects_example()

    non_hashable_objects_example()

    dictionary_hash_example()

    set_hash_example()

    hash_consistency_example()

    hash_collision_example()

    custom_hash_example()

    real_world_example()



if __name__ == "__main__":

    main()