# Problem 22 — Count Numbers Greater Than Previous

## Problem

Count how many numbers in a list are greater than the number immediately before them.

## Input

numbers = [10, 15, 12, 20, 25, 18, 30]

## Output

Count = 4

## Approach

* Start the loop from index `1` because index `0` has no previous element.
* Compare the current number with the previous number.
* If the current number is greater, increment the counter.
* Continue until the end of the list.

## Pattern

Previous Element Comparison

## Key Concept

When comparing an element with its previous element:

`numbers[index]` → current element

`numbers[index - 1]` → previous element

Therefore, the loop starts at `1`.

## Complexity

* Time: O(n)
* Space: O(1)
