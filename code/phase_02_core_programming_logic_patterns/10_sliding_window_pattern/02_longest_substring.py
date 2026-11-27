"""
Topic: Longest Substring

Problem:
Find the length of the longest substring without repeating characters.
"""

text = "abcabcbb"

seen = set()

left = 0
maximum = 0

for right in range(len(text)):

    while text[right] in seen:
        seen.remove(text[left])
        left += 1

    seen.add(text[right])

    maximum = max(maximum, right - left + 1)

print("Longest Length:", maximum)