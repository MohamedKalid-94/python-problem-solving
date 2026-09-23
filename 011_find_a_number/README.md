# Problem 11 — Find a Number

## Problem

Check whether a target number exists in a list without using `in()`, `index()`, or other built-in search functions.

## Input

```python
numbers = [12, 45, 7, 89, 23, 56]
target = 23
```

## Output

```text
Found
```

## Approach

* Start with `found = False`.
* Loop through each number.
* If the number matches the target, set `found = True`.
* Check the final value after the loop.

## Pattern

**Linear Search + Boolean State**

## Complexity

* **Time:** `O(n)`
* **Space:** `O(1)`
