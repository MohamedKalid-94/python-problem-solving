"""
Topic: Duplicate Detection

Problem:
Detect duplicate values using a hash map.
"""

numbers = [1, 2, 3, 4, 2, 5, 6]

seen = {}

duplicate_found = False

for number in numbers:

    if number in seen:
        duplicate_found = True
        print("Duplicate:", number)
        break

    seen[number] = True

if not duplicate_found:
    print("No duplicates")