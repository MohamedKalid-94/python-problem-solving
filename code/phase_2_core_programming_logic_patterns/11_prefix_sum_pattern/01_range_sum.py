"""
Topic: Range Sum

Problem:
Find the sum between two indices using a prefix sum array.
"""

numbers = [10, 20, 30, 40, 50]

prefix = [0]

for number in numbers:
    prefix.append(prefix[-1] + number)

left = 1
right = 3

range_sum = prefix[right + 1] - prefix[left]

print("Range Sum:", range_sum)
