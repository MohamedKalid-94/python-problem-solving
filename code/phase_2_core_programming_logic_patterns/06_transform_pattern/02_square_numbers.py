"""
Topic: Square Numbers

Problem:
Create a new list containing the square of every number.
"""

numbers = [2, 4, 6, 8]

squares = []

for number in numbers:
    squares.append(number ** 2)

print("Numbers :", numbers)
print("Squares :", squares)