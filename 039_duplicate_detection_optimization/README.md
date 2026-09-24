# Problem 39 — Duplicate Detection and Optimization

## Problem

Determine whether a list contains any duplicate value.

The problem is solved using two approaches:
1. Brute force using nested loops
2. Optimized approach using a dictionary

## Input

numbers = [10, 20, 30, 40, 40, 50]

## Output

Duplicate Found = True

## Approach 1 — Brute Force

- Use two loops to compare pairs of numbers.
- Start the second loop from `i + 1` to avoid comparing a number with itself.
- Stop when a duplicate is found.

## Approach 2 — Dictionary

- Create a dictionary called `seen`.
- Loop through each number.
- Check whether the number already exists in `seen`.
- If it exists, a duplicate has been found.
- Otherwise, store the number in `seen`.
- Use `break` to stop when a duplicate is found.

## Pattern

Hashing + Lookup + Early Exit

## Key Concept

The dictionary allows fast average-case lookup.

Instead of comparing every pair:

`Have I seen this number before?`

## Complexity

### Brute Force
- Time: O(n²)
- Space: O(1)

### Dictionary
- Time: O(n) average
- Space: O(n)

## Optimization

The dictionary approach uses additional memory to reduce the time complexity from O(n²) to O(n) average.