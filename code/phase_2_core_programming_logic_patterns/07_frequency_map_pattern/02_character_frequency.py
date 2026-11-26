"""
Topic: Character Frequency

Problem:
Count each character in a string.
"""

text = "programming"

frequency = {}

for character in text:
    frequency[character] = frequency.get(character, 0) + 1

print(frequency)