"""
Topic: Anagram

Problem:
Check whether two words are anagrams.
"""

word1 = input("First word: ")
word2 = input("Second word: ")

if sorted(word1.lower()) == sorted(word2.lower()):
    print("Anagram")
else:
    print("Not an Anagram")