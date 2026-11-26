# Programming Patterns - Complete Notes

# Introduction

Programming patterns are reusable problem-solving techniques that help solve common programming problems efficiently.

Instead of memorizing individual solutions, developers learn patterns that can be applied to many different problems.

Programming patterns are heavily used in:

- Software Development
- Coding Interviews
- Competitive Programming
- Data Processing
- Artificial Intelligence
- Machine Learning
- Backend Development

---

# Why Learn Programming Patterns?

Programming patterns help you:

- Write clean code
- Reduce code duplication
- Improve problem-solving skills
- Optimize algorithms
- Crack coding interviews
- Build scalable applications

---

# 1. Counter Pattern

## Definition

The Counter Pattern counts how many items satisfy a condition.

## Workflow

```
Start Counter

↓

Traverse Collection

↓

Condition True?

↓

Increase Counter

↓

Continue

↓

Display Count
```

## Example

```python
count = 0

for number in numbers:
    if number > 0:
        count += 1
```

## Applications

- Count vowels
- Count words
- Count positive numbers
- Count failed students
- Count login attempts

## Complexity

Time

```
O(n)
```

Space

```
O(1)
```

---

# 2. Accumulator Pattern

## Definition

The Accumulator Pattern stores a running result while processing data.

## Example

```python
total = 0

for number in numbers:
    total += number
```

## Applications

- Sum
- Product
- Average
- Running balance
- Total sales

## Complexity

Time

```
O(n)
```

Space

```
O(1)
```

---

# 3. Max / Min Pattern

## Definition

Find the largest or smallest value by comparing elements one by one.

## Example

```python
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
```

## Applications

- Highest salary
- Lowest temperature
- Longest word
- Highest score

## Complexity

Time

```
O(n)
```

---

# 4. Search Pattern

## Definition

Search for an element in a collection.

## Linear Search

Checks every element until the target is found.

## Example

```python
for item in items:
    if item == target:
        print("Found")
```

## Applications

- Search employee
- Search product
- Search username
- Search book

## Complexity

Time

```
O(n)
```

---

# 5. Filter Pattern

## Definition

Creates a new collection containing only the elements that satisfy a condition.

## Example

```python
positive = []

for number in numbers:
    if number > 0:
        positive.append(number)
```

## Applications

- Positive numbers
- Even numbers
- Active users
- Valid emails
- Passed students

## Complexity

Time

```
O(n)
```

---

# 6. Transform Pattern

## Definition

Converts every item into another value.

## Example

```python
squares = []

for number in numbers:
    squares.append(number ** 2)
```

## Applications

- Currency conversion
- Unit conversion
- Uppercase strings
- Feature engineering

## Complexity

Time

```
O(n)
```

---

# 7. Frequency Map Pattern

## Definition

Uses a dictionary to count occurrences efficiently.

## Example

```python
frequency = {}

for item in items:
    frequency[item] = frequency.get(item, 0) + 1
```

## Applications

- Character frequency
- Word frequency
- Duplicate detection
- Vote counting
- Histograms

## Complexity

Time

```
O(n)
```

Dictionary lookup

```
O(1)
```

---

# 8. Grouping Pattern

## Definition

Groups similar items together using a dictionary.

## Example

```python
groups = {}

for student, grade in students:
    groups.setdefault(grade, []).append(student)
```

## Applications

- Students by grade
- Employees by department
- Products by category
- Orders by customer

## Complexity

Time

```
O(n)
```

---

# 9. Two Pointer Pattern

## Definition

Uses two pointers moving through a collection.

Usually:

```
Left →

← Right
```

## Example

```python
left = 0
right = len(array) - 1
```

## Applications

- Palindrome
- Reverse array
- Pair sum
- Merge arrays
- Remove duplicates

## Advantages

- Faster
- Less memory
- Cleaner logic

## Complexity

Time

```
O(n)
```

---

# 10. Sliding Window Pattern

## Definition

Processes a subset (window) of data while moving across the collection.

Instead of recalculating everything, update only the changed elements.

## Example

```
Window Size = 3

[2 1 5]

↓

[1 5 1]

↓

[5 1 3]
```

## Applications

- Maximum sum subarray
- Longest substring
- Moving average
- Streaming data

## Complexity

Time

```
O(n)
```

instead of

```
O(n × k)
```

---

# 11. Prefix Sum Pattern

## Definition

Stores cumulative sums for answering range queries efficiently.

## Example

Original

```
2 4 6 8
```

Prefix

```
2 6 12 20
```

## Formula

```
Range Sum

=

prefix[right]

-

prefix[left-1]
```

## Applications

- Range Sum
- Cumulative Reports
- Query Optimization

## Complexity

Building

```
O(n)
```

Query

```
O(1)
```

---

# 12. Hash Map Thinking

## Definition

Use dictionaries for fast lookup and indexing.

## Example

```python
students = {
    101: "Alice"
}
```

## Applications

- Cache
- Fast lookup
- Duplicate detection
- Frequency counting
- Index mapping

## Complexity

Average lookup

```
O(1)
```

---

# 13. Nested Loop Thinking

## Definition

Use one loop inside another to process multiple dimensions or compare combinations.

## Example

```python
for row in matrix:
    for value in row:
        print(value)
```

## Applications

- Matrix
- Grid
- Chess board
- Pattern printing
- Pair comparison

## Complexity

```
O(n²)
```

---

# 14. State Tracking Pattern

## Definition

Keep track of previous values or status while processing current data.

## Example

```python
previous = values[0]

for current in values[1:]:
    if current != previous:
        print("Changed")
    previous = current
```

## Applications

- Sensor monitoring
- Traffic lights
- Login/logout tracking
- Event detection
- Stock price changes

## Complexity

```
O(n)
```

---

# 15. Simulation Pattern

## Definition

Represents the behavior of a real-world system by updating its state step by step.

## Example

```python
balance = 1000

balance += 500
balance -= 200
```

## Applications

- ATM
- Banking
- Robotics
- Games
- Inventory
- Traffic systems

---

# Pattern Selection Guide

| Problem Type | Best Pattern |
|--------------|--------------|
| Count items | Counter |
| Calculate total | Accumulator |
| Find largest/smallest | Max / Min |
| Find an element | Search |
| Extract matching items | Filter |
| Convert values | Transform |
| Count occurrences | Frequency Map |
| Categorize data | Grouping |
| Compare from both ends | Two Pointer |
| Fixed/variable-size subarray | Sliding Window |
| Fast range queries | Prefix Sum |
| Fast key lookup | Hash Map |
| Matrix or grid traversal | Nested Loop |
| Detect changes over time | State Tracking |
| Model real-world processes | Simulation |

---

# Time Complexity Summary

| Pattern | Time Complexity | Space Complexity |
|----------|----------------:|-----------------:|
| Counter | O(n) | O(1) |
| Accumulator | O(n) | O(1) |
| Max / Min | O(n) | O(1) |
| Search | O(n) | O(1) |
| Filter | O(n) | O(n) |
| Transform | O(n) | O(n) |
| Frequency Map | O(n) | O(n) |
| Grouping | O(n) | O(n) |
| Two Pointer | O(n) | O(1) |
| Sliding Window | O(n) | O(1) |
| Prefix Sum | O(n) Build, O(1) Query | O(n) |
| Hash Map | O(1) Average Lookup | O(n) |
| Nested Loop | O(n²) | O(1) |
| State Tracking | O(n) | O(1) |
| Simulation | Depends on Input | Depends on State |

---

# Common Interview Questions

- Count vowels in a string.
- Find the largest element in a list.
- Search for a target value.
- Remove duplicates from a list.
- Count character frequencies.
- Group employees by department.
- Check if a string is a palindrome.
- Find the maximum sum subarray.
- Answer range sum queries efficiently.
- Detect duplicate values using a hash map.
- Traverse a matrix.
- Track status changes in a sequence.
- Simulate an ATM or banking system.

---

# Best Practices

- Identify the problem pattern before coding.
- Choose the simplest pattern that solves the problem.
- Analyze time and space complexity.
- Handle edge cases such as empty collections.
- Write readable code with meaningful variable names.
- Optimize only after achieving a correct solution.
- Practice recognizing patterns instead of memorizing code.

---

# Key Takeaways

- Programming patterns are reusable solutions to common problems.
- The same pattern can solve many different interview questions.
- Understanding patterns improves coding speed, code quality, and problem-solving ability.
- Mastering these 15 patterns provides a strong foundation for data structures, algorithms, software engineering, and AI development.