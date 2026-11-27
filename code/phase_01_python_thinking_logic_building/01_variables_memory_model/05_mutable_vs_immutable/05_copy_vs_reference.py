"""
Topic: Mutable vs Immutable

Concept:
Difference between reference and copy.

Reference:
Points to the same object.

Copy:
Creates a new object.
"""

original_list = [1, 2, 3]


reference_list = original_list

copy_list = original_list.copy()


reference_list.append(4)

copy_list.append(5)


print("Original List")
print(original_list)

print()

print("Reference List")
print(reference_list)

print()

print("Copy List")
print(copy_list)