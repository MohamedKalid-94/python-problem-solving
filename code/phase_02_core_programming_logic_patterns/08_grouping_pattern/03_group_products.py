"""
Topic: Group Products

Problem:
Group products by category.
"""

products = [
    ("Laptop", "Electronics"),
    ("TV", "Electronics"),
    ("Shirt", "Clothing"),
    ("Jeans", "Clothing"),
    ("Apple", "Food")
]

categories = {}

for product, category in products:
    categories.setdefault(category, []).append(product)

print(categories)