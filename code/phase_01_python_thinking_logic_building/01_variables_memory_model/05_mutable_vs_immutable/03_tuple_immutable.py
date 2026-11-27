"""
Topic: Mutable vs Immutable

Concept:
Tuple values cannot be changed after creation.

Immutable Object:
Tuple
"""

coordinates = (10, 20)

print("Original Tuple")
print(coordinates)

# This will create an error
# coordinates[0] = 50

print()

print("Tuple cannot be modified")