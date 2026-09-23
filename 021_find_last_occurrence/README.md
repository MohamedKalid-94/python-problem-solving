# Problem 21 — Find Last Occurrence

## Problem

Find the index of the last occurrence of a target number in a list.

## Input

numbers = [10, 20, 30, 20, 40, 20, 50]
target = 20

## Output

Last Occurrence Index = 5

## Approach

* Initialize `last_index` as `-1`.
* Loop through all indexes in the list.
* If the current number matches the target, update `last_index`.
* Continue the loop so later occurrences can replace the previous index.
* If the target is not found, `last_index` remains `-1`.

## Pattern

Keep Updating / Last Match

## Complexity

* Time: O(n)
* Space: O(1)
