"""
Topic: Object Identity

Concept:
Observe identity changes.
"""

value = 100


print("Initial Value")
print(value)

print("ID:")
print(id(value))


value = 200


print()

print("New Value")
print(value)

print("New ID:")
print(id(value))