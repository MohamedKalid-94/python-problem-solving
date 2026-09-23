# Problem 24 — Two Sum Using Nested Loops

## Problem

Find two numbers in a list whose sum equals a given target.

## Input

numbers = [10, 20, 30, 40, 50]
target = 70

## Output

Pair = 20, 50

## Approach

* Use two indexes, `i` and `j`.
* The outer loop selects the first number.
* The inner loop starts from `i + 1` so the same pair is not checked twice.
* Add the two numbers and compare the result with the target.
* Print the pair when the sum matches the target.

## Pattern

Nested Loop + Pair Search

## Complexity

* Time: O(n²)
* Space: O(1)

## Key Concept

Using:

`range(i + 1, len(numbers))`

prevents:

* Comparing a number with itself.
* Checking the same pair twice.
