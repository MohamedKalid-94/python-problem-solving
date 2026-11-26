"""
Topic: Find Largest Number

Problem:
Find the largest number in a list.
"""

numbers = [15, 42, 8, 99, 27]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest:", largest)