"""
Topic: Longest Word

Problem:
Find the longest word in a list.
"""

words = ["Python", "Programming", "AI", "Developer", "Engineer"]

longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest Word:", longest)