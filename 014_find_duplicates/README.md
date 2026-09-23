# Problem 14 — Find Duplicate Values

## Problem

Find the values that appear more than once in a list without using `set()`, `count()`, or `Counter`.

## Input

numbers = [10, 20, 10, 30, 20, 40, 50, 10]

## Output

Duplicate Values = [10, 20]

## Approach

* Maintain a `seen` list.
* If a number is already in `seen`, it is a duplicate.
* Add the duplicate only if it is not already in `duplicates`.
* Otherwise, add the number to `seen`.

## Pattern

Track → Detect → Avoid Repeating

## Complexity

* Time: O(n²)
* Space: O(n)
