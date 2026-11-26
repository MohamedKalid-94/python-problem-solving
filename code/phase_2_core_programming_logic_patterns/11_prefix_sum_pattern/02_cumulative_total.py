"""
Topic: Cumulative Total

Problem:
Display the cumulative total after each element.
"""

numbers = [5, 10, 15, 20]

running_total = 0

for number in numbers:
    running_total += number
    print(running_total)
    