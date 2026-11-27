"""
Topic: Window Optimization

Problem:
Find the minimum sum of a subarray of size k.
"""

numbers = [4, 2, 1, 7, 8, 1, 2]

k = 3

window_sum = sum(numbers[:k])

minimum = window_sum

for i in range(k, len(numbers)):

    window_sum += numbers[i]
    window_sum -= numbers[i - k]

    minimum = min(minimum, window_sum)

print("Minimum Sum:", minimum)