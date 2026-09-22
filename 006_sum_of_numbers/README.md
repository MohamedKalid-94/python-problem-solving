# Problem 6 — Sum of Numbers

## Problem

Given a list of numbers, calculate the sum of all numbers without using the built-in `sum()` function.

## Input

```python
numbers = [12, 45, 7, 89, 23, 56]
```

## Expected Output

```text
Total = 232
```

## Approach

1. Initialize `total` to `0`.
2. Loop through each number.
3. Add each number to `total`.
4. Print the final total.

## Python Implementation

See [`solution.py`](solution.py).

```python
numbers = [12, 45, 7, 89, 23, 56]

total = 0

for number in numbers:
    total += number

print("Total =", total)
```

## Pattern

**Accumulator Pattern**

```python
total = 0

for item in items:
    total += item
```

## Complexity

* **Time:** `O(n)`
* **Space:** `O(1)`
