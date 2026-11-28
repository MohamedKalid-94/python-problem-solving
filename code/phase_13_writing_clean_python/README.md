# Phase 13 - Writing Clean Python

## Overview

Code is read many more times than it is written. This phase teaches the habits that make Python code easy to read, check and change. Every file shows **BAD** code and **CLEAN** code side by side, and both can be run so you can compare the output.

## What You Will Learn

- Naming: variables, functions, classes, constants, booleans, underscores
- PEP 8 style: spacing, line length, blank lines, comparisons
- Docstrings: summary, Args, Returns, Raises, examples, doctest
- Type hints and what they do (and do not do)
- Logging instead of `print()`
- Assertions vs input validation
- Organizing code into small single-purpose functions
- Refactoring safely by proving the behavior did not change

## Folder Structure

```
phase_13_writing_clean_python/
├── helpers.py
├── 01_naming_conventions_complete.py
├── 02_pep8_style_guide_complete.py
├── 03_docstrings_complete.py
├── 04_type_hints_complete.py
├── 05_logging_complete.py
├── 06_assertions_complete.py
├── 07_code_organization_complete.py
├── 08_refactoring_complete.py
├── README.md
├── notes.md
├── practice.md
└── interview_qanda.md
```

## Files

| File | BAD example | CLEAN example |
|---|---|---|
| 01 Naming | `bad_calc(a, b, c)`, a variable named `max` | `calculate_total_price(price, quantity, tax)` |
| 02 PEP 8 | one-line `def`, `== True`, `== None`, `len(x) == 0` | spacing, `is None`, `not items` |
| 03 Docstrings | `"""Calculate discount."""` | Google-style docstring with a doctest |
| 04 Type hints | `bad_add(a, b)` | `add_numbers(a: int, b: int) -> int` |
| 05 Logging | `print()` and a broad `except Exception` | `logger`, levels, `logger.exception` |
| 06 Assertions | `assert` used to check input | `raise ValueError` for input, `assert` for bugs |
| 07 Organization | one function that does everything | `parse_order`, `load_orders`, `calculate_total`, `format_report` |
| 08 Refactoring | nested ifs, magic numbers, repeated code | guard clause, constants, one rate table |

## How to Run

Keep `helpers.py` in the same folder.

```
cd code/phase_13_writing_clean_python
python 05_logging_complete.py
```

Try this experiment (assertions are switched off, and the BAD code behaves differently):

```
python -O 06_assertions_complete.py
```

Requirements: Python 3.10 or newer (file 04 uses `int | None`).

## Tools That Check Style For You

```
pip install ruff mypy
ruff format .          # fixes formatting automatically
ruff check .           # finds style problems and bugs
mypy .                 # checks type hints
```

The BAD functions in this phase carry `# noqa` so the checker ignores them on purpose.

## Skills After This Phase

- Write readable, consistently styled Python
- Choose clear names and write useful docstrings
- Use type hints and know their limits
- Use `logging` correctly
- Choose between `assert` and `raise`
- Split code into small functions
- Refactor with confidence by comparing old and new behavior