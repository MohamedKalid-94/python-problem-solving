"""
Topic: Object References

Concept:
Multiple variables can refer to the same object.

Real-World Example:
Shared shopping cart.
"""

shopping_cart = ["Laptop", "Mouse"]

customer_1 = shopping_cart
customer_2 = shopping_cart

customer_1.append("Keyboard")

print("Customer 1 Cart")
print(customer_1)

print()

print("Customer 2 Cart")
print(customer_2)