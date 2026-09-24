# Problem 37 — Check if List is Sorted

## Problem
Determine whether a list of numbers is sorted in ascending order.

Equal values are allowed.

## Input

numbers = [1, 2, 3, 4, 5, 6, 7]

## Output

Sorting Status = True

## Approach

- Assume the list is sorted by setting `is_sorted = True`.
- Start checking from index `1` because every element needs to be compared with the previous element.
- Compare the current number with the previous number.
- If the current number is smaller than the previous number, the ascending order is broken.
- Set `is_sorted = False`.
- Use `break` because there is no need to continue checking.

## Pattern

Adjacent Element Comparison + Boolean State + Early Exit

## Key Concept

For ascending order:

`current < previous` → Order is broken

Example:

`[1, 2, 3, 4]` → Sorted

`[1, 2, 4, 3]` → Not Sorted

Because:

`3 < 4`

## Edge Cases

- Already sorted list → `True`
- Unsorted list → `False`
- Descending list → `False`
- Duplicate values → `True`
- Single-element list → `True`
- Empty list → `True`

## Complexity

- Time: O(n)
- Space: O(1)