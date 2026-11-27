"""
Topic: Count Even Numbers

Problem:
Count the even numbers in a list.
"""

numbers = [12, 5, 8, 9, 14, 21, 18]

count = 0

for number in numbers:
    if number % 2 == 0:
        count += 1

print("Even Numbers:", count)