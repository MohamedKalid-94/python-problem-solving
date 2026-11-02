# 003 · Even or Odd

**Difficulty:** Easy · **Pattern:** Modulo · **Code:** [`even_or_odd.py`](../../phase_0_basics/even_or_odd.py)

## Problem
Return `"even"` or `"odd"` for a whole number.

## Examples
| Input | Output |
|---|---|
| `4` | `"even"` |
| `7` | `"odd"` |
| `0` | `"even"` |
| `-3` | `"odd"` |

## Pseudocode
```text
if the remainder of n divided by 2 is 0:
    return "even"
otherwise:
    return "odd"
```

## How it works
`n % 2` gives the remainder after dividing by 2. Remainder 0 means even, anything else means odd.

## Edge cases
Zero is even. In Python, `-3 % 2` is `1`, so negatives work correctly.

## Complexity
Time: O(1) · Space: O(1)