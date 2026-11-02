"""Return the biggest number in a list (without using max())."""


def max_of_list(nums):
    if len(nums) == 0:
        return None

    biggest = nums[0]
    for n in nums:
        if n > biggest:
            biggest = n
    return biggest