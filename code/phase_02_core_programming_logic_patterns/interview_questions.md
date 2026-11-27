# Programming Patterns - Interview Questions & Answers

# Beginner Level

## 1. What is a programming pattern?

A programming pattern is a reusable approach for solving a common type of problem.

Instead of memorizing solutions, programmers learn patterns that can solve many problems efficiently.

Example:

- Counting items
- Finding maximum values
- Searching
- Filtering
- Grouping
- Simulation

---

## 2. Why are programming patterns important?

Programming patterns help developers:

- Write efficient code
- Solve interview questions faster
- Reduce duplicate logic
- Improve readability
- Build scalable solutions

---

## 3. What are the most common programming patterns?

- Counter Pattern
- Accumulator Pattern
- Max/Min Pattern
- Search Pattern
- Filter Pattern
- Transform Pattern
- Frequency Map Pattern
- Grouping Pattern
- Two Pointer Pattern
- Sliding Window Pattern
- Prefix Sum Pattern
- Hash Map Pattern
- Nested Loop Pattern
- State Tracking Pattern
- Simulation Pattern

---

## 4. What is the Counter Pattern?

Counter Pattern counts how many items satisfy a condition.

Example:

```python
count = 0

for number in numbers:
    if number > 0:
        count += 1
```

---

## 5. Where is Counter Pattern used?

Examples:

- Count vowels
- Count words
- Count positive numbers
- Count students
- Count login attempts

---

## 6. What is the Accumulator Pattern?

Accumulator Pattern stores a running result.

Example:

```python
total = 0

for number in numbers:
    total += number
```

---

## 7. Applications of Accumulator Pattern

- Sum
- Product
- Running total
- Average
- Total sales

---

## 8. Difference between Counter and Accumulator?

Counter:

Counts occurrences.

Example:

```python
count += 1
```

Accumulator:

Stores calculated values.

Example:

```python
total += number
```

---

## 9. What is Max/Min Pattern?

Used to find largest or smallest value.

Example:

```python
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number
```

---

## 10. Applications of Max/Min Pattern

- Highest salary
- Lowest temperature
- Longest word
- Maximum score

---

# Search Pattern

## 11. What is Search Pattern?

Search Pattern checks whether an element exists.

Example:

```python
for number in numbers:
    if number == target:
        print("Found")
```

---

## 12. Difference between Linear Search and Binary Search?

Linear Search

- O(n)
- Works on any list

Binary Search

- O(log n)
- Requires sorted data

---

## 13. What is Linear Search?

Checks every element one by one.

---

## 14. What is the time complexity of Linear Search?

```
O(n)
```

---

## 15. What is the space complexity?

```
O(1)
```

---

# Filter Pattern

## 16. What is Filter Pattern?

Creates a new collection containing only elements that satisfy a condition.

Example:

```python
positive = []

for number in numbers:
    if number > 0:
        positive.append(number)
```

---

## 17. Applications of Filter Pattern

- Positive numbers
- Even numbers
- Valid records
- Adult users
- Paid customers

---

# Transform Pattern

## 18. What is Transform Pattern?

Transforms every item into another value.

Example:

```python
square = []

for number in numbers:
    square.append(number ** 2)
```

---

## 19. Applications

- Currency conversion
- Temperature conversion
- Uppercase conversion
- Image processing
- Feature engineering

---

# Frequency Map Pattern

## 20. What is Frequency Map Pattern?

Counts occurrences using a dictionary.

Example:

```python
frequency = {}

for item in items:
    frequency[item] = frequency.get(item,0)+1
```

---

## 21. Applications

- Character frequency
- Word frequency
- Duplicate detection
- Histograms
- Voting systems

---

## 22. Why use Dictionary instead of List?

Dictionary lookup is much faster.

Average complexity:

```
O(1)
```

---

# Grouping Pattern

## 23. What is Grouping Pattern?

Groups similar data together.

Example:

```python
employees = {

"HR":[...],

"IT":[...]

}
```

---

## 24. Applications

- Students by grade
- Employees by department
- Products by category
- Orders by date

---

# Two Pointer Pattern

## 25. What is Two Pointer Pattern?

Uses two indices moving through a collection.

Example:

```python
left = 0

right = len(array)-1
```

---

## 26. Applications

- Palindrome
- Pair Sum
- Reverse Array
- Merge Arrays
- Remove Duplicates

---

## 27. Advantages

- Faster
- Less memory
- Often O(n)

---

# Sliding Window Pattern

## 28. What is Sliding Window?

Processes a fixed-size or variable-size window.

Example:

Instead of recalculating the whole subarray, update only the changed elements.

---

## 29. Applications

- Maximum subarray
- Minimum subarray
- Longest substring
- Moving average

---

## 30. Complexity

Usually

```
O(n)
```

instead of

```
O(n²)
```

---

# Prefix Sum Pattern

## 31. What is Prefix Sum?

Stores cumulative sums.

Example:

```
prefix[i]

=

sum of first i elements
```

---

## 32. Applications

- Range Sum
- Cumulative Reports
- Financial Analysis
- Query Processing

---

## 33. Complexity

Building Prefix

```
O(n)
```

Each Query

```
O(1)
```

---

# Hash Map Thinking

## 34. What is Hash Map Thinking?

Solve problems using dictionaries for fast lookup.

---

## 35. Applications

- Duplicate detection
- Fast lookup
- Cache
- Frequency counting
- Index mapping

---

## 36. Complexity

Average lookup

```
O(1)
```

---

# Nested Loop Pattern

## 37. When do we use Nested Loops?

When processing:

- Matrix
- Grid
- Table
- Pair comparisons

---

## 38. Time Complexity

Typical:

```
O(n²)
```

---

## 39. Examples

- Matrix multiplication
- Pattern printing
- Chess board traversal

---

# State Tracking Pattern

## 40. What is State Tracking?

Remember previous information while processing data.

Example:

```python
previous = current
```

---

## 41. Applications

- Sensor monitoring
- Traffic lights
- Event detection
- Stock prices

---

# Simulation Pattern

## 42. What is Simulation?

Simulates a real-world system step by step.

---

## 43. Applications

- ATM
- Banking
- Games
- Robotics
- Inventory

---

# Coding Interview Questions

## 44. Remove duplicates from a list.

Expected Pattern:

Hash Map or Set

---

## 45. Find the most frequent element.

Expected Pattern:

Frequency Map

---

## 46. Find the largest element.

Expected Pattern:

Max Pattern

---

## 47. Count vowels in a sentence.

Expected Pattern:

Counter Pattern

---

## 48. Calculate average.

Expected Pattern:

Accumulator Pattern

---

## 49. Find first occurrence.

Expected Pattern:

Search Pattern

---

## 50. Reverse an array.

Expected Pattern:

Two Pointer Pattern

---

## 51. Find maximum subarray of size K.

Expected Pattern:

Sliding Window

---

## 52. Answer multiple range sum queries.

Expected Pattern:

Prefix Sum

---

## 53. Group employees by department.

Expected Pattern:

Grouping Pattern

---

## 54. Detect duplicate values.

Expected Pattern:

Hash Map

---

## 55. Compare every pair of elements.

Expected Pattern:

Nested Loop

---

## 56. Track status changes.

Expected Pattern:

State Tracking

---

## 57. Simulate an ATM system.

Expected Pattern:

Simulation Pattern

---

# Scenario-Based Questions

## 58. Which pattern would you use to count login attempts?

Counter Pattern

---

## 59. Which pattern would you use to calculate total revenue?

Accumulator Pattern

---

## 60. Which pattern would you use to find the highest-paid employee?

Max Pattern

---

## 61. Which pattern would you use to search a username?

Search Pattern

---

## 62. Which pattern would you use to filter active users?

Filter Pattern

---

## 63. Which pattern would you use to convert Celsius to Fahrenheit for every value?

Transform Pattern

---

## 64. Which pattern would you use to count word occurrences?

Frequency Map

---

## 65. Which pattern would you use to group orders by customer?

Grouping Pattern

---

## 66. Which pattern would you use to check whether a string is a palindrome?

Two Pointer

---

## 67. Which pattern would you use to find the maximum sum of a fixed-size subarray?

Sliding Window

---

## 68. Which pattern would you use for answering thousands of range sum queries?

Prefix Sum

---

## 69. Which pattern would you use for duplicate detection?

Hash Map

---

## 70. Which pattern would you use for matrix traversal?

Nested Loop

---

## 71. Which pattern would you use to detect sensor value changes?

State Tracking

---

## 72. Which pattern would you use to model a banking application?

Simulation Pattern

---

# Complexity Summary

| Pattern | Time Complexity | Typical Use |
|----------|----------------:|-------------|
| Counter | O(n) | Counting |
| Accumulator | O(n) | Sum/Product |
| Max/Min | O(n) | Largest/Smallest |
| Search | O(n) | Finding Elements |
| Filter | O(n) | Extract Values |
| Transform | O(n) | Data Conversion |
| Frequency Map | O(n) | Counting Occurrences |
| Grouping | O(n) | Categorization |
| Two Pointer | O(n) | Sorted Arrays, Palindromes |
| Sliding Window | O(n) | Subarrays |
| Prefix Sum | O(n) Build / O(1) Query | Range Queries |
| Hash Map | O(1) Average Lookup | Fast Access |
| Nested Loop | O(n²) | Matrix & Pair Problems |
| State Tracking | O(n) | Change Detection |
| Simulation | Depends on Input | Real-world Modeling |

---

# Interview Tips

- Identify the problem pattern before coding.
- Optimize brute-force solutions using appropriate patterns.
- Explain your time and space complexity.
- Use meaningful variable names.
- Handle edge cases such as empty inputs and single-element collections.
- Practice recognizing patterns across different problem statements instead of memorizing solutions.

---

# Final Takeaway

Programming patterns are reusable problem-solving techniques. Mastering these patterns enables you to solve a wide variety of coding interview questions efficiently and write clean, maintainable, and optimized code.