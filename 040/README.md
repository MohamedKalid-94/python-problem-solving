# Problem 38 — Largest Even Number

## Problem

Find the largest even number in a list.

If the list contains no even numbers, return `None`.

## Input

numbers = [1, 7, 10, 4, 3, 14, 7]

## Output

Largest Even Number = 14

## Approach

- Initialize `largest_even` as `None`.
- Loop through every number in the list.
- Check whether the number is even using `% 2 == 0`.
- If it is the first even number, store it.
- Otherwise, compare it with `largest_even`.
- Update `largest_even` only when the current number is larger.
- If no even number exists, `largest_even` remains `None`.

## Pattern

Filtering + Best-So-Far + Edge Case Handling

## Key Concept

Only update the answer when the current value improves it.

`number % 2 == 0` → Even number

`number > largest_even` → Found a larger even number

## Edge Cases

- Multiple even numbers → find the largest
- One even number → return that number
- No even numbers → `None`
- Duplicate even numbers → handled correctly
- Negative even numbers → handled correctly

## Complexity

- Time: O(n)
- Space: O(1)