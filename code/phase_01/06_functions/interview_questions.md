# Phase 1 - Step 6: Functions Interview Questions & Answers

## Overview

This document contains commonly asked Python **Functions** interview questions and answers, starting from beginner level and progressing to intermediate concepts.

Topics Covered:

- Function Basics
- Parameters
- Arguments
- Return Values
- Default Arguments
- Keyword Arguments
- Positional Arguments
- Variable Arguments
- Local Scope
- Global Scope
- nonlocal
- Lambda Functions
- Recursion
- Function Design Patterns

---

# Beginner Level

## 1. What is a function?

### Answer

A function is a reusable block of code that performs a specific task.

Instead of writing the same code repeatedly, we write it once inside a function and call it whenever needed.

Example

```python
def greet():
    print("Hello")

greet()
```

---

## 2. Why do we use functions?

### Answer

Functions help to:

- Reduce code duplication
- Improve readability
- Improve reusability
- Simplify debugging
- Make programs modular
- Improve maintenance

---

## 3. How do you define a function?

### Answer

Functions are defined using the `def` keyword.

Syntax

```python
def function_name():
    pass
```

Example

```python
def welcome():
    print("Welcome")
```

---

## 4. How do you call a function?

### Answer

A function executes only when it is called.

Example

```python
welcome()
```

---

## 5. What is a parameter?

### Answer

A parameter is a variable defined in the function declaration.

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

## 6. What is an argument?

### Answer

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

## 7. Difference between parameter and argument?

### Answer

| Parameter | Argument |
|-----------|----------|
| Variable in function definition | Actual value passed |
| Receives value | Supplies value |

---

## 8. Can a function have multiple parameters?

### Answer

Yes.

Example

```python
def student(name, age):
    print(name, age)
```

---

## 9. What is a return statement?

### Answer

The `return` statement sends a value back to the caller.

Example

```python
def add(a, b):
    return a + b
```

---

## 10. Difference between print() and return?

### Answer

| print() | return |
|----------|---------|
| Displays output | Sends value back |
| Cannot reuse result | Result can be reused |
| Ends after printing | Caller receives value |

---

# Arguments

## 11. What are default arguments?

### Answer

Default arguments provide a value when no argument is passed.

Example

```python
def greet(name="Guest"):
    print(name)
```

---

## 12. What are positional arguments?

### Answer

Arguments passed according to their position.

Example

```python
student("Kalid", 25)
```

---

## 13. What are keyword arguments?

### Answer

Arguments passed using parameter names.

Example

```python
student(age=25, name="Kalid")
```

---

## 14. Can positional and keyword arguments be mixed?

### Answer

Yes.

Positional arguments must come first.

Correct

```python
student("Kalid", age=25)
```

Incorrect

```python
student(age=25, "Kalid")
```

---

## 15. What are variable-length arguments?

### Answer

Python provides:

- `*args`
- `**kwargs`

They allow functions to accept any number of arguments.

---

# *args and **kwargs

## 16. What is *args?

### Answer

`*args` accepts multiple positional arguments.

Example

```python
def add(*numbers):
    print(numbers)
```

---

## 17. What is **kwargs?

### Answer

`**kwargs` accepts multiple keyword arguments.

Example

```python
def student(**details):
    print(details)
```

---

## 18. Difference between *args and **kwargs?

### Answer

| *args | **kwargs |
|--------|-----------|
| Positional arguments | Keyword arguments |
| Tuple | Dictionary |

---

## 19. When should you use *args?

### Answer

Use `*args` when the number of positional arguments is unknown.

Examples:

- Sum of numbers
- Average calculation
- Mathematical operations

---

## 20. When should you use **kwargs?

### Answer

Use `**kwargs` when the number of keyword arguments is unknown.

Examples:

- User profiles
- Configuration settings
- Product details

---

# Scope

## 21. What is variable scope?

### Answer

Scope determines where a variable can be accessed.

Python has:

- Local
- Enclosing
- Global
- Built-in

---

## 22. What is a local variable?

### Answer

A local variable exists only inside the function where it is created.

Example

```python
def show():
    name = "Kalid"
```

---

## 23. What is a global variable?

### Answer

A global variable is declared outside all functions.

Example

```python
company = "OpenAI"
```

---

## 24. What is the global keyword?

### Answer

The `global` keyword allows a function to modify a global variable.

Example

```python
count = 10

def update():

    global count

    count += 1
```

---

## 25. What is the nonlocal keyword?

### Answer

`nonlocal` modifies variables from the enclosing function.

Example

```python
def outer():

    value = 5

    def inner():

        nonlocal value

        value += 1
```

---

## 26. What is the LEGB Rule?

### Answer

Python searches variables in this order:

```
L → Local

E → Enclosing

G → Global

B → Built-in
```

---

# Lambda Functions

## 27. What is a lambda function?

### Answer

A lambda function is an anonymous one-line function.

Example

```python
square = lambda x: x * x
```

---

## 28. When should lambda functions be used?

### Answer

Lambda functions are useful for:

- Sorting
- Filtering
- Mapping
- Small calculations

---

## 29. Difference between lambda and normal functions?

### Answer

| Lambda | Normal Function |
|---------|-----------------|
| One line | Multiple lines |
| Anonymous | Named |
| Simple operations | Complex logic |

---

# Recursion

## 30. What is recursion?

### Answer

Recursion is when a function calls itself.

Example

```python
def display(n):

    if n == 0:
        return

    print(n)

    display(n - 1)
```

---

## 31. What is a base case?

### Answer

A base case is the stopping condition in recursion.

Without it, recursion never ends.

---

## 32. What happens if recursion has no base case?

### Answer

Python raises:

```
RecursionError
```

---

## 33. What are the advantages of recursion?

### Answer

- Cleaner code
- Easier tree traversal
- Divide-and-conquer algorithms
- Elegant solutions

---

## 34. What are the disadvantages of recursion?

### Answer

- More memory usage
- Slower than loops
- Stack overflow if too deep

---

## 35. Difference between recursion and loops?

### Answer

| Loop | Recursion |
|------|-----------|
| Uses for/while | Function calls itself |
| Faster | Slightly slower |
| Less memory | More memory |
| Simpler for repetition | Better for recursive problems |

---

# Function Design

## 36. What is a validation function?

### Answer

Checks whether input is valid.

Example

```python
def is_valid(age):

    return age >= 18
```

---

## 37. What is a calculation function?

### Answer

Performs mathematical operations.

Example

```python
def add(a, b):

    return a + b
```

---

## 38. What is a search function?

### Answer

Searches for data and returns the result.

Example

```python
def search(items, target):
    ...
```

---

## 39. What is a conversion function?

### Answer

Converts one format to another.

Example

```python
def celsius_to_fahrenheit(c):
    return (c * 9 / 5) + 32
```

---

## 40. Why should functions perform only one task?

### Answer

Functions should follow the **Single Responsibility Principle**, making code:

- Easier to test
- Easier to debug
- Easier to maintain
- More reusable

---

# Scenario-Based Questions

## 41. When should you use a function instead of repeating code?

### Answer

Whenever the same logic is used multiple times, create a function to improve readability and avoid duplication.

---

## 42. When should you use return instead of print?

### Answer

Use `return` when the result needs to be reused, stored, or passed to another function.

---

## 43. When should you use *args?

### Answer

Use `*args` when you don't know how many positional arguments the function will receive.

---

## 44. When should you use **kwargs?

### Answer

Use `**kwargs` when you don't know the names or number of keyword arguments in advance.

---

## 45. When should you use recursion instead of loops?

### Answer

Use recursion for problems with recursive structures, such as:

- Tree traversal
- Directory traversal
- Factorial
- Fibonacci
- Divide-and-conquer algorithms

---

# Common Mistakes

## 46. What happens if you forget to call a function?

### Answer

The function is defined but never executed.

---

## 47. What happens if you forget the return statement?

### Answer

The function returns `None` by default.

---

## 48. Can a function return multiple values?

### Answer

Yes.

Example

```python
def student():
    return "Kalid", 25
```

---

## 49. Can a function call another function?

### Answer

Yes.

Functions can call other functions, which helps build modular programs.

---

## 50. What are the benefits of modular programming using functions?

### Answer

- Better code organization
- Reusability
- Easier maintenance
- Easier testing
- Reduced duplication
- Improved readability

---

# Quick Revision Table

| Concept | Key Point |
|----------|-----------|
| Function | Reusable block of code |
| Parameter | Receives value |
| Argument | Sends value |
| Return | Sends result back |
| Default Argument | Provides default value |
| Positional Argument | Based on position |
| Keyword Argument | Based on parameter name |
| *args | Unlimited positional arguments |
| **kwargs | Unlimited keyword arguments |
| Local Variable | Exists inside function |
| Global Variable | Exists outside function |
| global | Modifies global variable |
| nonlocal | Modifies enclosing variable |
| Lambda | Anonymous one-line function |
| Recursion | Function calling itself |
| Base Case | Stops recursion |

---

# Interview Checklist

- [ ] Explain functions
- [ ] Define and call functions
- [ ] Explain parameters and arguments
- [ ] Differentiate `print()` and `return`
- [ ] Explain default, positional, and keyword arguments
- [ ] Explain `*args` and `**kwargs`
- [ ] Explain local and global variables
- [ ] Explain `global` and `nonlocal`
- [ ] Explain the LEGB rule
- [ ] Explain lambda functions
- [ ] Explain recursion and base cases
- [ ] Compare recursion and loops
- [ ] Explain common function design patterns
```