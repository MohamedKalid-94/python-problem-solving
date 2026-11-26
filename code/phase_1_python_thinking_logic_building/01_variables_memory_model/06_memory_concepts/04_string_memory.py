"""
Topic: Memory Concepts

Concept:
Strings are immutable objects.

Changing a string creates a new object.
"""

name = "Python"

new_name = name


print("Before Change")

print(name)
print(new_name)


new_name = "Python Programming"


print()

print("After Change")

print(name)
print(new_name)