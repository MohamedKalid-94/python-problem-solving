"""
Topic: Find Smallest Number

Problem:
Find the smallest number in a list.
"""

numbers = [15, 42, 8, 99, 27]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("Smallest:", smallest)