# 007 · Reverse String

**Difficulty:** Easy · **Pattern:** Build a new string · **Code:** [`reverse_string.py`](../../phase_0_basics/reverse_string.py)

## Problem
Reverse a string without using `[::-1]`.

## Examples
| Input | Output |
|---|---|
| `"hello"` | `"olleh"` |
| `"a"` | `"a"` |
| `""` | `""` |

## Pseudocode
```text
new_string = empty
for each character in s:
    put the character in FRONT of new_string
return new_string
```

## How it works
```text
start: ""
h -> "h"
e -> "eh"
l -> "leh"
l -> "lleh"
o -> "olleh"
```

## Edge cases
Empty string and a single character.

## Complexity
Time: O(n²) (each prepend copies the string) · Space: O(n)
A faster version using a list and `join` comes in a later phase.