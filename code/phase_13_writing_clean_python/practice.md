# Practice - Writing Clean Python

Run each example file first. Then try these. For every "fix" exercise, write the clean version and compare the output with the original.

## 01 Naming

1. Rename the variables and function: `def f(x, y, z): return x * y + z` that calculates `price * quantity + shipping`.
2. Fix this and explain the error: `sum = 0` followed by `sum([1, 2, 3])`.
3. Rename these booleans so they read like questions: `active`, `discount`, `login`.
4. Write a class `Student` with `_marks` and `__id`. Print `student._Student__id`.
5. Move a constant from inside a function to the top of the module. Why is that better?
6. Write 5 bad names and their clean replacements.

## 02 PEP 8

7. Rewrite this properly: `def total(a,b): return a+b`.
8. Replace `if len(items) == 0:` and `if flag == True:` with clean versions.
9. Fix `if value == None:`. Why is `is` correct here?
10. Split a 100-character line into lines under 79 characters.
11. Reorder these imports into three groups: `import requests`, `import os`, `from helpers import separator`, `import sys`.
12. Install `ruff`, run `ruff check .` on a folder from an earlier phase, and fix three problems.

## 03 Docstrings

13. Write a Google-style docstring for `def is_even(number)`.
14. Add `Args`, `Returns` and `Raises` to a division function.
15. Add a doctest example and run `doctest.testmod()`. What happens if the example output is wrong?
16. Write a class docstring with an `Attributes` section for a `Book` class.
17. Rewrite `"""This function adds two numbers."""` so it is not a copy of the code.
18. Call `help()` on your own function and read the result.

## 04 Type Hints

19. Add type hints: `def greet(name, age): return name + " is " + str(age)`.
20. Write `def find_user(users: dict[str, int], name: str) -> ...` that may return `None`. Which hint do you use?
21. Call a hinted function with the wrong type. Does Python stop you? Which tool would?
22. Install `mypy` and run it on a file with a wrong call.
23. Add hints to a function that takes a list of strings and returns a dictionary of counts.
24. What is the difference between `list`, `list[int]` and `list[str]` in a hint?

## 05 Logging

25. Replace three `print()` calls in a program with `logger.info` and `logger.warning`.
26. Move `logging.basicConfig` from the top of a file into `main()`. Why?
27. Change the level to `INFO`. Which messages disappear?
28. Replace `logging.error(error)` with `logger.exception(...)` and compare the output.
29. Write a function that catches `FileNotFoundError` and logs it with a traceback.
30. Add a `FileHandler` so the logs also go to `app.log`.

## 06 Assertions

31. For each case, choose `raise` or `assert`: user age input, a function result that must never be negative, a missing config file, an internal list that must never be empty here.
32. Run `python -O 06_assertions_complete.py` and explain every difference.
33. Fix: `assert (x > 0, "x must be positive")`. Why does the original never fail?
34. Rewrite a function that uses `assert` to check its arguments so it uses `ValueError`.

## 07 Code Organization

35. Take a script that reads numbers, calculates the average and prints it, and split it into `load_numbers`, `calculate_average` and `show_result`.
36. Add a `save_report(report, filename)` function to `07_code_organization_complete.py` that writes the report to a file.
37. Add a "discount" step to the order total without editing the existing functions.
38. Create a package: a folder with `__init__.py`, `parsers.py` and `reports.py`. Import from it.
39. Find a magic number in any earlier phase and replace it with a named constant.
40. Draw the folder structure for a small shop application (`app/`, `models/`, `services/`, `tests/`).

## 08 Refactoring

41. Refactor nested ifs into guard clauses:
    ```python
    def check_age(age):
        if age is not None:
            if age >= 0:
                if age >= 18:
                    return "adult"
                else:
                    return "minor"
            else:
                return "invalid"
        else:
            return "missing"
    ```
42. Refactor two functions that are identical except for one number into one function with a parameter.
43. Replace a long `if / elif` chain of country codes with a dictionary.
44. Write 10 test cases and compare the old and new versions of your refactored function.
45. Change `MEMBER_DISCOUNT` to `0.2`. How many places did you edit? What would it be without the constant?
46. Take any function from phase 14 and refactor it. Show before and after.

## Challenge

47. Clean up a full project from phase 14: names, docstrings, type hints, logging and one refactor. Run `ruff check` and `mypy` until both are clean.
48. Add `ruff check .` and `ruff format --check .` to your `.github/workflows/ci.yml`.
49. Write a short style guide (10 rules) for your own repository.