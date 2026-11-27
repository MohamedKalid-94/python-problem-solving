"""
Topic: Membership Operators

Concept:
Check whether an item exists in a list.

Operators:
in
not in
"""


shopping_items = [
    "Laptop",
    "Mouse",
    "Keyboard"
]


item = "Mouse"


print("Shopping List")
print("-------------")

print("Item Available:", item in shopping_items)

print("Item Missing:", item not in shopping_items)