# Notes - Writing Clean Python

## 1. Naming (PEP 8)

| What | Style | Example |
|---|---|---|
| Variable, function, method | `snake_case` | `total_price`, `calculate_total()` |
| Class | `PascalCase` | `BankAccount` |
| Constant | `UPPER_CASE` | `MAX_RETRY_COUNT` |
| Module / file | short `lowercase` | `helpers.py` |
| Internal use | `_single_underscore` | `self._balance` |
| Name mangling | `__double_underscore` | `self.__pin` becomes `_BankAccount__pin` |

Good names:
- Say **what it is**, not how it is stored: `user_names`, not `list1`.
- Booleans read like questions: `is_active`, `has_discount`.
- Functions are verbs: `calculate_total`, `load_orders`.
- No single letters except short loops (`i`, `j`) or math.
- Never reuse a built-in name (`list`, `max`, `sum`, `id`, `type`, `input`). It hides the built-in and breaks later code.

```python
max = 10
max([1, 5, 3])      # TypeError: 'int' object is not callable
```

- Put constants at the top of the module, not inside a function.

## 2. PEP 8 Style

- 4 spaces for indentation (never tabs mixed with spaces).
- Lines up to **79** characters (formatters like `black` and `ruff` use 88 by default).
- **Two blank lines** between top-level functions and classes, **one** between methods.
- One statement per line. No `def f(): return x` and no `a = 1; b = 2`.
- Spaces after commas and around operators: `calculate(1000, 100)`, `a + b`.
- Imports at the top, one per line, in three groups separated by a blank line:
  standard library, third-party packages, your own modules.
- Compare with `None` using `is`: `if value is None`.
- Do not compare to `True` or `False`: use `if flag:`.
- Empty check: `if not items:`, not `if len(items) == 0:`.
- Never use a bare `except:`.
- Comments explain **why**, not what. Remove commented-out code.

## 3. Docstrings (PEP 257)

A docstring is the first string in a module, function, class or method.

```python
def calculate_discount(price, discount_percent):
    """Return the price after applying a percentage discount.

    Args:
        price: Original price (must be 0 or more).
        discount_percent: Discount from 0 to 100.

    Returns:
        The final price as a float.

    Raises:
        ValueError: If price is negative or the discount is not 0-100.
    """
```

- First line: a short summary, imperative mood ("Return...", not "Returns..."), ends with a period.
- Describe inputs, result and errors. Do not just repeat the function name.
- Common styles: **Google** (used here), **NumPy**, **reStructuredText** (Sphinx).
- Read them with `help(function)` or `function.__doc__`.
- Examples written as `>>> code` followed by the output can be checked with `doctest.testmod()`.

## 4. Type Hints

```python
def find_age(ages: dict[str, int], name: str) -> int | None:
    return ages.get(name)
```

- They document what goes in and out, and help IDEs and tools.
- **Python does not enforce them.** `add_numbers("a", "b")` still runs. Use `mypy` or `pyright` to check them.
- `list[int]`, `dict[str, int]` need Python 3.9+. `int | None` needs 3.10+ (older code uses `Optional[int]` from `typing`).
- The hints are stored in `function.__annotations__`.

| Hint | Meaning |
|---|---|
| `int`, `str`, `float`, `bool` | simple types |
| `list[int]` | list of ints |
| `dict[str, int]` | keys are str, values are int |
| `tuple[int, str]` | fixed tuple |
| `int \| None` | an int, or None |
| `-> None` | the function returns nothing |

## 5. Logging

```python
import logging
logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(level=logging.INFO,
                        format="%(levelname)s | %(name)s | %(message)s")
```

| Level | Value | Use for |
|---|---|---|
| DEBUG | 10 | details while developing |
| INFO | 20 | normal progress |
| WARNING | 30 | something unexpected (default level) |
| ERROR | 40 | something failed |
| CRITICAL | 50 | the program may not continue |

- `print()` has no level, no time and cannot be switched off. Logging can.
- Configure logging **once** in the entry point (`main()`), not when a module is imported.
- Use `logger.exception("message")` inside an `except` block. It logs the message **and the traceback**. `logging.error(error)` loses the traceback.
- Use `logger.debug("value is %s", value)` (not an f-string) so the text is built only when the level is on.
- Catch the **specific** error (`ZeroDivisionError`), not `Exception`.

## 6. Assertions

```python
assert percentage <= 100, "bug: percentage out of range"
```

- `assert` checks something that must always be true **if your code is correct**.
- It is **removed** when Python runs with `-O` (`__debug__` becomes `False`).
- Never use `assert` to check user input or data from outside. Use `raise ValueError(...)`.
- Gotcha: `assert (condition, "message")` with parentheses is always true, because a non-empty tuple is true. Write `assert condition, "message"`.

| Use `raise` | Use `assert` |
|---|---|
| Bad input from a user, file or network | Impossible state caused by a bug in your own code |

## 7. Code Organization

- **One function, one job.** Load data, process it and print it in three functions.
- Functions that calculate should `return` a value. Keep `print` in `main()`.
- Constants at the top (`TAX_RATE`), no magic numbers in the middle of code.
- Avoid global variables that functions change.
- Do not repeat code (DRY). If you copy a block twice, make it a function.
- Keep functions short enough to read without scrolling.
- A real project has folders: `app/`, `services/`, `models/`, `utils/`, `tests/`. Each folder with an `__init__.py` is a package.

## 8. Refactoring

Refactoring = change the **structure** of code without changing its **behavior**.

Techniques:
- Rename (`weight` → `weight_kg`)
- Replace magic numbers with named constants
- **Guard clauses**: handle the bad case first with an early `return`, and remove nested `if`s
- Extract a function from a long block
- Replace repeated code with one function or one data table (`RATES`)

Always **prove** nothing changed: run the old and the new version on the same inputs and compare (the file does this with 8 cases). Real projects use automated tests for this.

## 9. Tools

| Tool | Does |
|---|---|
| `ruff format` / `black` | formats code automatically |
| `ruff check` / `flake8` / `pylint` | finds style problems and bugs |
| `mypy` / `pyright` | checks type hints |
| `pre-commit` | runs the checks before every commit |
| `pytest` + CI | runs your tests on every push |

## Quick Revision

- Names: `snake_case`, `PascalCase`, `UPPER_CASE`; never reuse built-ins.
- PEP 8: 4 spaces, 79 chars, two blank lines, `is None`, `if not items`.
- Docstring: summary + Args + Returns + Raises.
- Type hints: documentation, not enforcement.
- `logger.exception` in `except`; configure in `main()`.
- `raise` for input, `assert` for bugs.
- Small functions, named constants, guard clauses.
- Refactor only with a check that behavior is the same.