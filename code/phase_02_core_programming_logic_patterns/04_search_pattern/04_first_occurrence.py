"""
Topic: First Occurrence

Problem:
Find the first occurrence of a value.
"""

numbers = [5, 10, 15, 10, 20, 10]

target = 10

for index in range(len(numbers)):
    if numbers[index] == target:
        print("First Occurrence:", index)
        break