# Interview Questions & Answers - Real World Python

## Beginner

### 1. What does `while True` do in a menu program?
It repeats forever until a `break` runs. The menu keeps showing until the user chooses Exit.

### 2. Why do we use `.strip()` on user input?
It removes accidental leading and trailing spaces, so `" 1 "` matches `"1"`.

### 3. Why does `float(input())` crash on `abc`?
`input()` returns text and `float("abc")` raises `ValueError`. Wrap it in `try / except ValueError` and ask again.

### 4. What is CRUD?
Create, Read, Update, Delete: the four basic operations of most applications.

### 5. When do you use a list and when a dictionary for records?
A list of dicts is good when you loop through everything. A dictionary keyed by ID is good when you look up one record by its ID, because lookup is O(1).

### 6. What does `if __name__ == "__main__":` do?
It runs `main()` only when the file is executed directly, not when it is imported.

### 7. Why is it good to have an `else` branch in a menu?
It handles invalid choices, so the program tells the user instead of silently doing nothing.

## Intermediate

### 8. How do you stop duplicate IDs?
Check before adding: `if student_id in existing: print("ID already exists"); return`. Without it, a new record can overwrite the old one.

### 9. Why write a `find_student()` helper?
Search, update, delete and the duplicate check all need the same loop. One helper removes the repetition and keeps the logic in one place.

### 10. How do you save data in a Python program?
Use `json.dump(data, file, indent=4)` to write and `json.load(file)` to read. Call the save function after every change so no data is lost.

### 11. Why use `Path(__file__).with_name("data.json")`?
It puts the data file next to the script, so the program works no matter which folder you run it from. A plain `"data.json"` is relative to the current folder.

### 12. What can go wrong when loading a JSON file?
The file may not exist (first run) or may be damaged (`json.JSONDecodeError`). `load_data()` handles both and starts with empty data.

### 13. Why create `helpers.py` instead of copying the input functions into every file?
One copy means one place to fix bugs and less code. This is the DRY principle (Don't Repeat Yourself).

### 14. Why should `deposit` reject negative amounts?
A negative deposit would reduce the balance and a negative withdrawal would increase it. Every input that changes money must be validated.

### 15. Why check the state before issuing a library book?
Without the check you can issue a book that is already issued, or return a book that was never issued. State checks prevent impossible actions.

### 16. What does `.title()` do for names and categories?
It normalizes the text (`"kalid"` → `"Kalid"`), so the same person or category is not stored twice with different spelling.

## Advanced

### 17. Why is the password manager not saving to a file?
Saving passwords in plain text is a serious security problem. A real program encrypts them (for example `cryptography.fernet`) or uses the operating system keychain (`keyring`).

### 18. What does `getpass.getpass()` do?
It reads input without echoing it on screen, so nobody can read the password over your shoulder. It is still plain text in memory.

### 19. Why does the file organizer ask for confirmation and refuse to overwrite?
It changes real files and cannot be undone. Safe programs confirm first, check that the target exists before moving, and skip anything unexpected.

### 20. What bug does the old file organizer have for a file named `README`?
`"README".split(".")[-1]` returns `"README"`, which becomes the folder name. A file with that name already exists, so `os.makedirs` raises `FileExistsError`. The fix uses a fixed folder name (`no_extension_files`) and a suffix (`_files`).

### 21. Why are floats risky for money?
Floats cannot represent values like `0.1` exactly (`0.1 + 0.2` is `0.30000000000000004`). Use `decimal.Decimal` or store whole cents as integers.

### 22. How would you make a bank transfer safe?
Check both accounts and the balance first, then subtract and add together, then save once. If anything fails before saving, nothing has changed. In a database this is a transaction.

### 23. What is the difference between `os.path` and `pathlib`?
Both work with paths. `os.path` uses functions on strings. `pathlib.Path` uses objects with methods (`path.exists()`, `path / "file.txt"`) and is the modern style.

### 24. Why does `math.isfinite` appear in `ask_number`?
`float("nan")` and `float("inf")` are valid floats. Without the check, a user could enter `nan` as an amount and it would pass every comparison.

### 25. How would you test these programs?
Move the logic into functions that take values and return results (the way phase 15 does), and keep `input()` and `print()` in `main()`. Then you can test the functions with `pytest` without typing anything.

### 26. How would you turn one of these projects into a class-based design?
Create an `Account` class (name, balance, `deposit`, `withdraw`) and a `Bank` class that holds the accounts dictionary, with `save` and `load` methods. The menu code stays outside the classes.

## Practical Tasks

1. Add input validation to a function that reads an age.
2. Write `load_data()` and `save_data()` for a list of records.
3. Add duplicate ID protection to an "add" function.
4. Explain why the old banking system could lose a customer's money.
5. Make a file-moving program safe (confirm, never overwrite, handle no extension).
6. Suggest how to store passwords safely.