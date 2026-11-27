"""
Topic: Most Repeated Item

Problem:
Find the most frequently occurring element.
"""

numbers = [2, 4, 2, 5, 6, 2, 4, 5, 5, 5]

frequency = {}

for number in numbers:
    frequency[number] = frequency.get(number, 0) + 1

most_repeated = max(frequency, key=frequency.get)

print("Most Repeated:", most_repeated)
print("Count:", frequency[most_repeated])