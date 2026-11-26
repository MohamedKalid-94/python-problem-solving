"""
Topic: Filter Valid Values

Problem:
Remove None values from a list.
"""

data = [10, None, 25, None, 40, 55, None]

valid_values = []

for item in data:
    if item is not None:
        valid_values.append(item)

print(valid_values)