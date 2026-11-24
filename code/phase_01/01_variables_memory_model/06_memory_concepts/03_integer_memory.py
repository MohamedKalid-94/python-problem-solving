"""
Topic: Memory Concepts

Concept:
Integers are immutable objects.
"""

number_1 = 100
number_2 = number_1


print("Before Change")

print(number_1)
print(number_2)


number_2 = 200


print()

print("After Change")

print(number_1)
print(number_2)