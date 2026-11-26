"""
Topic: Compare Elements

Problem:
Compare every pair of elements.
"""

numbers = [2, 4, 6]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        print(numbers[i], numbers[j])