"""
Topic: Dynamic Typing

Concept:
Convert one data type into another.

Real-World Example:
Converting user data for calculations.
"""

number_text = "100"

print("Before Conversion")
print("-----------------")
print(number_text)
print(type(number_text))


number = int(number_text)

print()

print("After Conversion")
print("----------------")
print(number)
print(type(number))


result = number + 50

print()

print("Calculation Result")
print("------------------")
print(result)