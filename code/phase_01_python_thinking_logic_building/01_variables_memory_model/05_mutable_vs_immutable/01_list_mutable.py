"""
Topic: Mutable vs Immutable

Concept:
Lists can be changed after creation.

Mutable Object:
List
"""

numbers = [10, 20, 30]

print("Before Change")
print(numbers)

numbers.append(40)

print()

print("After Change")
print(numbers)