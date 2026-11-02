# 009 · Count Vowels

**Difficulty:** Easy · **Pattern:** Counting with `in` · **Code:** [`count_vowels.py`](../../phase_0_basics/count_vowels.py)

## Problem
Count the vowels (a, e, i, o, u) in a string, ignoring upper or lower case.

## Examples
| Input | Output |
|---|---|
| `"Hello World"` | `3` |
| `"AEIOU"` | `5` |
| `"xyz"` | `0` |

## Pseudocode
```text
convert s to lowercase
count = 0
for each character in s:
    if the character is a, e, i, o or u:
        add 1 to count
return count
```

## How it works
`s.lower()` makes `A` and `a` the same. `ch in "aeiou"` is True when the character is one of the five vowels.

## Edge cases
Empty string, uppercase letters, and strings with no vowels.

## Complexity
Time: O(n) · Space: O(1)