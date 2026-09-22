# Problem 3 — Find Largest and Smallest Number

## Problem

Given a list of numbers, find the **largest** and **smallest** numbers without using:

* `max()`
* `min()`
* `sorted()`
* `sort()`

The solution should scan the list only once.

## Input

```python
numbers = [12, 45, 7, 89, 23, 56]
```

## Expected Output

```text
Largest Number = 89
Smallest Number = 7
```

## Approach

We maintain two variables:

```text
largest  → largest number seen so far
smallest → smallest number seen so far
```

### Steps

1. Initialize both `largest` and `smallest` with the first element.
2. Loop through every number in the list.
3. If the current number is greater than `largest`, update `largest`.
4. If the current number is smaller than `smallest`, update `smallest`.
5. Print the final values.

## Python Implementation

See the complete implementation in [`solution.py`](solution.py).

```python
numbers = [12, 45, 7, 89, 23, 56]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:

    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print("Largest Number =", largest)
print("Smallest Number =", smallest)
```

## Manual Trace

| Number | Largest | Smallest |
| -----: | ------: | -------: |
|     12 |      12 |       12 |
|     45 |      45 |       12 |
|      7 |      45 |        7 |
|     89 |      89 |        7 |
|     23 |      89 |        7 |
|     56 |      89 |        7 |

## Complexity

**Time Complexity:** `O(n)`

The list is scanned once.

**Space Complexity:** `O(1)`

Only two additional variables are used.

## Pattern Learned

### Maintain Multiple States

While scanning a collection, maintain multiple pieces of information and update each one independently.

In this problem:

```text
largest
smallest
```

This pattern is useful for many problems involving tracking minimum, maximum, counts, or other running values.

## Edge Cases Considered

* Positive numbers
* Negative numbers
* Mixed positive and negative numbers
* Duplicate numbers
* Single-element list

### Note

The current implementation assumes that the input list contains at least one element. An empty list would cause an `IndexError` when accessing `numbers[0]`.
