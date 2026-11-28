"""
Phase 15 - Interview-Level Python
07 Sorting Algorithms
"""


def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 1):
        swapped = False
        # After each round the biggest item is in its place, so the
        # next round can skip the end of the list.
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:      # no swaps means the list is already sorted
            break
    return nums


def selection_sort(nums):
    for i in range(len(nums)):
        m = i                          # index of the smallest item found so far
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[m]:
                m = j
        nums[i], nums[m] = nums[m], nums[i]
    return nums


def main():
    nums = [5, 2, 8, 1]

    # .copy() so each sort starts from the original list
    print("Bubble:", bubble_sort(nums.copy()))
    print("Selection:", selection_sort(nums.copy()))


if __name__ == "__main__":
    main()