# Phase 10 — Functional Programming
# Practice Problems

---

# Beginner Level

## 1. Square Numbers Using map()

Create a list:

```python
numbers = [1, 2, 3, 4, 5]
```

Use `map()` to generate square values.

---

## 2. Convert Strings to Integers

Input:

```python
numbers = ["10", "20", "30", "40"]
```

Convert all strings into integers using `map()`.

---

## 3. Convert Celsius to Fahrenheit

Input:

```python
temperatures = [0, 20, 35, 100]
```

Convert all temperatures to Fahrenheit using `map()`.

---

## 4. Convert Names to Uppercase

Input:

```python
names = ["python", "java", "go", "rust"]
```

Convert all names to uppercase.

---

## 5. Add GST

Input:

```python
prices = [100, 250, 500, 800]
```

Add 18% GST using `map()`.

---

# filter() Practice

## 6. Find Even Numbers

Filter even numbers from:

```python
numbers = [1,2,3,4,5,6,7,8]
```

---

## 7. Find Odd Numbers

Filter odd numbers.

---

## 8. Students Passed

Input:

```python
marks = [45,78,90,35,66,22]
```

Return marks greater than or equal to 50.

---

## 9. Remove Empty Strings

Input:

```python
["Python","","AI","","ML"]
```

Remove empty strings.

---

## 10. Filter High Salary Employees

Input:

```python
employees = [
    {"name":"John","salary":45000},
    {"name":"Alice","salary":75000},
    {"name":"David","salary":60000}
]
```

Filter employees whose salary is greater than 50000.

---

# reduce() Practice

## 11. Find Sum

Find the sum of:

```python
[5,10,15,20]
```

using `reduce()`.

---

## 12. Find Product

Multiply all numbers.

---

## 13. Find Maximum

Find the largest value using `reduce()`.

---

## 14. Find Minimum

Find the smallest value using `reduce()`.

---

## 15. Join Words

Input:

```python
["Python","is","awesome"]
```

Join all words into one sentence.

---

# zip() Practice

## 16. Combine Two Lists

Input:

```python
names = ["John","Alice","Sara"]
marks = [85,92,88]
```

Combine using `zip()`.

---

## 17. Create Dictionary

Create a dictionary from:

```python
keys = ["name","age","city"]

values = ["Kalid",28,"Bangalore"]
```

---

## 18. Zip Three Lists

Combine:

- Name
- Age
- Department

---

## 19. Unzip Data

Input:

```python
students = [
    ("John",85),
    ("Alice",90)
]
```

Separate names and marks.

---

## 20. Employee Report

Create employee records using `zip()`.

---

# enumerate() Practice

## 21. Print Index and Value

Use `enumerate()` on:

```python
["Python","AI","ML"]
```

---

## 22. Start Index from 100

Print values starting from index 100.

---

## 23. Student Ranking

Display:

```text
Rank 1
Rank 2
Rank 3
```

using `enumerate()`.

---

## 24. Enumerate String

Print each character with its index.

---

## 25. Menu System

Display:

```text
1. Home
2. About
3. Contact
```

using `enumerate()`.

---

# any() Practice

## 26. Check Positive Numbers

Determine whether at least one positive number exists.

---

## 27. Check Admin User

Input:

```python
users = [
    {"admin":False},
    {"admin":True}
]
```

Use `any()`.

---

## 28. Check Passed Student

Determine if any student scored above 50.

---

## 29. Check Valid Email

Check if any employee has an email address.

---

## 30. Detect Error Logs

Input:

```python
logs = [
    "INFO",
    "ERROR",
    "WARNING"
]
```

Check whether any error exists.

---

# all() Practice

## 31. Check All Positive

Verify whether all numbers are positive.

---

## 32. Student Eligibility

Check if all students scored at least 50.

---

## 33. Employee Details

Check whether every employee has:

- Name
- Email
- Phone

---

## 34. Attendance Validation

Verify whether every student has attendance greater than or equal to 75%.

---

## 35. Password Validation

Check whether all passwords satisfy the minimum length requirement.

---

# sorted() Practice

## 36. Sort Numbers

Sort numbers in ascending order.

---

## 37. Reverse Sort

Sort numbers in descending order.

---

## 38. Sort Strings

Sort a list of programming languages alphabetically.

---

## 39. Sort Students by Marks

Input:

```python
students = [
    {"name":"John","marks":82},
    {"name":"Alice","marks":95}
]
```

Sort by marks.

---

## 40. Sort Employees by Salary

Sort employees in descending order of salary.

---

# Key Function Practice

## 41. Sort by String Length

Sort:

```python
["AI","Python","MachineLearning"]
```

using `key=len`.

---

## 42. Find Longest Word

Use:

```python
max()
```

with `key=len`.

---

## 43. Find Shortest Word

Use:

```python
min()
```

with `key=len`.

---

## 44. Sort by Age

Sort employee dictionaries using age.

---

## 45. Sort Products by Price

Sort products in ascending order using `key`.

---

# Higher-Order Function Practice

## 46. Build Calculator

Pass:

- add
- subtract
- multiply
- divide

as function arguments.

---

## 47. Discount Calculator

Create:

```python
process_prices(function, prices)
```

Pass different discount functions.

---

## 48. Greeting Generator

Return different greeting functions.

Example:

```python
english()

tamil()

hindi()
```

---

## 49. Callback Example

Create:

```python
download(callback)
```

Print:

```
Download Complete
```

after download finishes.

---

## 50. Function Factory

Create:

```python
multiplier(2)

multiplier(5)

multiplier(10)
```

Each returned function should multiply by its own factor.

---

# Real-World Problems

## 51. Employee Salary Processing

- Increase salary by 10%
- Filter salaries above ₹60,000
- Sort highest salary first

---

## 52. Student Result System

- Filter passed students
- Sort by marks
- Assign ranks
- Calculate total marks

---

## 53. Shopping Cart

- Add GST
- Apply discount
- Calculate final bill
- Sort products by price

---

## 54. API Response Processing

Convert API data into a clean format using:

- `map()`
- `filter()`
- `sorted()`

---

## 55. Log Analyzer

- Filter ERROR logs
- Count ERROR messages
- Sort by timestamp

---

## 56. CSV Data Processing

- Read records
- Filter invalid rows
- Convert values
- Generate summary

---

## 57. AI Dataset Cleaning

- Remove empty records
- Convert text to lowercase
- Remove duplicates
- Sort by label

---

## 58. RAG Document Pipeline

Create a processing pipeline:

```text
Documents
      │
      ▼
Filter Empty Documents
      │
      ▼
Convert to Lowercase
      │
      ▼
Sort by Length
      │
      ▼
Generate Document IDs
```

---

## 59. Employee Performance Report

Generate a report containing:

- Rank
- Name
- Department
- Salary
- Performance Grade

using functional programming techniques.

---

## 60. End-to-End Functional Data Pipeline

Create a pipeline that:

```text
Raw Data
      │
      ▼
Filter Invalid Records
      │
      ▼
Transform Data
      │
      ▼
Sort Results
      │
      ▼
Aggregate Statistics
      │
      ▼
Final Report
```

Use `filter()`, `map()`, `sorted()`, `reduce()`, and `enumerate()` together.

---

# Mini Projects

## 1. Student Management System

Features:

- Add students
- Filter passed students
- Rank students
- Calculate class average

---

## 2. Employee Payroll System

Features:

- Salary calculation
- Bonus calculation
- Tax deduction
- Salary ranking

---

## 3. E-Commerce Order Processor

Features:

- GST calculation
- Discount processing
- Order filtering
- Sales summary

---

## 4. AI Dataset Preprocessor

Features:

- Data cleaning
- Data transformation
- Duplicate removal
- Dataset validation

---

## 5. RAG Document Processing Pipeline

Features:

- Filter documents
- Normalize text
- Assign IDs
- Sort by size
- Prepare for embedding generation

---

# Learning Outcome

After completing these practice problems, you should be able to:

- Apply `map()`, `filter()`, `reduce()`, `zip()`, `enumerate()`, `any()`, `all()`, and `sorted()` confidently.
- Use `key` functions for custom sorting.
- Create higher-order functions and callbacks.
- Build clean, reusable functional pipelines.
- Solve real-world backend, data engineering, and AI/GenAI data processing problems using functional programming principles.