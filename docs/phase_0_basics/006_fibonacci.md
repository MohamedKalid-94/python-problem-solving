# 006 · Fibonacci

**Difficulty:** Easy · **Pattern:** Two variables · **Code:** [`fibonacci.py`](../../phase_0_basics/fibonacci.py)

## Problem
Return the first `n` Fibonacci numbers as a list. Each number is the sum of the two before it.

## Examples
| Input | Output |
|---|---|
| `0` | `[]` |
| `1` | `[0]` |
| `10` | `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]` |

## Pseudocode
```text
result = empty list
a = 0, b = 1
repeat n times:
    add a to result
    next = a + b
    a = b
    b = next
return result
```

## How it works
`a` is the current number and `b` is the next one. Each round saves `a`, then moves both forward. `next_number` holds the new value temporarily so nothing is overwritten too early.

## Edge cases
`n = 0` returns an empty list. `n = 1` returns only `[0]`.

## Complexity
Time: O(n) · Space: O(n)