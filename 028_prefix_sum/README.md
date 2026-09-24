# Problem 28 — Prefix Sum

## Problem
Create a new list where each element represents the sum of all elements from the beginning of the original list up to that position.

## Input
numbers = [2, 4, 1, 5, 3]

## Output
Prefix Sum = [2, 6, 7, 12, 15]

## Approach
- Start a running total with `count = 0`.
- Create an empty `prefix_sum` list.
- Loop through each number.
- Add the current number to the running total.
- Store the running total in `prefix_sum`.

## Pattern
Prefix Sum / Running State

## Complexity
- Time: O(n)
- Space: O(n)

## Key Concept
The current prefix sum is built using the previous prefix sum:

`Current Sum = Previous Sum + Current Number`

Example:

`2 → 2`

`2 + 4 → 6`

`6 + 1 → 7`

`7 + 5 → 12`

`12 + 3 → 15`