# Problem 31 — Find Pair with Given Difference

## Problem
Find two numbers in a list whose difference equals a given target.

## Input
numbers = [10, 20, 30, 40, 50]
target = 20

## Output
Pair = 10, 30

## Approach
- Create an empty dictionary called `seen`.
- Loop through each number.
- Calculate the required number using:
  `required = number - target`
- Check whether the required number already exists in `seen`.
- If it exists, the difference between the two numbers equals the target.
- Otherwise, store the current number in `seen`.
- Stop after finding the first valid pair.

## Pattern
Hashing + Lookup

## Key Concept
For a current number:

`Current Number - Required Number = Target`

Therefore:

`Required Number = Current Number - Target`

Example:

`30 - 10 = 20`

When the current number is `30`, the required number is:

`30 - 20 = 10`

Since `10` was already seen, the pair is `10, 30`.

## Complexity
- Time: O(n) average
- Space: O(n)