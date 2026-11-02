# 001 · Sum of List

**Difficulty:** Easy · **Pattern:** Accumulator · **Code:** [`sum_of_list.py`](../../phase_0_basics/sum_of_list.py)

## Problem
Given a list of numbers, return their sum without using `sum()`.

## Examples
| Input | Output |
|---|---|
| `[1, 2, 3]` | `6` |
| `[]` | `0` |
| `[-1, 1]` | `0` |

## Pseudocode
```text
total = 0
for each number in the list:
    add the number to total
return total
```

## How it works
1. `total` starts at 0, like an empty bucket.
2. The loop takes each number one by one.
3. Each number is added to `total`.
4. After the loop, `total` holds the final sum.

## Edge cases
Empty list (the loop never runs, so the answer is 0) and negative numbers.

## Complexity
Time: O(n) · Space: O(1)