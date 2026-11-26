"""
Topic: Word Frequency

Problem:
Count occurrences of every word.
"""

sentence = "python is easy python is powerful"

words = sentence.split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)