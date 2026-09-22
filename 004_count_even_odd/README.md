# Problem 4 — Count Even and Odd Numbers

## Problem

Given a list of integers, count how many numbers are **even** and how many are **odd**.

Do not use:

* `count()`
* List comprehensions
* External libraries

Use a `for` loop.

## Input

```python
numbers = [12, 7, 45, 8, 23, 10, 6, 9]
```

## Expected Output

```text
Odd Count = 4
Even Count = 4
```

## Approach

We maintain two counters:

```text
count_even → number of even values found
count_odd  → number of odd values found
```

### Steps

1. Initialize both counters to `0`.
2. Loop through each number in the list.
3. Use the modulo operator `%` to check divisibility by `2`.
4. If `number % 2 == 0`, increase the even counter.
5. Otherwise, increase the odd counter.
6. Print the final counts.

## Python Implementation

See the complete implementation in [`solution.py`](solution.py).

```python
numbers = [12, 7, 45, 8, 23, 10, 6, 9]

count_odd = 0
count_even = 0

for number in numbers:

    if number % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print("Odd Count =", count_odd)
print("Even Count =", count_even)
```

## How It Works

The modulo operator `%` gives the remainder after division.

```text
12 % 2 = 0 → Even
7 % 2 = 1  → Odd
8 % 2 = 0  → Even
9 % 2 = 1  → Odd
```

Therefore:

```text
Even Count = 4
Odd Count = 4
```

## Edge Cases Considered

### Negative numbers

```python
numbers = [-4, -3, -20, 7]
```

Negative numbers can also be correctly classified as even or odd.

### Zero

```python
0 % 2 == 0
```

Therefore, **0 is even**.

### Single element

```python
numbers = [5]
```

Output:

```text
Odd Count = 1
Even Count = 0
```

### Empty list

```python
numbers = []
```

Output:

```text
Odd Count = 0
Even Count = 0
```

No indexing is used, so the algorithm naturally handles an empty list.

## Complexity

**Time Complexity:** `O(n)`

The list is scanned once.

**Space Complexity:** `O(1)`

Only two counter variables are used.

## Pattern Learned

### Counter Pattern

Whenever a problem asks:

> "How many elements satisfy a condition?"

Think about a counter:

```python
count = 0

for item in items:
    if condition:
        count += 1
```

This pattern is one of the fundamental building blocks for more advanced frequency and counting problems.
