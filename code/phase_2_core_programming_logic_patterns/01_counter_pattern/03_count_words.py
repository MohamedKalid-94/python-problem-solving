"""
Topic: Count Words

Problem:
Count the number of words in a sentence.
"""

sentence = "Python is easy to learn"

words = sentence.split()

count = 0

for word in words:
    count += 1

print("Word Count:", count)