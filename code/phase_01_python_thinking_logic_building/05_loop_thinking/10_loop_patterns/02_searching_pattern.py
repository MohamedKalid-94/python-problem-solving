"""
Topic: Loop Pattern

Problem:
Search for a number.
"""

numbers = [12, 25, 40, 55]

search = 40

found = False

for number in numbers:

    if number == search:
        found = True
        break

if found:
    print("Number Found")
else:
    print("Number Not Found")