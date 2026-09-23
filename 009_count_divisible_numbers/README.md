# Problem 9 — Count Divisible Numbers

## Problem

Count how many numbers in a list are divisible by a given divisor.

## Input

```python
numbers = [10, 15, 20, 22, 30, 35, 40]
divisor = 5
```

## Output

```text
Count = 6
```

## Approach

* Initialize `count` to `0`.
* Loop through each number.
* Use `%` to check the remainder.
* If the remainder is `0`, increment the counter.

## Pattern

**Modulo + Condition + Counter**

## Complexity

* **Time:** `O(n)`
* **Space:** `O(1)`

> The divisor must not be `0`.
