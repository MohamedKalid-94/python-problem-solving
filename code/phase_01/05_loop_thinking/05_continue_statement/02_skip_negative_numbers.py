"""
Topic: continue Statement

Problem:
Skip negative numbers.
"""

numbers = [10, -5, 25, -8, 40]

for number in numbers:

    if number < 0:
        continue

    print(number)