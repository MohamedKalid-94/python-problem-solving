# 002 · Max of List

**Difficulty:** Easy · **Pattern:** Best so far · **Code:** [`max_of_list.py`](../../phase_0_basics/max_of_list.py)

## Problem
Return the biggest number in a list without using `max()`. Return `None` for an empty list.

## Examples
| Input | Output |
|---|---|
| `[3, 9, 2]` | `9` |
| `[-5, -2, -9]` | `-2` |
| `[7]` | `7` |
| `[]` | `None` |

## Pseudocode
```text
if the list is empty: return None
biggest = first number
for each number in the list:
    if number > biggest:
        biggest = number
return biggest
```

## How it works
1. An empty list has no biggest number, so return `None`.
2. Assume the first number is the biggest for now.
3. Compare every number with `biggest` and replace it when a larger one appears.

## Edge cases
Start with `nums[0]`, not `0`. Starting at 0 gives the wrong answer for all-negative lists.

## Complexity
Time: O(n) · Space: O(1)