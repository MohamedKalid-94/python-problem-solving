"""
Topic:
Python Lists - Copying, Nested Lists and Memory Behavior

Concepts Covered:
1. Assignment copy
2. Shallow copy
3. Slice copy
4. Deep copy
5. Mutable behavior
6. Nested lists
7. Memory reference
8. id() function

"""

import copy


def main():

    # ==================================================
    # 1. Assignment Copy (=)
    # ==================================================
    # Both variables point to the same list object
    # Changes affect the original list

    print("1. Assignment Copy")

    original = [10, 20, 30]

    assigned = original


    print("Original:", original)
    print("Assigned:", assigned)

    print("Same memory?")
    print(original is assigned)


    assigned.append(40)

    print("\nAfter modifying assigned list:")

    print("Original:", original)
    print("Assigned:", assigned)



    # ==================================================
    # 2. Copy using copy()
    # ==================================================
    # Creates a new list object
    # Changes in one list do not affect another

    print("\n\n2. Shallow Copy using copy()")


    numbers = [1,2,3,4]


    copied_numbers = numbers.copy()


    print("Original:", numbers)
    print("Copied:", copied_numbers)


    print("Same memory?")
    print(numbers is copied_numbers)


    copied_numbers.append(5)


    print("\nAfter modification:")

    print("Original:", numbers)
    print("Copied:", copied_numbers)



    # ==================================================
    # 3. Slice Copy
    # ==================================================

    print("\n\n3. Slice Copy")


    values = [100,200,300]


    slice_copy = values[:]


    print("Original:", values)
    print("Slice Copy:", slice_copy)


    print("Same object?")
    print(values is slice_copy)



    # ==================================================
    # 4. Shallow Copy Problem
    # ==================================================

    print("\n\n4. Shallow Copy with Nested Lists")


    students = [
        ["John",90],
        ["David",85]
    ]


    students_copy = students.copy()


    print("Original:")
    print(students)


    print("Copy:")
    print(students_copy)



    # Changing inner list

    students_copy[0][1] = 95


    print("\nAfter changing nested value:")

    print("Original:")
    print(students)


    print("Copy:")
    print(students_copy)



    # Both changed because inner list reference is shared



    # ==================================================
    # 5. Deep Copy
    # ==================================================

    print("\n\n5. Deep Copy")


    employees = [
        ["Alice",50000],
        ["Bob",60000]
    ]


    deep_copy = copy.deepcopy(employees)


    print("Original:")
    print(employees)


    print("Deep Copy:")
    print(deep_copy)



    deep_copy[0][1] = 70000


    print("\nAfter modifying deep copy:")


    print("Original:")
    print(employees)


    print("Deep Copy:")
    print(deep_copy)



    # ==================================================
    # 6. Memory Address using id()
    # ==================================================

    print("\n\n6. Memory Address")


    list_a = [1,2,3]

    list_b = list_a.copy()


    print("List A id:")
    print(id(list_a))


    print("List B id:")
    print(id(list_b))


    print("\nSame object?")
    print(id(list_a) == id(list_b))



    # ==================================================
    # 7. Mutable Behavior
    # ==================================================

    print("\n\n7. Mutable Behavior")


    data = [10,20,30]


    print("Before:")
    print(data)


    data[0] = 100


    print("After:")
    print(data)



if __name__ == "__main__":
    main()