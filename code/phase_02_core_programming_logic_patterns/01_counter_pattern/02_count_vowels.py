"""
Topic: Count Vowels

Problem:
Count the number of vowels in a string.
"""

text = "Python Programming"

count = 0

for character in text.lower():
    if character in "aeiou":
        count += 1

print("Vowel Count:", count)