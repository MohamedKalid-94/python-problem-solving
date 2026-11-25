"""
Topic: Word Counter

Problem:
Count the number of words.
"""

sentence = input("Enter a sentence: ")

words = sentence.split()

print("Words:", len(words))