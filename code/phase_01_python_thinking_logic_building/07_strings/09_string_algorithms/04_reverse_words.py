"""
Topic: Reverse Words

Problem:
Reverse the order of words.
"""

sentence = "Python is easy to learn"

words = sentence.split()

reversed_sentence = " ".join(words[::-1])

print(reversed_sentence)