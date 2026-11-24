"""
Topic: Arithmetic Operators

Concept:
Calculate product discount.

Formula:

Discount Amount = Price * Discount Percentage / 100

Final Price = Original Price - Discount Amount
"""


product_price = 2000

discount_percentage = 10


discount_amount = (
    product_price * discount_percentage / 100
)


final_price = product_price - discount_amount


print("Product Discount")
print("----------------")

print("Original Price :", product_price)

print("Discount % :", discount_percentage)

print("Discount Amount :", discount_amount)

print("Final Price :", final_price)