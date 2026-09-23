# Problem 23 — Find First Non-Repeating Number

## Problem

Find the first number in a list that appears exactly once.

## Input

numbers = [10, 20, 10, 5, 20, 40, 30]

## Output

First Non-Repeating Number = 5

## Approach

### Phase 1 — Frequency Counting

* Create a dictionary called `frequency`.
* Count how many times each number appears.

### Phase 2 — Find First Unique Number

* Loop through the original list again.
* Check whether the current number has a frequency of `1`.
* Store the number and use `break` to stop at the first match.

## Pattern

Frequency / Hashing + Linear Search

## Complexity

* Time: O(n)
* Space: O(k)

Where `k` is the number of unique values.
