# Notes - Real World Python

## 1. The Menu Loop

Every project uses the same shape:

```python
def main():
    while True:
        print("\n1.Add\n2.View\n3.Exit")
        choice = input("Choice: ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            view_items()
        elif choice == "3":
            break
        else:
            print("Invalid Choice")
```

- `while True` repeats until `break`.
- `.strip()` removes accidental spaces.
- Always have an `else` for invalid choices.
- In the calculator, check the choice **before** asking for numbers, so a bad choice does not waste the user's time (`continue` goes back to the menu).

## 2. Input Validation

`input()` returns text, and `float("abc")` raises `ValueError`. Never trust user input.

```python
def ask_number(prompt, minimum=None, maximum=None):
    while True:
        try:
            number = float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            continue
        ...
        return number
```

Pattern: **loop until valid**, then `return`.

What to check:
- Not empty (`ask_text`)
- Is a number (`try / except ValueError`)
- Range (minimum, maximum), for example age 1-120, marks 0-100, amount at least 0.01
- Not `nan` or `inf` (`math.isfinite`)

## 3. CRUD

CRUD = **C**reate, **R**ead, **U**pdate, **D**elete. Most real applications are CRUD.

| Operation | Example function |
|---|---|
| Create | `add_student()` |
| Read | `view_students()`, `search_student()` |
| Update | `update_student()` |
| Delete | `delete_student()` |

## 4. A `find_` Helper Avoids Repeated Loops

```python
def find_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None
```

Search, update and delete all reuse it, and `add_student` uses it to refuse duplicate IDs.

## 5. Unique IDs

```python
if student_id in existing:        # dict
    print("ID already exists")
    return
```

Without this check, a second record with the same ID can overwrite or shadow the first (the old banking system silently replaced an account this way).

## 6. List vs Dictionary for Records

| Use | When |
|---|---|
| List of dicts | You mostly loop through everything, order matters |
| Dict keyed by ID | You mostly look up one record by its ID (O(1)) |

`accounts["101"]` is a direct lookup. `find_student("S1")` has to loop through the list.

## 7. Saving Data with JSON

```python
import json
from pathlib import Path

DATA_FILE = Path(__file__).with_name("students.json")

def load_data():
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Data file is damaged. Starting empty.")
    return []

def save_data():
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)
```

- `Path(__file__).with_name(...)` puts the file next to the script, no matter where you run it from.
- Call `save_data()` after **every** change.
- `load_data()` handles two cases: no file yet, and a damaged file.
- JSON keeps strings, numbers, booleans, lists and dicts. It turns `None` into `null` and `True` into `true`.

## 8. Helper Module (`helpers.py`)

Repeated code belongs in one place.

```python
from helpers import ask_text, ask_number, ask_int
```

If you fix a bug in `ask_number`, every project gets the fix. A script's own folder is on Python's import path, so `helpers.py` next to the project works.

## 9. Money and Floats

Floats cannot store values like 0.1 exactly. For learning projects they are fine, and `round(x, 2)` hides the tiny error when printing. Real systems use `decimal.Decimal` or store whole cents as integers.

## 10. State Changes (Library)

A book has a state: `issued` is `True` or `False`. Check the state before changing it.

```python
if book["issued"]:
    print("Book is already issued")
```

This stops impossible actions like issuing a book twice.

## 11. Files and Folders (File Organizer)

| Function | Does |
|---|---|
| `os.listdir(folder)` | Names inside a folder |
| `os.path.join(a, b)` | Builds a path for any operating system |
| `os.path.isfile(path)` / `isdir(path)` | Check what a path is |
| `os.makedirs(path, exist_ok=True)` | Create a folder (no error if it exists) |
| `shutil.move(src, dst)` | Move a file |

Safe habits for programs that change files:
1. Check the folder exists.
2. **Ask the user to confirm.**
3. Never overwrite: check `os.path.exists(new_path)` first.
4. Skip hidden files and sub-folders.
5. Handle files with no extension and different upper/lower case (`.JPG` vs `.jpg`).

## 12. Passwords

- `getpass.getpass("Password: ")` reads input without showing it on screen.
- Never print real passwords in a list (`********`).
- Never save passwords as plain text. Real tools encrypt them (for example `cryptography`) or use the operating system keychain (`keyring`).
- This project keeps them in memory only on purpose.

## 13. Normalizing Input

```python
name = ask_text("Name: ").title()     # "kalid" and "KALID" become "Kalid"
```

Without this, "kalid" and "Kalid" become two different contacts.

## Quick Revision

- Menu loop: `while True`, `if / elif / else`, `break`.
- Validate input in a loop until valid.
- CRUD = add, view, update, delete.
- Check for duplicates before adding.
- Save after every change; load at start.
- Share common code in a helper module.
- Passwords: hidden input, never plain-text storage.
- Programs that change files must ask first and never overwrite.