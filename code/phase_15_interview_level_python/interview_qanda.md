# Interview Questions & Answers - Interview-Level Python

## Beginner

### 1. How do you reverse a string in Python?
Use slicing: `s[::-1]`. It creates a new string, because strings are immutable.

### 2. How do you check if a string is a palindrome?
Clean it (keep letters and digits, ignore case), then compare it with its reverse. Without cleaning, `"A man, a plan..."` fails.

### 3. How do you count how many times each character appears?
Loop and use a dictionary: `result[ch] = result.get(ch, 0) + 1`. Or use `collections.Counter(s)`.

### 4. How do you find the maximum of a list?
`max(nums)`. It raises `ValueError` on an empty list, so check for that first.

### 5. How do you remove duplicates from a list?
`list(set(nums))` removes them but loses the order. `list(dict.fromkeys(nums))` removes them and keeps the order.

### 6. What is the difference between a list, a set and a dictionary?
A list is ordered and allows duplicates. A set is unordered and unique. A dictionary maps keys to values.

### 7. What does `with open(...)` do?
It opens the file and closes it automatically when the block ends, even if an error happens.

## Intermediate

### 8. How do you check whether two strings are anagrams?
Compare their sorted letters (O(n log n)), or compare character counts with `Counter` (O(n)). Ignore case and spaces first.

### 9. Why does `"".join(set("programming"))` give a different order each time?
A set has no guaranteed order. Use `"".join(dict.fromkeys(s))` to keep the first-seen order.

### 10. How does the Two Sum hash-map solution work?
For each number, check whether `target - number` is already in a dictionary of numbers seen so far. If yes, return both indexes. If no, store this number. It runs in O(n) time and O(n) space, compared with O(n²) for two loops.

### 11. How do you rotate a list by `k` positions?
`k = k % len(nums)`, then `nums[-k:] + nums[:-k]`. The `%` handles `k` larger than the list. Handle the empty list separately.

### 12. What is the difference between linear search and binary search?
Linear search checks each item (O(n), any list). Binary search halves the range each step (O(log n)) but needs a **sorted** list.

### 13. How do you find the transpose of a matrix?
`list(map(list, zip(*matrix)))`. `zip(*matrix)` groups the columns, and each column becomes a row.

### 14. What are the base case and recursive case?
The base case stops the recursion (`n == 0`). The recursive case calls the function again with a smaller input. Without a reachable base case you get `RecursionError`.

### 15. Why is bubble sort rarely used in practice?
It is O(n²). Python's built-in `sorted()` is O(n log n). Bubble sort is for learning.

### 16. What is the difference between `sorted()` and `list.sort()`?
`sorted()` returns a new list and works on any iterable. `.sort()` sorts the list in place and returns `None`.

### 17. What happens when you call `withdraw` with more money than the balance?
The corrected `BankAccount` raises `ValueError("insufficient balance")`. Silently ignoring it would hide the bug from the caller.

## Advanced

### 18. Why is the plain recursive Fibonacci so slow?
It recomputes the same values many times, so the calls grow as O(2ⁿ). Memoization (`@lru_cache`) stores each answer, which makes it O(n).

### 19. What is the recursion limit in Python, and what do you do about it?
The default limit is about 1000 calls. For deep problems use a loop, a formula (`n * (n + 1) // 2`), or restructure the algorithm.

### 20. What is the difference between O(n²) and O(n) for Two Sum?
Brute force checks every pair with two loops (O(n²) time, O(1) extra space). The hash-map version trades memory for speed (O(n) time, O(n) space).

### 21. Why is the original sliding window solution O(n·k)?
`sum(nums[i:i+k])` re-adds `k` numbers for every window. The sliding window keeps a running total: add the new number, subtract the one that left. That is O(n).

### 22. When does the two-pointer technique work?
When the list is **sorted** (or the problem has an order). Moving the left pointer increases the sum, and moving the right pointer decreases it.

### 23. Why must binary search use sorted data?
Each step discards half the list by assuming everything left of `mid` is smaller and everything right is bigger. On unsorted data that assumption breaks and the answer is wrong.

### 24. Is `(low + high) // 2` safe?
In Python yes, because integers do not overflow. In languages like Java or C, use `low + (high - low) // 2` to avoid overflow.

### 25. What is a stable sort?
A stable sort keeps equal items in their original order. Bubble sort and Python's `sorted()` are stable. Selection sort (with swaps) is not.

### 26. Why use `dict.fromkeys` instead of a set to remove duplicates?
Dictionaries keep insertion order (Python 3.7+). `dict.fromkeys(items)` keeps the first occurrence of each item in order, in O(n).

### 27. What is the time complexity of `x in list` vs `x in set`?
`x in list` is O(n). `x in set` is O(1) on average, because it uses hashing.

### 28. Why should you pass the file name as a parameter?
A function with a hardcoded file name is hard to reuse and test, and it may overwrite a file you did not mean to. A parameter (with a default) fixes that.

### 29. Why is building a string with `s = s + ch` in a loop not ideal for big inputs?
Each addition may copy the whole string. For large inputs, collect characters in a list and use `"".join(parts)`.

### 30. How would you explain Big-O in one sentence?
Big-O describes how the running time or memory grows as the input size grows, ignoring constant factors.

## Practical Tasks

1. Write `two_sum` in O(n) and explain why a dictionary makes it fast.
2. Remove duplicates from a list while keeping order.
3. Implement binary search and explain why the list must be sorted.
4. Rotate a list by `k`, including `k` larger than the list.
5. Write recursive factorial and explain the base case.
6. Fix `fibonacci(40)` so it runs instantly.
7. Convert a slow slice-sum window into a true sliding window.
8. Add validation to a bank account class and test it with bad input.