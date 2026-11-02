# 008 · Palindrome

**Difficulty:** Easy · **Pattern:** Compare with reverse · **Code:** [`palindrome.py`](../../phase_0_basics/palindrome.py)

## Problem
Return `True` if a string reads the same forwards and backwards.

## Examples
| Input | Output |
|---|---|
| `"racecar"` | `True` |
| `"hello"` | `False` |
| `""` | `True` |

## Pseudocode
```text
reversed_s = reverse of s
if s equals reversed_s:
    return True
otherwise:
    return False
```

## How it works
Build the reversed string (same idea as problem 007), then compare it with the original.

## Edge cases
Empty string and one character are palindromes. Case and spaces are not ignored in this version.

## Complexity
Time: O(n²) · Space: O(n)
A two-pointer version reaches O(n) time and O(1) space (Phase 3).