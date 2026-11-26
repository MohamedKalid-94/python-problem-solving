"""
Topic: Filter Even Numbers

Problem:
Create a list containing only even numbers.
"""

numbers = [3, 8, 15, 20, 22, 31, 40]

even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)