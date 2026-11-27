"""
Topic: Maximum Sum Subarray

Problem:
Find the maximum sum of a subarray of size k.
"""

numbers = [2, 1, 5, 1, 3, 2]

k = 3

window_sum = sum(numbers[:k])
maximum = window_sum

for i in range(k, len(numbers)):

    window_sum += numbers[i]
    window_sum -= numbers[i - k]

    maximum = max(maximum, window_sum)

print("Maximum Sum:", maximum)