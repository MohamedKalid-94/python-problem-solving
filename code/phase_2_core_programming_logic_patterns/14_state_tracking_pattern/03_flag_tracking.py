"""
Topic: Flag Tracking

Problem:
Check whether any negative number exists.
"""

numbers = [5, 8, 12, -3, 7]

found_negative = False

for number in numbers:

    if number < 0:
        found_negative = True
        break

print("Negative Found:", found_negative)
