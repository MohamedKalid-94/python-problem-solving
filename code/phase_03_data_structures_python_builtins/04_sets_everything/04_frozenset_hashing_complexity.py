"""
=========================================================
Topic: Frozenset, Hashing and Time Complexity
=========================================================

Concepts Covered

1. What is frozenset?
2. Creating frozenset
3. Difference between set and frozenset
4. Hashable vs Non-Hashable
5. Using frozenset as Dictionary Key
6. Using frozenset inside another Set
7. Hashing
8. Internal Working of Sets
9. Time Complexity
10. Real-World Examples

"""

def main():

    # ==================================================
    # 1. Creating frozenset
    # ==================================================

    print("=" * 60)
    print("1. Creating frozenset")
    print("=" * 60)

    numbers = frozenset([10, 20, 30, 40])

    print(numbers)

    print(type(numbers))


    # ==================================================
    # 2. Immutability
    # ==================================================

    print("\n" + "=" * 60)
    print("2. Frozenset is Immutable")
    print("=" * 60)

    colors = frozenset({

        "Red",

        "Green",

        "Blue"

    })

    print(colors)

    print()

    print("Frozenset cannot be modified.")

    # Uncomment to see the error

    # colors.add("Yellow")

    # colors.remove("Red")


    # ==================================================
    # 3. Set vs Frozenset
    # ==================================================

    print("\n" + "=" * 60)
    print("3. Set vs Frozenset")
    print("=" * 60)

    normal_set = {1, 2, 3}

    frozen_set = frozenset([1, 2, 3])

    print("Set")

    print(normal_set)

    print()

    print("Frozenset")

    print(frozen_set)


    # ==================================================
    # 4. Hashable Objects
    # ==================================================

    print("\n" + "=" * 60)
    print("4. Hashable Objects")
    print("=" * 60)

    print(hash("Python"))

    print(hash(100))

    print(hash((1, 2)))

    print(hash(frozenset({1, 2, 3})))

    print()

    print("List and Set are NOT hashable.")

    # Uncomment to see errors

    # hash([1,2])

    # hash({1,2})


    # ==================================================
    # 5. Frozenset as Dictionary Key
    # ==================================================

    print("\n" + "=" * 60)
    print("5. Frozenset as Dictionary Key")
    print("=" * 60)

    permissions = {

        frozenset({"Read"}): "Viewer",

        frozenset({"Read", "Write"}): "Editor",

        frozenset({"Read", "Write", "Delete"}): "Admin"

    }

    print(permissions)

    print()

    print(permissions[frozenset({"Read"})])


    # ==================================================
    # 6. Frozenset Inside Another Set
    # ==================================================

    print("\n" + "=" * 60)
    print("6. Nested Sets")
    print("=" * 60)

    set_of_sets = {

        frozenset({1, 2}),

        frozenset({3, 4}),

        frozenset({5, 6})

    }

    print(set_of_sets)


    # ==================================================
    # 7. Hashing
    # ==================================================

    print("\n" + "=" * 60)
    print("7. Hashing")
    print("=" * 60)

    print("Hash Value")

    print(hash("Python"))

    print()

    print(hash(frozenset({"AI", "ML"})))

    print()

    print("Sets use hash values for fast lookup.")


    # ==================================================
    # 8. Internal Working
    # ==================================================

    print("\n" + "=" * 60)
    print("8. Internal Working")
    print("=" * 60)

    skills = {

        "Python",

        "SQL",

        "Docker"

    }

    print(skills)

    print()

    print("Python computes the hash value.")

    print("Stores data inside a hash table.")

    print("Membership testing is O(1) average.")


    # ==================================================
    # 9. Time Complexity
    # ==================================================

    print("\n" + "=" * 60)
    print("9. Time Complexity")
    print("=" * 60)

    print("Add              : O(1) Average")

    print("Remove           : O(1) Average")

    print("Membership       : O(1) Average")

    print("Union            : O(n)")

    print("Intersection     : O(min(A,B))")

    print("Difference       : O(n)")

    print("Iteration        : O(n)")


    # ==================================================
    # 10. Real-World Example
    # ==================================================

    print("\n" + "=" * 60)
    print("10. User Permissions")
    print("=" * 60)

    roles = {

        frozenset({"Read"}): "Guest",

        frozenset({"Read", "Write"}): "Employee",

        frozenset({"Read", "Write", "Delete"}): "Administrator"

    }

    user_permission = frozenset({"Read", "Write"})

    print("Role")

    print(roles[user_permission])


if __name__ == "__main__":
    main()