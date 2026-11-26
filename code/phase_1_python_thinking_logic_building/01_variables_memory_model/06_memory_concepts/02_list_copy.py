"""
Topic: Memory Concepts

Concept:
Copy creates a separate object in memory.
"""

original_list = [10, 20, 30]

copied_list = original_list.copy()


print("Original List")
print(original_list)

print()

print("Copied List")
print(copied_list)


copied_list.append(40)


print()

print("After Modification")

print("Original List")
print(original_list)

print("Copied List")
print(copied_list)