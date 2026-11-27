"""
Topic: Count Positive Numbers

Problem:
Count how many positive numbers are present in a list.
"""

numbers = [-5, 10, 0, 8, -2, 15, -7, 4]

count = 0

for number in numbers:
    if number > 0:
        count += 1

print("Positive Numbers:", count)