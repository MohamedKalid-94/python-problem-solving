# Phase 14 - Real World Python

## Overview

This phase puts everything from the earlier phases into ten small console projects. Each one is a menu-driven program with functions, input checking and, where it makes sense, data saved to a JSON file.

## What You Will Learn

- Build a menu-driven program with `while True` and `break`
- Split a program into small functions
- Check user input so the program never crashes
- Store records in lists and dictionaries
- Save and load data with `json` and `pathlib`
- Prevent duplicate IDs
- Share code between files with a helper module
- Work safely with files and folders (`os`, `shutil`)
- Handle sensitive data (passwords) responsibly

## Folder Structure

```
phase_14_real_world_python/
├── helpers.py
├── 01_calculator_project.py
├── 02_expense_tracker_project.py
├── 03_student_management_system.py
├── 04_banking_system.py
├── 05_inventory_system.py
├── 06_library_management_system.py
├── 07_file_organizer.py
├── 08_password_manager.py
├── 09_employee_management_system.py
├── 10_contact_book.py
├── README.md
├── notes.md
├── practice.md
└── interview_qanda.md
```

## Projects

| # | Project | Data Structure | Saved to file | Key Idea |
|---|---|---|---|---|
| 01 | Calculator | none | No | Menu loop, `ValueError` for divide by zero |
| 02 | Expense Tracker | list of dicts | `expenses.json` | Totals and category summary |
| 03 | Student Management | list of dicts | `students.json` | Full CRUD with a `find_student` helper |
| 04 | Banking System | dict of dicts | `accounts.json` | Amount validation, no duplicate accounts |
| 05 | Inventory System | dict of dicts | `inventory.json` | Stock update and delete |
| 06 | Library Management | list of dicts | `books.json` | State change (available / issued) |
| 07 | File Organizer | files | No | `os`, `shutil`, never overwrite, ask first |
| 08 | Password Manager | dict of dicts | No (on purpose) | `getpass`, hidden passwords |
| 09 | Employee Management | list of dicts | `employees.json` | CRUD with unique IDs |
| 10 | Contact Book | dict of dicts | `contacts.json` | Phone and email validation |

## `helpers.py`

| Function | Does |
|---|---|
| `ask_text(prompt)` | Asks until the user types a non-empty value |
| `ask_number(prompt, minimum, maximum)` | Asks until the user types a valid number in range |
| `ask_int(prompt, minimum, maximum)` | Same, for whole numbers |

## How to Run

Keep `helpers.py` in the same folder as the projects.

```
cd code/phase_14_real_world_python
python 02_expense_tracker_project.py
```

## Notes

- Data files (`expenses.json`, `students.json`, ...) are created in this folder the first time you save. Add `code/phase_14_real_world_python/*.json` to `.gitignore`.
- `07_file_organizer.py` moves real files. Test it on a copy of a folder, never on a folder with your code.
- `08_password_manager.py` keeps passwords in memory only. Never store real passwords in a plain text file.
- Money uses floats here for learning. Real systems use `Decimal` or whole cents.

## Skills After This Phase

- Build a complete console application from scratch
- Validate every user input
- Save and load data with JSON
- Organize repeated code in a module
- Choose list vs dictionary for the records
- Think about what can go wrong (duplicates, empty data, bad input)