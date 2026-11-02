"""Return the sum of all numbers in a list (without using sum())."""


def sum_of_list(nums):
    total = 0
    for n in nums:
        total = total + n
    return total