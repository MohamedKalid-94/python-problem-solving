# Phase 1 - Step 4: Decision Making Notes

## Overview

Decision making allows a program to execute different blocks of code based on conditions.

In Python, decision making is performed using conditional statements.

These statements help programs:

- Make decisions
- Validate input
- Choose between multiple options
- Control program flow
- Handle different real-world scenarios

Examples:

- Login systems
- ATM withdrawal
- Student grading
- Online shopping discounts
- Ticket booking
- Banking applications

---

# What is a Condition?

A condition is an expression that evaluates to either:

```
True

or

False
```

Example:

```python
age = 20

age >= 18
```

Result:

```
True
```

---

# Decision Making Flow

```
Condition

      │

      ▼

True --------► Execute Code

False -------► Skip or Execute Another Block
```

---

# 1. Simple if Statement

The `if` statement executes a block of code only when the condition is True.

Syntax:

```python
if condition:
    statement
```

Example:

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

Output:

```
Eligible to vote
```

If the condition is False, nothing inside the `if` block executes.

Example:

```python
temperature = 38

if temperature > 35:
    print("High Temperature")
```

---

## When to Use

Use a simple `if` when only one action is required.

Examples:

- Check positive number
- Check login status
- Check high temperature
- Check even number

---

# 2. if else Statement

The `if else` statement provides two possible outcomes.

Syntax:

```python
if condition:
    statement
else:
    statement
```

Example:

```python
marks = 45

if marks >= 50:
    print("Pass")
else:
    print("Fail")
```

Output:

```
Fail
```

Flow:

```
Condition

   │

True ─────► if block

False ───► else block
```

---

## When to Use

Use `if else` when there are only two possible outcomes.

Examples:

- Pass or Fail
- Even or Odd
- Eligible or Not Eligible
- Discount Available or Not

---

# 3. if elif else Statement

Used when there are multiple conditions.

Syntax:

```python
if condition1:
    statement

elif condition2:
    statement

elif condition3:
    statement

else:
    statement
```

Example:

```python
marks = 82

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")
```

Output:

```
Grade B
```

Only one block executes.

---

## When to Use

Examples:

- Student grades
- Salary bonus
- Ticket categories
- Weather classification

---

# 4. Nested if

A nested `if` means an `if` statement inside another `if`.

Syntax:

```python
if condition1:

    if condition2:
        statement
```

Example:

```python
username = "admin"
password = "admin123"

if username == "admin":

    if password == "admin123":
        print("Login Successful")
```

Flow:

```
Condition 1

     │

True

     │

Condition 2

     │

True

     ▼

Execute
```

---

## When to Use

When one decision depends on another.

Examples:

- Login systems
- Bank withdrawal
- Student admission
- Employee promotion

---

# 5. Multiple Conditions

Multiple conditions are created using logical operators.

Operators:

```
and

or

not
```

---

## AND Operator

Both conditions must be True.

Example:

```python
if age >= 18 and citizen:
```

Used for:

- Voting eligibility
- Exam eligibility
- Job applications

---

## OR Operator

At least one condition must be True.

Example:

```python
if is_admin or is_manager:
```

Used for:

- Permission systems
- User roles

---

## NOT Operator

Reverses a condition.

Example:

```python
if not logged_in:
```

Used for:

- Validation
- Authentication
- Security checks

---

# 6. Guard Clauses

A guard clause checks invalid conditions first.

Instead of deeply nested code, invalid cases are handled immediately.

Example:

Instead of:

```python
if payment:

    if amount > 0:

        print("Success")
```

Use:

```python
if not payment:
    print("Payment Failed")

elif amount <= 0:
    print("Invalid Amount")

else:
    print("Payment Successful")
```

Advantages:

- Easier to read
- Less nesting
- Better debugging
- Cleaner code

---

# 7. Decision Making Patterns

Decision making follows common logic patterns used in software development.

---

## Validation Pattern

Checks whether the input is valid.

Examples:

- Username validation
- Password validation
- Age validation
- File validation

Example:

```python
if age < 18:
    print("Invalid")
```

---

## Range Checking

Checks whether a value falls within a range.

Example:

```
90-100 → Excellent

75-89 → Good

50-74 → Average

Below 50 → Fail
```

Examples:

- Marks
- Salary slabs
- Age groups
- Temperature

---

## Category Selection

Selects one option from multiple categories.

Example:

```
Premium

Gold

Regular
```

Examples:

- Customer types
- Membership plans
- Product categories

---

## Decision Tree

A decision tree contains multiple connected decisions.

Example:

```
Login

   │

Username Valid?

   │

Password Valid?

   │

Access Granted
```

Examples:

- Banking
- Recruitment
- Online shopping
- Insurance approval

---

# Best Practices

✔ Write meaningful conditions

✔ Keep conditions simple

✔ Avoid unnecessary nesting

✔ Use `elif` instead of multiple `if` statements when only one result is required

✔ Use guard clauses for invalid inputs

✔ Indent code properly

---

# Common Mistakes

❌ Missing colon

```python
if age > 18
```

Correct:

```python
if age > 18:
```

---

❌ Wrong indentation

```python
if age > 18:
print("Eligible")
```

Correct:

```python
if age > 18:
    print("Eligible")
```

---

❌ Using `=` instead of `==`

Wrong:

```python
if age = 18:
```

Correct:

```python
if age == 18:
```

---

# Real-World Applications

## Banking

- Withdraw money
- Check balance
- Loan approval

---

## Education

- Grade calculation
- Attendance check
- Admission process

---

## E-Commerce

- Discount calculation
- Payment validation
- Product availability

---

## Authentication

- Login
- Role verification
- Permission checking

---

# Quick Revision

| Concept | Purpose |
|----------|----------|
| if | Execute when condition is True |
| if else | Two possible outcomes |
| if elif else | Multiple choices |
| Nested if | Decision inside another decision |
| Multiple Conditions | Combine conditions |
| Guard Clauses | Handle invalid cases first |
| Validation | Check correctness of input |
| Range Checking | Check value ranges |
| Category Selection | Choose one category |
| Decision Tree | Multiple connected decisions |

---

# Summary

After completing this module, you can:

- Write conditional statements
- Build decision-making logic
- Validate user input
- Handle multiple scenarios
- Reduce nested code
- Apply common programming patterns

---

## Next Module

```
Phase 1 – Step 5

Loops & Iteration
```