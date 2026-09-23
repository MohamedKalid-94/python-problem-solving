# Problem 13 — Find First Occurrence

## Problem

Find the index of the first occurrence of a target number in a list.

## Input

numbers = [10, 20, 10, 30, 10, 40, 20]
target = 20

## Output

First Occurrence Index = 1

## Approach

* Start with `first_index = -1`.
* Loop through the indexes.
* Check whether the current number matches the target.
* Store the index when found.
* Use `break` to stop after the first match.

## Pattern

Linear Search + Index Tracking + Break

## Complexity

* Time: O(n)
* Space: O(1)
