# Phase 1 - Step 6: Functions Notes

## Overview

A **function** is a reusable block of code that performs a specific task. Functions help organize programs into smaller, manageable pieces, making code easier to read, test, maintain, and reuse.

Instead of writing the same code multiple times, we write it once inside a function and call it whenever needed.

---

# Why Do We Need Functions?

Functions help to:

- Reduce code duplication
- Improve readability
- Improve code reusability
- Simplify debugging
- Make programs modular
- Divide large problems into smaller tasks

Without Functions

```python
print("Welcome")
print("Welcome")
print("Welcome")
```

With Functions

```python
def welcome():
    print("Welcome")

welcome()
welcome()
welcome()
```

---

# Function Syntax

```python
def function_name():
    print("Hello")
```

Calling the function

```python
function_name()
```

---

# Function Definition

A function is created using the `def` keyword.

Syntax

```python
def greet():
    print("Hello")
```

---

# Function Call

A function executes only when it is called.

```python
greet()
```

---

# Parameters

A parameter is a variable defined in the function header that receives data.

Example

```python
def greet(name):
    print(name)
```

Here,

```
name
```

is the parameter.

---

# Arguments

An argument is the actual value passed to a function.

Example

```python
greet("Kalid")
```

Here,

```
"Kalid"
```

is the argument.

---

# Parameter vs Argument

| Parameter | Argument |
|-----------|----------|
| Variable in function definition | Actual value passed |
| Receives data | Sends data |

---

# Multiple Parameters

Functions can receive multiple values.

Example

```python
def student(name, age):
    print(name)
    print(age)

student("Kalid", 25)
```

---

# Return Values

A function can return data using the `return` statement.

Example

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

---

# Returning Multiple Values

Python allows multiple values to be returned.

Example

```python
def student():

    return "Kalid", 25

name, age = student()
```

---

# print() vs return

| print() | return |
|----------|---------|
| Displays output | Sends value back |
| Cannot reuse easily | Can reuse later |
| Ends after display | Caller receives value |

---

# Default Arguments

Default arguments provide a value when the caller does not pass one.

Example

```python
def greet(name="Guest"):
    print(name)

greet()

greet("Kalid")
```

Output

```
Guest

Kalid
```

---

# Keyword Arguments

Arguments can be passed using parameter names.

Example

```python
def student(name, age):

    print(name)
    print(age)

student(age=25, name="Kalid")
```

---

# Positional Arguments

Arguments are assigned according to their position.

Example

```python
student("Kalid", 25)
```

---

# Mixed Arguments

Positional arguments must come before keyword arguments.

Correct

```python
student("Kalid", age=25)
```

Incorrect

```python
student(age=25, "Kalid")
```

---

# Variable Length Arguments

Sometimes we don't know how many arguments will be passed.

Python provides:

- *args
- **kwargs

---

# *args

Accepts multiple positional arguments.

Example

```python
def add(*numbers):

    total = 0

    for number in numbers:
        total += number

    return total
```

Call

```python
add(10,20,30,40)
```

---

# **kwargs

Accepts multiple keyword arguments.

Example

```python
def student(**details):

    print(details["name"])
```

Call

```python
student(name="Kalid", age=25)
```

---

# Variable Scope

A variable's scope determines where it can be accessed.

Python has:

- Local Scope
- Global Scope
- Enclosing Scope
- Built-in Scope

This is called the **LEGB Rule**.

---

# Local Variables

Local variables exist only inside a function.

Example

```python
def display():

    name = "Kalid"

    print(name)
```

Outside the function,

```
name
```

does not exist.

---

# Global Variables

Global variables are created outside all functions.

Example

```python
company = "OpenAI"

def show():
    print(company)
```

---

# global Keyword

Used when modifying a global variable.

Example

```python
count = 10

def update():

    global count

    count += 1
```

---

# Nested Functions

Functions can exist inside other functions.

Example

```python
def outer():

    def inner():
        print("Hello")

    inner()
```

---

# nonlocal Keyword

Used to modify variables in the enclosing function.

Example

```python
def outer():

    count = 10

    def inner():

        nonlocal count

        count += 1

    inner()
```

---

# LEGB Rule

Python searches variables in this order:

```
Local

↓

Enclosing

↓

Global

↓

Built-in
```

---

# Lambda Functions

Lambda functions are anonymous one-line functions.

Syntax

```python
lambda parameters : expression
```

Example

```python
square = lambda number: number * number

print(square(5))
```

Equivalent Function

```python
def square(number):

    return number * number
```

---

# Advantages of Lambda

- Short syntax
- Easy to read
- Useful with sorting
- Useful with filtering
- Useful with mapping

---

# Recursion

Recursion is when a function calls itself.

Example

```python
def display(number):

    if number > 5:
        return

    print(number)

    display(number + 1)
```

---

# Base Case

The condition that stops recursion.

Example

```python
if number > 5:
    return
```

Without a base case,

```
RecursionError
```

will occur.

---

# Factorial Example

```python
def factorial(number):

    if number == 1:
        return 1

    return number * factorial(number-1)
```

---

# Recursion vs Loop

| Loop | Recursion |
|------|-----------|
| Uses for/while | Calls itself |
| Faster | Slightly slower |
| Less memory | Uses call stack |
| Easier | Useful for recursive problems |

---

# Function Design Patterns

Functions are commonly written for reusable tasks.

---

## Validation Function

Checks whether input is valid.

Example

```python
def is_valid_age(age):

    return age >= 18
```

---

## Calculation Function

Performs calculations.

Example

```python
def add(a,b):

    return a+b
```

---

## Search Function

Searches for data.

Example

```python
def search(items,target):

    for item in items:

        if item == target:
            return True

    return False
```

---

## Conversion Function

Converts one value into another.

Example

```python
def celsius_to_fahrenheit(c):

    return (c*9/5)+32
```

---

## Menu Function

Displays reusable menus.

Example

```python
def menu():

    print("1. Add")
    print("2. Exit")
```

---

# Common Mistakes

## Forgetting to Call the Function

Wrong

```python
def greet():

    print("Hello")
```

Nothing happens.

Correct

```python
greet()
```

---

## Forgetting return

Wrong

```python
def add(a,b):

    a+b
```

Correct

```python
def add(a,b):

    return a+b
```

---

## Modifying Global Variables

Wrong

```python
count = 10

def update():

    count += 1
```

Correct

```python
count = 10

def update():

    global count

    count += 1
```

---

## Infinite Recursion

Wrong

```python
def test():

    test()
```

Always provide a base case.

---

# Best Practices

- Use meaningful function names.
- Keep functions small.
- Perform one task per function.
- Return values instead of printing when possible.
- Avoid unnecessary global variables.
- Use default arguments wisely.
- Write reusable functions.
- Add comments and docstrings.

---

# Real-World Applications

## Banking

- Deposit
- Withdraw
- Balance check

---

## Education

- Grade calculation
- Attendance
- Student search

---

## E-Commerce

- Product search
- Price calculation
- Discount calculation

---

## Data Processing

- Validation
- Conversion
- Searching
- Filtering

---

## Web Applications

- Login
- Registration
- Authentication
- Form validation

---

# Quick Revision

| Concept | Purpose |
|----------|---------|
| Function | Reusable block of code |
| Parameter | Receives data |
| Argument | Sends data |
| Return | Sends value back |
| Default Argument | Default value |
| Keyword Argument | Pass by name |
| Positional Argument | Pass by position |
| *args | Multiple positional arguments |
| **kwargs | Multiple keyword arguments |
| Local Variable | Inside function |
| Global Variable | Outside function |
| global | Modify global variable |
| nonlocal | Modify enclosing variable |
| Lambda | One-line anonymous function |
| Recursion | Function calls itself |

---

# Summary

After completing this module, you can:

- Define and call functions
- Work with parameters and arguments
- Return values from functions
- Use default, positional, and keyword arguments
- Handle variable-length arguments using `*args` and `**kwargs`
- Understand variable scope and the LEGB rule
- Use `global` and `nonlocal`
- Write lambda functions
- Understand recursion and base cases
- Design reusable functions for validation, calculation, searching, conversion, and menus

---

# Next Module

```
Phase 1 – Step 7

Modules, Packages & Exception Handling
```