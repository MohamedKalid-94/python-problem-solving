# Problem 26 — Maximum Sum of Consecutive Elements

## Problem

Find the maximum sum of `window_size` consecutive numbers in a list.

## Input

numbers = [2, 1, 5, 1, 3, 2]
window_size = 3

## Output

Maximum Sum = 9

## Approach

### Step 1 — Build the First Window

Calculate the sum of the first `window_size` elements.

For the first window:

`2 + 1 + 5 = 8`

### Step 2 — Slide the Window

Move the window one position at a time.

Instead of calculating the complete sum again:

`New Sum = Previous Sum - Leaving Element + Entering Element`

The window sums are:

* `[2, 1, 5]` → 8
* `[1, 5, 1]` → 7
* `[5, 1, 3]` → 9
* `[1, 3, 2]` → 6

The maximum is `9`.

## Pattern

Fixed-Size Sliding Window

## Complexity

* Time: O(n)
* Space: O(1)

## Key Concept

When a fixed-size window moves:

`Leaving Element = numbers[index - window_size]`

`Entering Element = numbers[index]`
