"""
Topic: Filter Positive Numbers

Problem:
Create a list containing only positive numbers.
"""

numbers = [-10, 5, -3, 8, 12, -6, 20]

positive_numbers = []

for number in numbers:
    if number > 0:
        positive_numbers.append(number)

print(positive_numbers)