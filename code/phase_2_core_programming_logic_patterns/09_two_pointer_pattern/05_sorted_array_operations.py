"""
Topic: Sorted Array Operations

Problem:
Find two numbers whose sum equals the target.
"""

numbers = [1, 2, 3, 4, 6, 8, 10]

target = 10

left = 0
right = len(numbers) - 1

while left < right:

    current_sum = numbers[left] + numbers[right]

    if current_sum == target:
        print("Pair Found:", numbers[left], numbers[right])
        break

    elif current_sum < target:
        left += 1

    else:
        right -= 1