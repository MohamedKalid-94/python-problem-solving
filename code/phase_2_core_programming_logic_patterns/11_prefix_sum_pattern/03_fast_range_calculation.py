"""
Topic: Fast Range Calculation

Problem:
Answer multiple range sum queries efficiently using prefix sums.
"""

numbers = [2, 4, 6, 8, 10]

prefix = [0]

for number in numbers:
    prefix.append(prefix[-1] + number)

queries = [
    (0, 2),
    (1, 4),
    (2, 3)
]

for start, end in queries:

    result = prefix[end + 1] - prefix[start]

    print(f"Sum({start}, {end}) = {result}")
    