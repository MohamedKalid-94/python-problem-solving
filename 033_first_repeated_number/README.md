# Problem 33 — Find the First Repeated Number

## Problem
Find the first number that appears more than once while scanning the list from left to right.

## Input
numbers = [10, 20, 10, 5, 20, 40, 30]

## Output
First Repeating Number = 10

## Approach
- Create an empty dictionary called `seen`.
- Initialize `first_repeating` as `None`.
- Loop through the numbers from left to right.
- Check whether the current number already exists in `seen`.
- If it exists, the number has appeared before.
- Store it as `first_repeating`.
- Use `break` because we only need the first repeated number.
- If no number repeats, `first_repeating` remains `None`.

## Pattern
Hashing + Lookup + Early Exit

## Key Concept
`seen` keeps track of numbers encountered earlier.

Example:

`10 → store`

`20 → store`

`10 → already seen → FOUND`

## Complexity
- Time: O(n) average
- Space: O(n)