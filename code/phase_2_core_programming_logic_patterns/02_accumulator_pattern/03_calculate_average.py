"""
Topic: Calculate Average

Problem:
Calculate the average of numbers.
"""

numbers = [80, 90, 75, 85, 70]

total = 0

for number in numbers:
    total += number

average = total / len(numbers)

print("Average:", average)