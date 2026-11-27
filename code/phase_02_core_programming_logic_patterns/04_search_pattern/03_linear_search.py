"""
Topic: Linear Search

Problem:
Find the position of an element using linear search.
"""

numbers = [15, 28, 42, 67, 91]

target = 67

position = -1

for index in range(len(numbers)):
    if numbers[index] == target:
        position = index
        break

if position != -1:
    print("Found at index:", position)
else:
    print("Element not found")