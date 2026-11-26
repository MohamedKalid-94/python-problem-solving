"""
Topic: Moving Average

Problem:
Calculate the moving average of window size 3.
"""

numbers = [10, 20, 30, 40, 50]

k = 3

window_sum = sum(numbers[:k])

print(window_sum / k)

for i in range(k, len(numbers)):

    window_sum += numbers[i]
    window_sum -= numbers[i - k]

    print(window_sum / k)