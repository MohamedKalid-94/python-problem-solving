# Phase 1 - Step 4: Decision Making Interview Questions & Answers

## Overview

This document contains commonly asked Python interview questions on decision making, from beginner to intermediate level.

Topics Covered:

- if
- if else
- if elif else
- Nested if
- Multiple Conditions
- Guard Clauses
- Decision Patterns

---

# Beginner Level

## 1. What is decision making in Python?

### Answer

Decision making allows a program to execute different blocks of code based on a condition.

Python uses conditional statements to make decisions.

Example:

```python
age = 20

if age >= 18:
    print("Eligible")
```

---

## 2. What is a condition?

### Answer

A condition is an expression that evaluates to either:

```
True

or

False
```

Example:

```python
10 > 5
```

Result:

```
True
```

---

## 3. What is an if statement?

### Answer

The `if` statement executes a block of code only when the condition is True.

Syntax:

```python
if condition:
    statement
```

---

## 4. When should we use an if statement?

### Answer

Use an `if` statement when only one action needs to be performed if the condition is True.

Examples:

- Positive number
- Login status
- Temperature warning

---

## 5. What is an if else statement?

### Answer

The `if else` statement provides two possible outcomes.

Example:

```python
if marks >= 50:
    print("Pass")
else:
    print("Fail")
```

---

## 6. When should we use if else?

### Answer

Use `if else` when there are exactly two possible outcomes.

Examples:

- Pass or Fail
- Even or Odd
- Eligible or Not Eligible

---

## 7. What is an if elif else statement?

### Answer

It is used when multiple conditions need to be checked.

Example:

```python
if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

else:
    print("Grade C")
```

---

## 8. How many else blocks can an if statement have?

### Answer

Only one `else` block is allowed for an `if` statement.

---

## 9. How many elif blocks can we use?

### Answer

There is no fixed limit.

You can use as many `elif` blocks as required.

---

## 10. What happens if no condition is True and there is no else block?

### Answer

The program skips all the conditional blocks and continues executing the next statement.

---

# Nested if

## 11. What is a nested if statement?

### Answer

A nested `if` is an `if` statement inside another `if` statement.

Example:

```python
if username == "admin":

    if password == "admin123":
        print("Login Successful")
```

---

## 12. When should nested if be used?

### Answer

Use nested `if` when one condition depends on another condition.

Examples:

- Login systems
- Bank withdrawal
- Admission process

---

## 13. Can we write multiple nested if statements?

### Answer

Yes.

However, too many nested `if` statements reduce readability.

---

# Multiple Conditions

## 14. How do we combine multiple conditions?

### Answer

Using logical operators:

- `and`
- `or`
- `not`

Example:

```python
if age >= 18 and citizen:
    print("Eligible")
```

---

## 15. What does the and operator do?

### Answer

The `and` operator returns True only if all conditions are True.

Example:

```python
True and True
```

Output:

```
True
```

---

## 16. What does the or operator do?

### Answer

The `or` operator returns True if at least one condition is True.

Example:

```python
True or False
```

Output:

```
True
```

---

## 17. What does the not operator do?

### Answer

The `not` operator reverses the Boolean value.

Example:

```python
not True
```

Output:

```
False
```

---

## 18. Can we combine and and or together?

### Answer

Yes.

Example:

```python
if age >= 18 and (citizen or permanent_resident):
    print("Eligible")
```

---

# Guard Clauses

## 19. What is a guard clause?

### Answer

A guard clause checks invalid conditions first and exits early, reducing unnecessary nesting.

Example:

```python
if age < 18:
    print("Not Eligible")
else:
    print("Eligible")
```

---

## 20. Why are guard clauses useful?

### Answer

Benefits:

- Cleaner code
- Less nesting
- Better readability
- Easier maintenance

---

# Decision Patterns

## 21. What is validation?

### Answer

Validation checks whether input data is correct before processing it.

Examples:

- Username validation
- Password validation
- Age validation

---

## 22. What is range checking?

### Answer

Range checking verifies whether a value falls within a specified range.

Example:

```python
if marks >= 90:
```

---

## 23. What is category selection?

### Answer

Category selection chooses one option from multiple categories.

Examples:

- Premium
- Gold
- Regular

---

## 24. What is a decision tree?

### Answer

A decision tree is a sequence of connected decisions where each choice leads to another decision.

Examples:

- Loan approval
- Login system
- Insurance approval

---

# Comparison Questions

## 25. Difference between if and if else?

### Answer

| if | if else |
|----|----------|
| One-way decision | Two-way decision |
| Executes only when condition is True | Executes one of two blocks |

---

## 26. Difference between if else and if elif else?

### Answer

| if else | if elif else |
|----------|---------------|
| Two outcomes | Multiple outcomes |

---

## 27. Difference between nested if and multiple conditions?

### Answer

Nested `if`

```python
if condition1:

    if condition2:
        print("Success")
```

Multiple conditions

```python
if condition1 and condition2:
    print("Success")
```

Nested `if` is used when one decision depends on another.

Multiple conditions are used when all conditions can be checked together.

---

## 28. Which is better: nested if or multiple conditions?

### Answer

Use multiple conditions whenever possible because they are simpler and easier to read.

Use nested `if` only when decisions depend on previous conditions.

---

# Common Mistakes

## 29. What happens if the colon (:) is missing?

### Answer

Python raises a `SyntaxError`.

Incorrect:

```python
if age >= 18
```

Correct:

```python
if age >= 18:
```

---

## 30. Why is indentation important in Python?

### Answer

Python uses indentation to define code blocks.

Incorrect indentation results in an `IndentationError`.

---

## 31. Can we use assignment (=) inside an if condition?

### Answer

No.

Incorrect:

```python
if age = 18:
```

Correct:

```python
if age == 18:
```

---

# Scenario-Based Questions

## 32. How would you check voting eligibility?

### Answer

Conditions:

- Age ≥ 18
- Citizen = True

---

## 33. How would you design a login system?

### Answer

Steps:

1. Validate username.
2. Validate password.
3. Grant or deny access.

---

## 34. How would you validate a file upload?

### Answer

Checks:

- File exists
- Correct file type
- File size within limit

---

## 35. How would you calculate student grades?

### Answer

Use an `if elif else` statement with different mark ranges.

---

## 36. How would you approve a bank withdrawal?

### Answer

Check:

- Account is active
- Balance is sufficient
- Withdrawal amount is valid

---

## 37. How would you approve a job application?

### Answer

Check:

- Experience
- Required skills
- Qualification

---

## 38. How would you implement a discount system?

### Answer

Check:

- Purchase amount
- Membership type
- Offer availability

---

# Best Practices

## 39. What are the best practices for writing conditional statements?

### Answer

- Keep conditions simple.
- Use meaningful variable names.
- Avoid deep nesting.
- Use `elif` instead of multiple `if` statements when appropriate.
- Validate input before processing.
- Use guard clauses to simplify code.

---

## 40. Why is decision making important in programming?

### Answer

Decision making enables programs to:

- Make choices
- Validate data
- Handle different situations
- Solve real-world problems
- Build interactive applications

Without decision making, programs would execute every statement in sequence without responding to different inputs or conditions.

---

# Quick Revision Table

| Topic | Key Point |
|--------|-----------|
| if | One-way decision |
| if else | Two-way decision |
| if elif else | Multiple choices |
| Nested if | Decision inside another decision |
| Multiple Conditions | Use `and`, `or`, `not` |
| Guard Clauses | Handle invalid cases early |
| Validation | Check input correctness |
| Range Checking | Verify value ranges |
| Category Selection | Choose one category |
| Decision Tree | Series of connected decisions |

---

# Interview Checklist

- [ ] Understand Boolean conditions
- [ ] Know when to use `if`
- [ ] Know when to use `if else`
- [ ] Know when to use `if elif else`
- [ ] Understand nested `if`
- [ ] Use logical operators correctly
- [ ] Explain guard clauses
- [ ] Explain validation patterns
- [ ] Explain range checking
- [ ] Solve basic decision-making problems