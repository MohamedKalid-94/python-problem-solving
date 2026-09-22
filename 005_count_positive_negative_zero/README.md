# Problem 5 — Count Positive, Negative, and Zero

## Problem

Given a list of integers, count how many numbers are:

* Positive
* Negative
* Zero

The solution should use a `for` loop without using `count()`, list comprehensions, or external libraries.

## Input

```python id="b7q3kw"
numbers = [12, -5, 0, 8, -3, 0, 15, -10]
```

## Expected Output

```text id="xq0x4w"
Positive Numbers = 3
Negative Numbers = 3
Zeros = 2
```

## Approach

We maintain three counters:

```text id="az3t4n"
count_positive → number of positive values
count_negative → number of negative values
count_zero     → number of zero values
```

### Steps

1. Initialize all three counters to `0`.
2. Loop through each number in the list.
3. If the number is greater than `0`, increment the positive counter.
4. Else if the number is less than `0`, increment the negative counter.
5. Otherwise, the number is `0`, so increment the zero counter.
6. Print the final counts.

## Python Implementation

See the complete implementation in [`solution.py`](solution.py).

```python id="3u7lpi"
numbers = [12, -5, 0, 8, -3, 0, 15, -10]

count_positive = 0
count_negative = 0
count_zero = 0

for number in numbers:

    if number > 0:
        count_positive += 1

    elif number < 0:
        count_negative += 1

    else:
        count_zero += 1

print("Positive Numbers =", count_positive)
print("Negative Numbers =", count_negative)
print("Zeros =", count_zero)
```

## How
