"""
Topic: Character Frequency

Problem:
Count frequency of each character.
"""

text = input("Enter text: ")

for character in sorted(set(text)):
    print(character, ":", text.count(character))