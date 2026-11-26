"""
Topic: Last Occurrence

Problem:
Find the last occurrence of a value.
"""

numbers = [5, 10, 15, 10, 20, 10]

target = 10

position = -1

for index in range(len(numbers)):
    if numbers[index] == target:
        position = index

if position != -1:
    print("Last Occurrence:", position)
else:
    print("Element not found")