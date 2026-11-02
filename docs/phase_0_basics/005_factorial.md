# 005 · Factorial

**Difficulty:** Easy · **Pattern:** Accumulator · **Code:** [`factorial.py`](../../phase_0_basics/factorial.py)

## Problem
Return n! (the product of all whole numbers from 1 to n).

## Examples
| Input | Output |
|---|---|
| `5` | `120` |
| `1` | `1` |
| `0` | `1` |

## Pseudocode
```text
result = 1
for i from 1 to n:
    multiply result by i
return result
```

## How it works
1. `result` starts at 1, because starting at 0 would make every product 0.
2. `range(1, n + 1)` gives 1, 2, ... n.
3. Each number is multiplied into `result`.

## Edge cases
`0! = 1` by definition. The loop does not run for 0, so the answer stays 1.

## Complexity
Time: O(n) · Space: O(1)