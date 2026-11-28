"""
Phase 15 - Interview-Level Python
11 Coding Patterns
"""


def accumulator_pattern(nums):
    # Accumulator: keep adding values into one running total
    total = 0
    for n in nums:
        total += n
    return total


def counter_pattern(nums):
    # Counter: add 1 each time a condition is true (here: positive numbers)
    count = 0
    for n in nums:
        if n > 0:
            count += 1
    return count


def frequency_pattern(nums):
    result = {}
    for n in nums:
        result[n] = result.get(n, 0) + 1
    return result


def two_pointer(nums, target):
    # The list MUST be sorted. Start at both ends and move inward.
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return [left, right]
        if total < target:
            left += 1          # need a bigger sum
        else:
            right -= 1         # need a smaller sum
    return []


def sliding_window(nums, k):
    # Biggest sum of k numbers in a row.
    # Instead of adding k numbers again for every window, slide the window:
    # add the new number on the right, subtract the old number on the left.
    if k <= 0 or k > len(nums):
        raise ValueError("k must be between 1 and the list length")

    window = sum(nums[:k])
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best


def main():
    print("Accumulator:", accumulator_pattern([1, 2, 3]))
    print("Counter:", counter_pattern([1, -2, 3, 0]))
    print("Frequency:", frequency_pattern([1, 1, 2]))
    print("Two Pointer:", two_pointer([1, 2, 3, 4], 5))
    print("Sliding Window:", sliding_window([1, 2, 3, 4, 5], 3))


if __name__ == "__main__":
    main()