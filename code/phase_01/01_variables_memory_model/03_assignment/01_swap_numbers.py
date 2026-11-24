"""
Topic: Assignment

Concept:
Swap two variables.

Real-World Example:
Exchange two values without using a temporary variable.
"""

number_1 = 10
number_2 = 20

print("Before Swapping")
print("----------------")
print("Number 1:", number_1)
print("Number 2:", number_2)

number_1, number_2 = number_2, number_1

print()

print("After Swapping")
print("----------------")
print("Number 1:", number_1)
print("Number 2:", number_2)