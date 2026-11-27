"""
Topic: Running Total

Problem:
Display the cumulative total after each number.
"""

numbers = [10, 20, 30, 40]

running_total = 0

for number in numbers:
    running_total += number
    print(running_total)
    