# Practice - Interview-Level Python

Try each problem yourself first. Write a function that **returns** the answer, and test it with the examples. State your time complexity.

## 01 Strings

1. Write `count_consonants(s)`.
2. Write `capitalize_words(s)` without using `.title()`.
3. Write `is_palindrome_two_pointer(s)` using a left and right index instead of `[::-1]`.
4. Write `most_frequent_char(s)`.
5. Write `compress(s)`: `"aaabbc"` → `"a3b2c1"`.
6. Write `longest_word(sentence)`.
7. Write `is_anagram_counter(a, b)` using a dictionary instead of `sorted`.
8. What does `remove_duplicates("programming")` return? Why is `set()` not enough?

## 02 Lists

9. Write `second_largest(nums)` without sorting.
10. Write `find_missing(nums)` for a list of 1..n with one number missing.
11. Write `merge_sorted(a, b)` using two pointers.
12. Write `rotate_right(nums, k)` and test with `k = 0`, `k = len(nums)` and `k > len(nums)`.
13. Write `move_zeros_in_place(nums)` that changes the same list without making a new one.
14. Write `two_sum_brute(nums, target)` with two loops, then compare it with the hash-map version.
15. Write `three_sum_exists(nums, target)`.
16. Write `find_duplicates_list(nums)` that returns every value repeated.

## 03 Dictionaries

17. Write `invert_dict(d)` that swaps keys and values.
18. Write `group_by_length(words)`: `["a", "bb", "cc"]` → `{1: ["a"], 2: ["bb", "cc"]}`.
19. Rewrite `word_count` using `collections.Counter`.
20. Write `top_n_words(text, n)`.
21. Write `merge_and_sum(a, b)` that adds the values for shared keys.
22. Write `first_unique_key(d)`.

## 04 Sets

23. Write `common_elements(a, b, c)` for three lists.
24. Write `has_duplicates(nums)` using a set, O(n).
25. Write `symmetric_difference(a, b)` (items in exactly one list).
26. Write `longest_consecutive(nums)` using a set.
27. Why can you not put a list inside a set? What can you use instead?

## 05 Matrix

28. Write `matrix_multiply(a, b)`.
29. Write `anti_diagonal_sum(matrix)`.
30. Write `rotate_90(matrix)`.
31. Write `spiral_order(matrix)`.
32. Write `search_sorted_matrix(matrix, target)` for a matrix where each row is sorted.
33. What does `matrix_add` do with matrices of different shapes? Why?

## 06 Searching

34. Write `first_occurrence(nums, target)` using binary search.
35. Write `last_occurrence(nums, target)`.
36. Write `insert_position(nums, target)` (where would it go to keep the list sorted?).
37. Rewrite `binary_search` using the `bisect` module.
38. Write `binary_search_recursive(nums, target, low, high)`.
39. What happens if you run binary search on an unsorted list?

## 07 Sorting

40. Write `insertion_sort(nums)`.
41. Add a counter to `bubble_sort` to count swaps. Compare a sorted and a reversed list.
42. Write `sort_by_length(words)` using `sorted(words, key=len)`.
43. Sort a list of dictionaries by one key.
44. Write `is_sorted(nums)`.
45. Explain why `bubble_sort` stops early when `swapped` is `False`.

## 08 Recursion

46. Write `power(base, exp)` recursively.
47. Write `reverse_string_recursive(s)`.
48. Write `is_palindrome_recursive(s)`.
49. Write `digit_sum(n)` recursively.
50. Write `count_down(n)` that prints `n` to `1`.
51. Rewrite `fibonacci` using a loop. Compare the speed with the plain recursive version for `n = 35`.
52. What happens with `sum_numbers(5000)`? Fix it with a formula.

## 09 File Handling

53. Write `append_line(filename, text)`.
54. Write `count_lines(filename)`.
55. Write `longest_line(filename)`.
56. Write `word_frequency_file(filename)`.
57. Write `copy_file(source, target)`.
58. What happens if you read a file that does not exist? Handle it with `try / except FileNotFoundError`.

## 10 OOP

59. Add `transfer(self, other, amount)` to `BankAccount`.
60. Add `__str__` to `Employee` so `print(employee)` shows the details.
61. Add `give_raise(self, percent)` to `Employee`.
62. Create `Manager(Employee)` with a `bonus` attribute.
63. Create a `Student` class that stores marks and returns the average.
64. Keep a transaction history list inside `BankAccount`.

## 11 Patterns

65. Accumulator: write `product(nums)`.
66. Counter: write `count_even(nums)`.
67. Frequency: write `most_common_number(nums)`.
68. Two pointer: write `is_pair_sum_sorted(nums, target)`.
69. Two pointer: write `remove_duplicates_sorted(nums)` in place.
70. Sliding window: write `average_of_k(nums, k)`.
71. Sliding window: write `longest_unique_substring(s)`.
72. Why is the sliding window solution O(n) and the slice-sum version O(n·k)?

## Mixed Timed Challenges

73. In 20 minutes: solve problems 11, 24 and 34 with no help.
74. Take any three functions from this phase and write the brute-force version, the better version and the Big-O of each.
75. Pick one function and list five edge cases. Check how your function behaves for each.