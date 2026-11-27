"""
Topic: Membership Operators

Concept:
Search products in inventory.
"""


products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Watch"
]


search_product = "Mobile"


print("Product Search")
print("--------------")


print(
    "Product Available:",
    search_product in products
)