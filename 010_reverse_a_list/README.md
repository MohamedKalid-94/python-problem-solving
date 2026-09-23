# Problem 10 — Reverse a List

## Problem

Reverse a list without using `reverse()`, `reversed()`, or slicing.

## Input

```python
numbers = [10, 20, 30, 40, 50]
```

## Output

```text
Reversed List = [50, 40, 30, 20, 10]
```

## Approach

* Start from the last index.
* Move backward using `range()`.
* Add each element to a new list using `append()`.

## Pattern

**Backward Index Traversal**

## Complexity

* **Time:** `O(n)`
* **Space:** `O(n)`
