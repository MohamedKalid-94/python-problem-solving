# Phase 1 - Step 4: Decision Making Practice

## Overview

This practice sheet helps you strengthen your understanding of Python decision-making statements.

Topics covered:

- Simple if
- if else
- if elif else
- Nested if
- Multiple conditions
- Guard clauses
- Decision-making patterns

Try solving each problem without looking at previous examples.

---

# Section 1: Simple if

## 1. Positive Number

Write a program to check whether a number is positive.

Example:

```
Input:
15

Output:
Number is positive
```

---

## 2. Even Number

Write a program to check whether a number is even.

---

## 3. High Temperature

If the temperature is above 35°C, display:

```
High Temperature Warning
```

---

## 4. Login Status

If the user is logged in, display:

```
Welcome User
```

---

## 5. Account Balance

If the balance is greater than zero, display:

```
Account Active
```

---

# Section 2: if else

## 6. Even or Odd

Determine whether a number is even or odd.

---

## 7. Pass or Fail

If marks are greater than or equal to 50:

```
Pass
```

Otherwise:

```
Fail
```

---

## 8. Voting Eligibility

If age is 18 or above:

```
Eligible
```

Otherwise:

```
Not Eligible
```

---

## 9. Discount Availability

If purchase amount is ₹1000 or more:

```
Discount Available
```

Otherwise:

```
No Discount
```

---

## 10. ATM Balance Check

If withdrawal amount is less than or equal to balance:

```
Transaction Successful
```

Otherwise:

```
Insufficient Balance
```

---

# Section 3: if elif else

## 11. Grade Calculator

Rules:

```
90+   Grade A
75+   Grade B
50+   Grade C
Below 50  Fail
```

---

## 12. Weather Category

```
Above 35   Hot

20-35      Normal

Below 20   Cold
```

---

## 13. Movie Ticket

```
Below 5      Free

5-18         Child

19-60        Adult

Above 60     Senior Citizen
```

---

## 14. Employee Bonus

```
10+ Years    High Bonus

5+ Years     Medium Bonus

Below 5      Normal Bonus
```

---

## 15. Customer Membership

Categories:

```
Premium

Gold

Silver

Regular
```

Display the customer category.

---

# Section 4: Nested if

## 16. Login System

Conditions:

- Username should be correct.
- Password should be correct.

Display appropriate messages.

---

## 17. Bank Withdrawal

Conditions:

- Account should be active.
- Balance should be sufficient.

---

## 18. Student Admission

Conditions:

- Entrance exam passed.
- Minimum age requirement satisfied.

---

## 19. Employee Promotion

Conditions:

- Minimum experience.
- Good performance rating.

---

## 20. Online Course Enrollment

Conditions:

- Registration completed.
- Payment completed.

---

# Section 5: Multiple Conditions

## 21. Voting Eligibility

Conditions:

- Age ≥ 18
- Citizen = True

---

## 22. Job Application

Conditions:

- Experience ≥ 2 years
- Python skill available

---

## 23. Credit Card Approval

Conditions:

- Salary ≥ ₹30,000
- Credit Score ≥ 700

---

## 24. Exam Eligibility

Conditions:

- Attendance ≥ 75%
- Fees Paid

---

## 25. Scholarship Eligibility

Conditions:

- Marks ≥ 90
- Attendance ≥ 90%

---

# Section 6: Guard Clauses

## 26. Validate Age

Reject users below 18 years.

---

## 27. Validate Username

Reject:

- Empty username
- Username less than 5 characters

---

## 28. Validate Payment

Reject:

- Payment not completed
- Amount less than or equal to zero

---

## 29. Validate File Upload

Reject:

- File not found
- Invalid file format

---

## 30. Validate Email

Reject empty email address.

---

# Section 7: Decision Patterns

## 31. Range Checking

Classify marks into:

```
Excellent

Good

Average

Fail
```

---

## 32. Salary Slab

Classify salary into:

```
High

Medium

Low
```

---

## 33. Category Selection

Select customer category:

```
Premium

Gold

Regular
```

---

## 34. Validation Pattern

Validate:

- Name
- Age
- Mobile Number

---

## 35. Decision Tree

Design a simple loan approval system.

Conditions:

- Salary
- Credit Score
- Employment Status

---

# Output Prediction

## 36.

Predict the output:

```python
age = 20

if age >= 18:
    print("Eligible")
```

---

## 37.

Predict the output:

```python
marks = 45

if marks >= 50:
    print("Pass")
else:
    print("Fail")
```

---

## 38.

Predict the output:

```python
number = 10

if number > 0:
    print("Positive")

elif number == 0:
    print("Zero")

else:
    print("Negative")
```

---

## 39.

Predict the output:

```python
age = 25
citizen = True

if age >= 18 and citizen:
    print("Eligible")
```

---

## 40.

Predict the output:

```python
logged_in = False

if not logged_in:
    print("Please Login")
```

---

# Mini Projects

## Project 1: Student Result System

Features:

- Marks
- Grade
- Pass/Fail

---

## Project 2: ATM Withdrawal

Features:

- Account Active
- Balance Check
- Withdrawal Approval

---

## Project 3: Login System

Features:

- Username Validation
- Password Validation
- Role Verification

---

## Project 4: Online Shopping Discount

Features:

- Purchase Amount
- Membership Type
- Final Discount

---

## Project 5: College Admission

Features:

- Marks Validation
- Entrance Exam
- Age Verification
- Admission Decision

---

# Challenge Exercises

1. Write a program using only `if`.
2. Convert an `if else` program into an `if elif else` program.
3. Rewrite a nested `if` using multiple conditions.
4. Identify where guard clauses can simplify nested code.
5. Design a decision tree for an online food ordering system.
6. Create a grading system with five grade levels.
7. Build a movie ticket pricing program using conditions.
8. Create a loan approval system using multiple conditions.
9. Validate user registration details.
10. Build a simple menu-driven decision program.

---

# Practice Checklist

## Simple if

- [ ] Positive number
- [ ] Even number
- [ ] Temperature check
- [ ] Login status

## if else

- [ ] Pass/Fail
- [ ] Voting eligibility
- [ ] Discount check
- [ ] ATM withdrawal

## if elif else

- [ ] Grade calculation
- [ ] Weather category
- [ ] Ticket category
- [ ] Bonus calculation

## Nested if

- [ ] Login
- [ ] Admission
- [ ] Promotion
- [ ] Withdrawal

## Multiple Conditions

- [ ] AND
- [ ] OR
- [ ] NOT

## Guard Clauses

- [ ] Age validation
- [ ] Username validation
- [ ] Payment validation
- [ ] File validation

## Decision Patterns

- [ ] Validation
- [ ] Range checking
- [ ] Category selection
- [ ] Decision tree

---

# Goal

After completing all practice problems, you should be able to:

- Write conditional statements confidently.
- Solve beginner-level logic problems.
- Build real-world decision-making programs.
- Prepare for coding interviews and programming assessments.