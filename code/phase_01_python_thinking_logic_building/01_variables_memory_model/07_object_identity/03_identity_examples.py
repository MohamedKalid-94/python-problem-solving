"""
Topic: Object Identity

Concept:
Same object vs different objects.
"""

numbers_1 = [10, 20]

numbers_2 = numbers_1


print("numbers_1 id")
print(id(numbers_1))

print()

print("numbers_2 id")
print(id(numbers_2))


print()

print("Same Object?")
print(numbers_1 is numbers_2)