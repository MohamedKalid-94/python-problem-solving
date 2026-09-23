# Problem 16 — Find Second Largest Number

## Problem

Find the largest and second largest distinct numbers in a list without using `max()`, `sorted()`, or `sort()`.

## Input

numbers = [10, 45, 20, 89, 56, 89, 30]

## Output

Largest Number = 89
Second Largest Number = 56

## Approach

* Initialize `largest` with the first number.
* Initialize `second_largest` as `None`.
* Loop through the numbers.
* Update `largest` when a larger number is found.
* Move the old `largest` to `second_largest`.
* Ignore duplicate values of the largest number.
* Handle the case where a second distinct value does not exist.

## Pattern

Maintain Multiple States + Edge Case Handling

## Complexity

* Time: O(n)
* Space: O(1)
