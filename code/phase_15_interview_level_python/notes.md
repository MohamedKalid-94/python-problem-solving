# Notes - Interview-Level Python

## 1. Strings (01)

Strings are immutable, so every change creates a new string.

```python
s[::-1]                               # reverse
s.lower()                             # ignore case
"".join(dict.fromkeys(s))             # remove duplicates, keep order
sorted("listen") == sorted("silent")  # anagram check
```

**Palindrome:** clean the string first, then compare it with its reverse.

```python
"A man, a plan, a canal: Panama"   # -> "amanaplanacanalpanama"
```

**First non-repeating character:** count first, then scan again.

```python
freq = character_frequency(s)
for ch in s:
    if freq[ch] == 1:
        return ch
```

| Problem | Time |
|---|---|
| Reverse, palindrome, vowels | O(n) |
| Frequency, first non-repeating | O(n) |
| Anagram with `sorted` | O(n log n) |

## 2. Lists (02)

```python
max(nums), min(nums)               # O(n); raise ValueError on an empty list
list(dict.fromkeys(nums))          # remove duplicates, keep order
nums[::-1]                         # reverse (new list)
```

**Rotate:** move the last `k` items to the front.

```python
k = k % len(nums)          # k larger than the list wraps around
nums[-k:] + nums[:-k]      # [1,2,3,4] with k=1 -> [4,1,2,3]
```

**Move zeros:** keep non-zero items, then add the zeros.

```python
[x for x in nums if x != 0] + [0] * nums.count(0)
```

**Two Sum (hash map):** store each number and its index. For each new number, check whether `target - number` was already seen.

| Approach | Time | Space |
|---|---|---|
| Brute force (two loops) | O(n²) | O(1) |
| Hash map | O(n) | O(n) |

## 3. Dictionaries (03)

Counting pattern:

```python
result[ch] = result.get(ch, 0) + 1     # get returns 0 if the key is missing
```

- `from collections import Counter` does the same in one line: `Counter(text)`.
- Merge: `{**a, **b}` (the right side wins on duplicate keys). Python 3.9+ also has `a | b`.
- Filter with a dictionary comprehension: `{k: v for k, v in d.items() if v > 1}`.

## 4. Sets (04)

A set stores unique values, with no order and no indexing.

```python
set(a) & set(b)        # intersection (in both)
set(a) | set(b)        # union (in either)
set(a) - set(b)        # difference (in a, not in b)
set(a).issubset(set(b))
```

- Lookup (`x in my_set`) is O(1) on average, but O(n) on a list.
- Sets cannot contain lists or dicts (they are not hashable).

## 5. Matrices (05)

A matrix is a list of lists: `matrix[row][column]`.

```python
matrix = [[1, 2], [3, 4]]
matrix[1][0]                           # 3
list(map(list, zip(*matrix)))          # transpose -> [[1, 3], [2, 4]]
sum(matrix[i][i] for i in range(n))    # main diagonal (square matrix)
```

- Adding matrices needs the **same shape**, so check it first.
- Most matrix loops are O(rows × columns).

## 6. Searching (06)

| Algorithm | Needs sorted list? | Time |
|---|---|---|
| Linear search | No | O(n) |
| Binary search | **Yes** | O(log n) |

```python
low, high = 0, len(nums) - 1
while low <= high:
    mid = (low + high) // 2
    if nums[mid] == target: return mid
    elif nums[mid] < target: low = mid + 1     # search the right half
    else: high = mid - 1                       # search the left half
return -1
```

- Python also has `bisect` for binary search on sorted lists.
- With duplicates, this version returns any matching index.

## 7. Sorting (07)

| Algorithm | Best | Worst | Notes |
|---|---|---|---|
| Bubble sort (with early exit) | O(n) | O(n²) | Simple, stable, slow |
| Selection sort | O(n²) | O(n²) | Fewer swaps, not stable |
| `sorted()` / `.sort()` | O(n) | O(n log n) | Timsort, use this in real code |

- Bubble sort: swap neighbors; after round `i`, the last `i` items are final, so the inner loop shrinks. Stop when a round has no swaps.
- Sorting algorithms here change the list **in place**, so pass a `.copy()` to keep the original.

## 8. Recursion (08)

A recursive function needs:
1. A **base case** (when to stop)
2. A **recursive case** that moves toward the base case

```python
def factorial(n):
    if n == 0:                 # base case
        return 1
    return n * factorial(n - 1)
```

**Fibonacci:** the plain version recalculates the same values many times, which is O(2ⁿ).

```python
@lru_cache(maxsize=None)       # remember answers: now O(n)
def fibonacci(n): ...
```

- Python's default recursion limit is about 1000, so very deep recursion raises `RecursionError`. For big inputs, use a loop or a formula (`sum = n * (n + 1) // 2`).
- Always reject negative input, or the function never reaches the base case.

## 9. File Handling (09)

```python
with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Python Interview")
```

| Mode | Meaning |
|---|---|
| `"r"` | read (error if the file is missing) |
| `"w"` | write (creates or **overwrites**) |
| `"a"` | append to the end |

- `with` closes the file automatically, even if an error occurs.
- Pass the file name as a parameter instead of hardcoding it inside the function.
- Set `encoding="utf-8"` so it works the same on every computer.

## 10. OOP (10)

```python
class BankAccount:
    def __init__(self, name, balance): ...
    def deposit(self, amount): ...
    def withdraw(self, amount): ...
```

- `__init__` sets up the object's data.
- **Validate** inputs and `raise ValueError` for bad values instead of ignoring them.
- Catch it with `try / except ValueError as error`.
- Methods that calculate should usually `return`; printing belongs outside the class.

## 11. Coding Patterns (11)

| Pattern | Idea | Example |
|---|---|---|
| Accumulator | Add values into one total | Sum a list |
| Counter | Add 1 when a condition is true | Count positives |
| Frequency | Count items in a dictionary | Word count |
| Two pointer | Two indexes move inward on a **sorted** list | Pair with a target sum |
| Sliding window | Slide a fixed window, add the new, subtract the old | Max sum of `k` in a row |

**Sliding window:** O(n) instead of O(n·k).

```python
window += nums[i] - nums[i - k]     # add the new number, drop the old one
```

## Big-O Cheat Sheet

| Operation | Time |
|---|---|
| `list[i]`, `dict[key]`, `x in set` | O(1) average |
| `x in list`, `list.index(x)`, `list.count(x)` | O(n) |
| `list.pop(0)`, `list.insert(0, x)` | O(n) |
| `sorted(list)` | O(n log n) |
| Nested loops over n items | O(n²) |
| Binary search | O(log n) |

## Quick Revision

- Edge cases first: empty, one item, duplicates, negatives.
- Counting → dictionary. Uniqueness or membership → set.
- Sorted data → binary search or two pointers.
- A window over consecutive items → sliding window.
- Recursion needs a base case; add `lru_cache` when answers repeat.
- Always state the time complexity.