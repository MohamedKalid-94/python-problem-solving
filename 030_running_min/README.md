# Problem 30 — Running Minimum

## Problem
Create a new list where each element represents the minimum number seen so far while traversing the original list.

## Input
numbers = [3, 1, 5, 2, 8, 4]

## Output
Running Minimum = [3, 1, 1, 1, 1, 1]

## Approach
- Initialize `min_so_far` with the first number.
- Create an empty `running_min` list.
- Loop through each number.
- Compare the current number with `min_so_far`.
- If the current number is smaller, update `min_so_far`.
- Append `min_so_far` to the result list.

## Pattern
Running State / Best-So-Far

## Complexity
- Time: O(n)
- Space: O(n)

## Key Concept
`min_so_far` always stores the smallest number encountered up to the current position.

Example:

`3 → 3`

`1 → 1`

`5 → 1`

`2 → 1`

`8 → 1`

`4 → 1`