# Interview Questions & Answers - Writing Clean Python

## Beginner

### 1. What is PEP 8?
The official style guide for Python code. It covers naming, indentation (4 spaces), line length (79), blank lines, imports and more. It makes code look the same across projects.

### 2. What naming style does Python use?
`snake_case` for variables, functions and methods, `PascalCase` for classes, `UPPER_CASE` for constants.

### 3. What is a docstring?
The first string in a module, function or class that explains what it does. You can read it with `help()` or `__doc__`.

### 4. What are type hints?
Notes about the expected types, such as `def add(a: int, b: int) -> int`. They help readers, IDEs and tools.

### 5. Why use `logging` instead of `print()`?
Logging has levels (DEBUG to CRITICAL), can show time and source, can go to files, and can be turned on or off without editing the code.

### 6. What is refactoring?
Improving the structure of code without changing what it does.

### 7. Why is `if not items:` better than `if len(items) == 0:`?
It is shorter and works for any empty collection. It is the style PEP 8 recommends.

## Intermediate

### 8. Why is naming a variable `list` or `max` a problem?
It hides the built-in with the same name. After `max = 10`, calling `max([1, 5, 3])` raises `TypeError: 'int' object is not callable`.

### 9. What do `_name` and `__name` mean?
`_name` means "internal, do not use from outside" (only a convention). `__name` inside a class is name-mangled to `_ClassName__name`, which makes accidental access harder.

### 10. Why compare with `None` using `is`?
`None` is a single object, so `is None` checks identity. It is faster and cannot be tricked by a class that redefines `==`.

### 11. Do type hints stop wrong types at runtime?
No. `add_numbers("a", "b")` still runs. Python ignores hints at runtime. Tools like `mypy` and `pyright` check them before you run the code.

### 12. What goes into a good docstring?
A short imperative summary line, then the arguments, the return value, the errors raised, and ideally an example. Do not just repeat the function name.

### 13. What is the difference between `logger.error()` and `logger.exception()`?
`logger.exception()` is used inside an `except` block and logs the message **and the full traceback**. `logging.error(error)` only logs the message text, so you lose where the error happened.

### 14. Why configure logging in `main()` and not at the top of a file?
Code at the top of a module runs when it is imported, which changes logging for every program that imports it. Only the entry point should configure logging.

### 15. Why write `logger.debug("x = %s", x)` instead of an f-string?
With `%s` the message is built only if the DEBUG level is on. An f-string is always built, even when the message is thrown away.

### 16. What is a guard clause?
An early `return` that handles the bad case first (`if weight <= 0: return None`), so the main logic stays at the top level without deep nesting.

### 17. What is a magic number and how do you fix it?
A number in the code with no explanation (`cost * 0.1`). Give it a named constant (`MEMBER_DISCOUNT = 0.10`) so the meaning is clear and it can be changed in one place.

## Advanced

### 18. When do you use `assert` and when `raise`?
Use `raise` for bad input from users, files or networks. Use `assert` for conditions that can only be false if your own code has a bug.

### 19. What is wrong with using `assert` to validate input?
Assertions are removed when Python runs with `-O`. The check disappears and bad data goes through (in the example `divide(10, 0)` becomes a `ZeroDivisionError` instead of a clear message).

### 20. What is the common `assert` mistake with parentheses?
`assert (x > 0, "message")` is a non-empty tuple, which is always true, so the assertion never fails. Write `assert x > 0, "message"`.

### 21. How do you refactor safely?
Keep the behavior the same and prove it: run the old and new code on the same inputs (the file compares 8 cases) or, in real projects, run automated tests before and after every small change.

### 22. What does "one function, one job" mean?
A function should do one thing: parse, calculate, format or print. Small functions are easy to name, test and reuse. `bad_do_everything` loads, validates, calculates and prints in one block.

### 23. How do you catch the right exceptions?
Catch the specific one (`ZeroDivisionError`, `FileNotFoundError`), not `Exception` or a bare `except:`. A broad catch hides real bugs.

### 24. Which tools do you use to keep a codebase clean?
A formatter (`ruff format` or `black`), a linter (`ruff` or `flake8`), a type checker (`mypy` or `pyright`), `pytest` for tests, and `pre-commit` or CI to run them automatically.

### 25. What is DRY and why does it matter?
"Don't Repeat Yourself." Copied code means a bug or a rule change must be fixed in several places. In `bad_shipping_cost` the same discount code appears twice. In the clean version it appears once.

### 26. What is the difference between Optional[int] and int | None?
They mean the same thing: an int or None. `int | None` is the newer syntax (Python 3.10+), and `Optional[int]` comes from `typing` and works on older versions.

### 27. What does `from helpers import separator` give you compared with copying the function into every file?
One place to change and no duplicates. Copy-pasted helper functions are a common code smell.

## Practical Tasks

1. Rename the variables and function in a short script and explain every choice.
2. Rewrite a function with `==  True`, `== None` and `len(x) == 0` in PEP 8 style.
3. Write a docstring with Args, Returns and Raises.
4. Add type hints to a function that may return `None`.
5. Replace `print()` and `except Exception` with `logger` and a specific exception.
6. Decide `raise` or `assert` for five different checks.
7. Refactor a function with three levels of nested ifs and prove the behavior is unchanged.