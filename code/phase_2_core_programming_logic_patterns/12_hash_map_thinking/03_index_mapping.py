"""
Topic: Index Mapping

Problem:
Create a dictionary mapping values to their indices.
"""

numbers = [10, 20, 30, 40]

index_map = {}

for index, value in enumerate(numbers):
    index_map[value] = index

print(index_map)