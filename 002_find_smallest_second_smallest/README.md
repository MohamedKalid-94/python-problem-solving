# Problem 002 — Find the Smallest and Second Smallest Numbers

## Problem

Given a list of numbers, find the smallest and second-smallest numbers without using:

* `min()`
* `sorted()`

## Example

### Input

```python
numbers = [12, 45, 7, 8, 23, 56]
```

### Output

```text
Smallest Number: 7
Second Smallest Number: 8
```

## Approach

Maintain two variables:

```text
smallest
second_smallest
```

### Step 1 — Initialize using the first two numbers

Compare the first two numbers.

If:

```text
first < second
```

then:

```text
smallest = first
second_smallest = second
```

Otherwise:

```text
smallest = second
second_smallest = first
```

### Step 2 — Process the remaining numbers

Start from index `2`:

```python
numbers[2:]
```

For every remaining number:

### Case 1 — New smallest

If:

```text
number < smallest
```

then the old smallest becomes the second smallest.

```text
second_smallest = smallest
smallest = number
```

### Case 2 — New second smallest

Otherwise, if:

```text
number < second_smallest
```

then:

```text
second_smallest = number
```

## Pseudocode

```text
if first < second:
    smallest = first
    second_smallest = second
else:
    smallest = second
    second_smallest = first

for each number starting from index 2:

    if number < smallest:
        second_smallest = smallest
        smallest = number

    else if number < second_smallest:
        second_smallest = number

print smallest
print second_smallest
```

## Python Implementation

```python
numbers = [12, 45, 7, 8, 23, 56]

if numbers[0] < numbers[1]:
    smallest = numbers[0]
    second_smallest = numbers[1]
else:
    smallest = numbers[1]
    second_smallest = numbers[0]

for number in numbers[2:]:
    if number < smallest:
        second_smallest = smallest
        smallest = number
    elif number < second_smallest:
        second_smallest = number

print("Smallest Number:", smallest)
print("Second Smallest Number:", second_smallest)
```

## Complexity

* Time Complexity: **O(n)**
* Extra Space Complexity: **O(1)**

## Important Edge Cases

The algorithm requires at least **2 elements**.

### Empty list

```python
[]
```

Cannot find the smallest or second smallest.

### One element

```python
[10]
```

Smallest exists, but a second smallest does not exist.

### Two elements

```python
[20, 10]
```

Result:

```text
Smallest Number: 10
Second Smallest Number: 20
```

### Duplicate values

```python
[10, 10]
```

This requires a definition:

* If duplicates are allowed as the second smallest → `10, 10`
* If "second smallest" means **second distinct smallest** → there is no second smallest.

## Key Pattern Learned

### Maintain Top 2 / Bottom 2

Instead of storing every number and sorting the list, maintain only the two values that matter:

```text
smallest
second_smallest
```

This is an important algorithmic pattern.

## Main Lesson

The difficult part was not the `for` loop.

The important reasoning was:

> When a new smallest number appears, what happens to the old smallest?

Answer:

```text
old smallest → second smallest
new number   → smallest
```

This idea generalizes to many "top two" or "bottom two" problems.
