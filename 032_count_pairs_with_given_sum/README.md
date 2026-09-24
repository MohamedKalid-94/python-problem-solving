# Problem 32 — Count Pairs with Given Sum

## Problem
Count how many pairs of elements in a list have a sum equal to a given target.

## Input
numbers = [1, 5, 7, -1, 5]
target = 6

## Output
Pair Count = 3

## Approach
- Create an empty dictionary called `seen`.
- Create a counter called `pair_count`.
- Loop through each number.
- Calculate the required complement:
  `complement = target - number`
- Check whether the complement has already been seen.
- If it has, increment `pair_count`.
- Store the current number in `seen`.
- Continue through the entire list because we need to count all valid pairs.

## Pattern
Hashing + Complement Lookup + Counting

## Key Concept
For every current number:

`Current Number + Complement = Target`

Therefore:

`Complement = Target - Current Number`

Example:

`5 + 1 = 6`

When the current number is `5`:

`6 - 5 = 1`

If `1` was already seen, a valid pair exists.

## Complexity
- Time: O(n) average
- Space: O(n)