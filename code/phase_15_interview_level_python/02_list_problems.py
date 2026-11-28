"""
Phase 15 - Interview-Level Python
02 List Problems
"""


def find_max(nums):
    if not nums:
        raise ValueError("list is empty")
    return max(nums)


def find_min(nums):
    if not nums:
        raise ValueError("list is empty")
    return min(nums)


def remove_duplicates(nums):
    # dict.fromkeys removes duplicates and keeps the original order
    return list(dict.fromkeys(nums))


def reverse_list(nums):
    return nums[::-1]


def rotate_list(nums, k):
    # Move the last k items to the front: [1, 2, 3, 4] rotated by 1 -> [4, 1, 2, 3]
    if not nums:
        return []
    k = k % len(nums)      # rotating by the list length gives the same list
    if k == 0:
        return nums[:]
    return nums[-k:] + nums[:-k]


def move_zeros(nums):
    # Keep the non-zero items, then add all the zeros at the end
    return [x for x in nums if x != 0] + [0] * nums.count(0)


def two_sum(nums, target):
    seen = {}                       # number -> index where we saw it
    for i, n in enumerate(nums):
        needed = target - n
        if needed in seen:
            return [seen[needed], i]
        seen[n] = i
    return []


def main():
    nums = [1, 2, 3, 4, 0, 2]

    print("Max:", find_max(nums))
    print("Min:", find_min(nums))
    print("Remove Duplicates:", remove_duplicates(nums))
    print("Reverse:", reverse_list(nums))
    print("Rotate:", rotate_list(nums, 2))
    print("Rotate (k > length):", rotate_list([1, 2, 3], 4))
    print("Move Zeros:", move_zeros(nums))
    print("Two Sum:", two_sum([2, 7, 11, 15], 9))


if __name__ == "__main__":
    main()