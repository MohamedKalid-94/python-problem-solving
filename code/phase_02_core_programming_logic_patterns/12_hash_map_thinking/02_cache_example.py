"""
Topic: Cache Example

Problem:
Demonstrate a simple cache using a dictionary.
"""

cache = {}

number = 5

if number not in cache:
    cache[number] = number ** 2

print(cache)