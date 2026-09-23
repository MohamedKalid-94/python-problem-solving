# Problem 15 — Remove Duplicate Values

## Problem

Create a new list containing each value only once without using `set()`, `count()`, or `dict.fromkeys()`.

## Input

numbers = [10, 20, 10, 30, 20, 40, 50, 10]

## Output

Unique Values = [10, 20, 30, 40, 50]

## Approach

* Create an empty `unique` list.
* Loop through each number.
* Check whether the number is already in `unique`.
* If not, add it using `append()`.

## Pattern

Seen Check + Conditional Append

## Complexity

* Time: O(n²)
* Space: O(n)
