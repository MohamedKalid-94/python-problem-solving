"""
Topic: Vowel Counter

Problem:
Count vowels in a string.
"""

text = input("Enter text: ")

count = 0

for character in text.lower():

    if character in "aeiou":
        count += 1

print("Vowels:", count)