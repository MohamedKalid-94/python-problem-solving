import pytest

from phase_2_arrays_sorting_hashing.arrays.second_largest import second_largest
from phase_2_arrays_sorting_hashing.arrays.reverse_in_place import reverse_in_place
from phase_2_arrays_sorting_hashing.arrays.left_rotate_by_one import left_rotate_by_one
from phase_2_arrays_sorting_hashing.arrays.move_zeroes import move_zeroes
from phase_2_arrays_sorting_hashing.arrays.remove_duplicates_sorted import remove_duplicates_sorted
from phase_2_arrays_sorting_hashing.arrays.rotate_by_k import rotate_by_k
from phase_2_arrays_sorting_hashing.arrays.merge_sorted_arrays import merge_sorted_arrays
from phase_2_arrays_sorting_hashing.arrays.missing_number import missing_number
from phase_2_arrays_sorting_hashing.arrays.majority_element import majority_element
from phase_2_arrays_sorting_hashing.sorting.bubble_sort import bubble_sort
from phase_2_arrays_sorting_hashing.sorting.selection_sort import selection_sort
from phase_2_arrays_sorting_hashing.sorting.insertion_sort import insertion_sort
from phase_2_arrays_sorting_hashing.sorting.sort_words import sort_words
from phase_2_arrays_sorting_hashing.sorting.kth_largest import kth_largest
from phase_2_arrays_sorting_hashing.sorting.sort_colors import sort_colors


# ---------- Day 1 ----------
@pytest.mark.parametrize("nums, expected", [
    ([3, 1, 4, 2], 3),
    ([5, 5, 4], 4),
    ([-1, -5, -3], -3),
    ([7], None),
    ([2, 2], None),
    ([], None),
])
def test_second_largest(nums, expected):
    assert second_largest(nums) == expected


@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 4], [4, 3, 2, 1]),
    ([1, 2, 3], [3, 2, 1]),
    ([1], [1]),
    ([], []),
])
def test_reverse_in_place(nums, expected):
    reverse_in_place(nums)
    assert nums == expected


@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 3, 4], [2, 3, 4, 1]),
    ([1, 2], [2, 1]),
    ([1], [1]),
    ([], []),
])
def test_left_rotate_by_one(nums, expected):
    left_rotate_by_one(nums)
    assert nums == expected


# ---------- Day 2 ----------
@pytest.mark.parametrize("nums, expected", [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0, 0], [0, 0]),
    ([1, 2], [1, 2]),
    ([0], [0]),
    ([], []),
])
def test_move_zeroes(nums, expected):
    move_zeroes(nums)
    assert nums == expected


@pytest.mark.parametrize("nums, expected", [
    ([1, 1, 2], [1, 2]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4]),
    ([2, 2, 2], [2]),
    ([1], [1]),
    ([], []),
])
def test_remove_duplicates_sorted(nums, expected):
    k = remove_duplicates_sorted(nums)
    assert k == len(expected)
    assert nums[:k] == expected


@pytest.mark.parametrize("nums, k, expected", [
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
    ([1, 2], 3, [2, 1]),
    ([1, 2, 3], 0, [1, 2, 3]),
    ([1], 5, [1]),
    ([], 2, []),
])
def test_rotate_by_k(nums, k, expected):
    rotate_by_k(nums, k)
    assert nums == expected


# ---------- Day 3 ----------
@pytest.mark.parametrize("a, b, expected", [
    ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
    ([1, 5, 9], [2, 3], [1, 2, 3, 5, 9]),
    ([], [1, 2], [1, 2]),
    ([1, 2], [], [1, 2]),
    ([1, 1], [1], [1, 1, 1]),
    ([], [], []),
])
def test_merge_sorted_arrays(a, b, expected):
    assert merge_sorted_arrays(a, b) == expected


@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 4, 5], 3),
    ([2], 1),
    ([1], 2),
    ([2, 3, 4], 1),
    ([1, 2, 3], 4),
])
def test_missing_number(nums, expected):
    assert missing_number(nums) == expected


@pytest.mark.parametrize("nums, expected", [
    ([3, 2, 3], 3),
    ([2, 2, 1, 1, 1, 2, 2], 2),
    ([5], 5),
    ([1, 1, 1], 1),
])
def test_majority_element(nums, expected):
    assert majority_element(nums) == expected


# ---------- Day 4 ----------
@pytest.mark.parametrize("func", [bubble_sort, selection_sort, insertion_sort])
@pytest.mark.parametrize("nums, expected", [
    ([5, 2, 9, 1], [1, 2, 5, 9]),
    ([3, 3, 1], [1, 3, 3]),
    ([4, 3, 2, 1], [1, 2, 3, 4]),
    ([1, 2, 3], [1, 2, 3]),
    ([-2, 5, -9, 0], [-9, -2, 0, 5]),
    ([1], [1]),
    ([], []),
])
def test_manual_sorts(func, nums, expected):
    original = list(nums)
    assert func(nums) == expected
    assert nums == original  # the input must not be modified


# ---------- Day 5 ----------
@pytest.mark.parametrize("words, expected", [
    (["banana", "kiwi", "apple", "fig"], ["fig", "kiwi", "apple", "banana"]),
    (["bb", "aa", "c"], ["c", "aa", "bb"]),
    (["b", "a"], ["a", "b"]),
    ([], []),
])
def test_sort_words(words, expected):
    assert sort_words(words) == expected


@pytest.mark.parametrize("nums, k, expected", [
    ([3, 2, 1, 5, 6, 4], 2, 5),
    ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ([1], 1, 1),
    ([2, 2], 2, 2),
])
def test_kth_largest(nums, k, expected):
    assert kth_largest(nums, k) == expected


@pytest.mark.parametrize("nums, expected", [
    ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
    ([2, 0, 1], [0, 1, 2]),
    ([1, 1], [1, 1]),
    ([0], [0]),
    ([], []),
])
def test_sort_colors(nums, expected):
    sort_colors(nums)
    assert nums == expected