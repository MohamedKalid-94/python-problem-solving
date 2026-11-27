"""
Topic: Remove Duplicates

Problem:
Remove duplicate values while preserving order.
"""

numbers = [10, 20, 10, 30, 20, 40, 50, 40]

unique_numbers = []

for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

print(unique_numbers)