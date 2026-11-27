"""
Topic: Remove Duplicates

Problem:
Remove duplicates from a sorted list.
"""

numbers = [1, 1, 2, 2, 3, 3, 4, 5, 5]

unique = [numbers[0]]

for i in range(1, len(numbers)):
    if numbers[i] != numbers[i - 1]:
        unique.append(numbers[i])

print(unique)