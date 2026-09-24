# Problem 29 — Running Maximum

## Problem
Create a new list where each element represents the maximum number seen so far while traversing the original list.

## Input
numbers = [3, 1, 5, 2, 8, 4]

## Output
Running Maximum = [3, 3, 5, 5, 8, 8]

## Approach
- Initialize `max_so_far` with the first number.
- Create an empty `running_max` list.
- Loop through each number.
- Compare the current number with `max_so_far`.
- If the current number is greater, update `max_so_far`.
- Append `max_so_far` to the result list.

## Pattern
Running State / Best-So-Far

## Complexity
- Time: O(n)
- Space: O(n)

## Key Concept
`max_so_far` always stores the largest number encountered up to the current position.

Example:

`3 → 3`

`1 → 3`

`5 → 5`

`2 → 5`

`8 → 8`

`4 → 8`