"""
Topic: Find Element

Problem:
Find whether an element exists in a list.
"""

numbers = [10, 20, 30, 40, 50]

target = 30

found = False

for number in numbers:
    if number == target:
        found = True
        break

if found:
    print("Element Found")
else:
    print("Element Not Found")