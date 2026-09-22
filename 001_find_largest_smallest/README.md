# Problem 001 — Find the Largest Number

## Problem

Given a list of numbers, find the largest number without using Python's built-in `max()` or `sorted()` functions.

## Example

### Input

```python
numbers = [12, 45, 7, 89, 23, 56]
```

### Output

```text
Largest Number: 89
```

## Approach

Use the **"best so far"** pattern.

1. Assume the first number is the largest.
2. Loop through the numbers.
3. Compare the current number with `largest`.
4. If the current number is larger, update `largest`.
5. Continue until all numbers are checked.

## Pseudocode

```text
largest = first number

for each number:
    if number > largest:
        largest = number

print largest
```

## Python Implementation

```python
numbers = [12, 45, 7, 89, 23, 56]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Largest Number:", largest)
```

## Complexity

* Time Complexity: **O(n)**
* Space Complexity: **O(1)**

## Key Pattern Learned

### Best So Far

Maintain the best value found while scanning the list.

This pattern can be used for:

* Largest number
* Smallest number
* Highest score
* Lowest price
* Maximum value
* Minimum value

## Edge Cases Tested

```text
[1, 2, 3, 4, 5]          → 5
[12, 45, 7, 89, 23, 56]  → 89
[-10, -5, -20, -3, -8]   → -3
[100]                     → 100
[5, 5, 5, 5]             → 5
```

## Main Lesson

Don't immediately think about sorting the entire list.

Ask:

> "Can I solve this by keeping only the information I need while scanning the data once?"
