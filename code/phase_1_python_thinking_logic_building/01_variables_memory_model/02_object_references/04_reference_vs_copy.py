"""
Topic: Object References

Concept:
Reference vs Copy.
"""

original_list = [10, 20, 30]

reference_list = original_list

copy_list = original_list.copy()

reference_list.append(40)

print("Original List")
print(original_list)

print()

print("Reference List")
print(reference_list)

print()

print("Copy List")
print(copy_list)