# Problem 25 — Two Sum Using Hashing

## Problem

Find two numbers in a list whose sum equals a given target using a dictionary.

## Input

numbers = [10, 20, 30, 40, 50]
target = 70

## Output

Pair = 30, 40

## Approach

* Create an empty dictionary called `seen`.
* Loop through each number.
* Calculate the required number using:
  `complement = target - number`
* Check whether the complement already exists in `seen`.
* If it exists, the pair has been found.
* Otherwise, store the current number in `seen`.
* Use `break` after finding the pair.

## Key Concept

For every current number:

`Current Number + Complement = Target`

Therefore:

`Complement = Target - Current Number`

Example:

`70 - 40 = 30`

Since `30` was already seen:

`30 + 40 = 70`

## Pattern

Hashing + Complement Lookup

## Complexity

* Time: O(n) average
* Space: O(n)

## Comparison

### Problem 24 — Nested Loops

* Time: O(n²)
* Space: O(1)

### Problem 25 — Hashing

* Time: O(n) average
* Space: O(n)

The hashing approach uses extra memory to reduce the number of comparisons.
