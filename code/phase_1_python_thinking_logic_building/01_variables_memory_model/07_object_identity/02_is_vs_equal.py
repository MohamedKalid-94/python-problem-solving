"""
Topic: Object Identity

Concept:

== checks values.

is checks memory identity.
"""

list_1 = [1, 2, 3]

list_2 = [1, 2, 3]


print("Value Comparison")
print(list_1 == list_2)


print()

print("Identity Comparison")
print(list_1 is list_2)