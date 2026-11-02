# 010 · Word Frequency

**Difficulty:** Easy · **Pattern:** Dictionary counting · **Code:** [`word_frequency.py`](../../phase_0_basics/word_frequency.py)

## Problem
Return a dictionary showing how many times each word appears in a text, ignoring case.

## Examples
| Input | Output |
|---|---|
| `"a a b"` | `{"a": 2, "b": 1}` |
| `"The the THE cat"` | `{"the": 3, "cat": 1}` |
| `""` | `{}` |

## Pseudocode
```text
counts = empty dictionary
split the lowercase text into words
for each word:
    if the word is already in counts:
        add 1 to its count
    otherwise:
        set its count to 1
return counts
```

## How it works
The dictionary stores word → number of times seen. A new word starts at 1, and a repeated word goes up by 1.

## Edge cases
Empty text, mixed case, and repeated spaces (`split()` handles them).

## Complexity
Time: O(n) · Space: O(k), where k is the number of unique words