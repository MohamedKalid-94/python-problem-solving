"""
Phase 15 - Interview-Level Python
06 Searching Algorithms
"""


def linear_search(nums, target):
    # Check every item one by one. Works on any list.
    for i, n in enumerate(nums):
        if n == target:
            return i
    return -1


def binary_search(nums, target):
    # The list MUST be sorted. Each step throws away half of the items.
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def main():
    nums = [1, 3, 5, 7, 9]

    print("Linear:", linear_search(nums, 5))
    print("Binary:", binary_search(nums, 7))
    print("Binary (not found):", binary_search(nums, 4))


if __name__ == "__main__":
    main()