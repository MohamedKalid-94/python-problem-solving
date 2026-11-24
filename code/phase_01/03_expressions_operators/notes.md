# Phase 1 - Step 3: Expressions & Operators Notes

## Overview

Expressions and operators are the foundation of programming logic.

Operators allow Python programs to perform:

- Mathematical calculations
- Value comparisons
- Decision making
- Searching
- Object checking
- Updating values

An expression is a combination of:

```
Values + Variables + Operators
```

Example:

```python
total = price * quantity
```

Here:

- `price` → Variable
- `quantity` → Variable
- `*` → Operator
- `price * quantity` → Expression


---

# 1. Arithmetic Operators

Arithmetic operators are used to perform mathematical operations.

## Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| + | Addition | 10 + 5 |
| - | Subtraction | 10 - 5 |
| * | Multiplication | 10 * 5 |
| / | Division | 10 / 5 |
| % | Modulus | 10 % 3 |
| // | Floor Division | 10 // 3 |
| ** | Power | 2 ** 3 |


---

## Addition (+)

Used to add two values.

Example:

```python
a = 10
b = 20

result = a + b
```

Output:

```
30
```


Real-world examples:

- Adding salary components
- Calculating total marks
- Shopping bill calculation


---

## Subtraction (-)

Used to find the difference between values.

Example:

```python
price = 1000
discount = 200

final_price = price - discount
```


Output:

```
800
```


---

## Multiplication (*)

Used to multiply values.

Example:

```python
price = 100
quantity = 5

total = price * quantity
```


Output:

```
500
```


---

## Division (/)

Used to divide values.

Example:

```python
total_marks = 500
students = 5

average = total_marks / students
```


Output:

```
100
```


---

## Modulus (%)

Returns the remainder after division.

Example:

```python
10 % 3
```


Output:

```
1
```


Real-world usage:

- Checking even or odd numbers
- Finding remaining balance


---

## Floor Division (//)

Returns only the integer part of division.

Example:

```python
10 // 3
```


Output:

```
3
```


---

## Power (**)

Used for exponent calculation.

Example:

```python
2 ** 3
```


Output:

```
8
```


---

# 2. Comparison Operators

Comparison operators compare two values.

The result is always:

```
True
or
False
```


## Operators

| Operator | Meaning |
|-|-|
| == | Equal |
| != | Not Equal |
| > | Greater Than |
| < | Less Than |
| >= | Greater Than or Equal |
| <= | Less Than or Equal |


---

## Equal (==)

Checks whether two values are the same.

Example:

```python
10 == 10
```

Output:

```
True
```


---

## Not Equal (!=)

Checks whether values are different.

Example:

```python
10 != 20
```

Output:

```
True
```


---

## Greater Than (>)

Example:

```python
20 > 10
```

Output:

```
True
```


---

## Less Than (<)

Example:

```python
5 < 10
```

Output:

```
True
```


---

## Greater/Less Than or Equal

Example:

```python
age >= 18
```

Used for:

- Age verification
- Eligibility checking


---

# 3. Logical Operators

Logical operators combine multiple conditions.

## Operators

| Operator | Meaning |
|-|-|
| and | Both conditions must be True |
| or | Any one condition must be True |
| not | Reverse the result |


---

# AND Operator

Both conditions should be True.

Example:

```python
age >= 18 and
citizen == True
```


Result:

```
True only when both are True
```


Real-world examples:

- Login validation
- Bank transaction approval
- Student eligibility


---

# OR Operator

At least one condition should be True.

Example:

```python
is_admin or is_manager
```


Real-world examples:

- Permission systems
- Role checking


---

# NOT Operator

Reverses the result.

Example:

```python
not True
```

Output:

```
False
```


---

# 4. Membership Operators

Membership operators check whether a value exists inside a collection.

## Operators

| Operator | Meaning |
|-|-|
| in | Exists |
| not in | Does not exist |


---

## in Operator

Example:

```python
"Python" in languages
```


Returns:

```
True
```


Used in:

- Searching
- Filtering
- Validation


---

## not in Operator

Example:

```python
"Java" not in languages
```


Returns:

```
True
```


---

# 5. Identity Operators

Identity operators compare object identity.

## Operators

| Operator | Meaning |
|-|-|
| is | Same object |
| is not | Different object |


---

## Difference Between == and is


## ==

Checks values.

Example:

```python
list1 == list2
```

Question:

"Do both objects contain the same data?"


---

## is

Checks memory identity.

Example:

```python
list1 is list2
```

Question:

"Are both variables pointing to the same object?"


---

Example:

```python
a = [1,2,3]

b = a

c = [1,2,3]
```


Results:

```python
a == c
```

True


```python
a is b
```

True


```python
a is c
```

False


---

# 6. Assignment Operators

Assignment operators assign and update values.

## Operators

| Operator | Example |
|-|-|
| = | x = 10 |
| += | x += 5 |
| -= | x -= 5 |
| *= | x *= 5 |
| /= | x /= 5 |


---

# Simple Assignment

Example:

```python
name = "Python"
```


Stores a value in a variable.


---

# Addition Assignment (+=)

Example:

```python
balance = 1000

balance += 500
```


Same as:

```python
balance = balance + 500
```


Result:

```
1500
```


---

# Subtraction Assignment (-=)

Example:

```python
balance -= 200
```


Same as:

```python
balance = balance - 200
```


---

# Operator Precedence

Python follows a priority order when evaluating expressions.


Order:

```
()
**
*
/
%
+
-
```


Example:

```python
result = 10 + 5 * 2
```


Calculation:

```
5 * 2 = 10

10 + 10 = 20
```


Result:

```
20
```


---

# Short Summary

| Category | Purpose |
|-|-|
| Arithmetic | Perform calculations |
| Comparison | Compare values |
| Logical | Combine conditions |
| Membership | Search inside collections |
| Identity | Check object identity |
| Assignment | Store/update values |


---

# Interview Revision

## What is an expression?

A combination of values, variables, and operators that produces a result.


## Difference between = and ==?

`=` assigns a value.

`==` compares values.


## Difference between == and is?

`==` checks values.

`is` checks object identity.


## Difference between / and //?

`/` returns float division.

`//` returns floor division.


## What does % operator do?

Returns the remainder after division.


## What is short-circuit evaluation?

Python stops evaluating logical expressions when the result is already known.


Example:

```python
False and something
```

Python does not check `something` because result is already False.


---

# Phase 1 Step 3 Completed

Concept Flow:

```
Variables
    ↓
Objects
    ↓
Expressions
    ↓
Operators
    ↓
Logic Building
    ↓
Decision Making
```

Next:

```
Phase 1 - Step 4
Conditional Statements
```