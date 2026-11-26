"""
Topic: Dynamic Typing

Concept:
Convert input data from string to required type.

Real-World Example:
Taking age from a user.
"""

age_input = "28"

print("Before Conversion")
print("-----------------")
print(age_input)
print(type(age_input))


age = int(age_input)

print()

print("After Conversion")
print("----------------")
print(age)
print(type(age))


future_age = age + 5

print()

print("Future Age")
print("----------")
print(future_age)