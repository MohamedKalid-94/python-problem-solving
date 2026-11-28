# Practice - Real World Python

Run each project, try to break it with bad input, then do the exercises.

## Try to Break It

1. In project 02, enter `abc`, `-5`, `0` and `nan` as the amount. What happens each time?
2. In project 03, enter a letter as the age, an age of `0`, and marks of `150`.
3. In project 04, create the same account number twice. What happens to the first account now?
4. In project 06, issue the same book twice, then return a book that was never issued.
5. In project 07, try a folder that does not exist, answer `n` to the question, and run it twice on the same folder.
6. In project 10, enter a phone number with letters and an email without `@`.

## Exercises per Project

### 01 Calculator
7. Add a `power(a, b)` and a `modulus(a, b)` option.
8. Keep a history list of the last 5 results and add a "show history" option.
9. Add a "use last result" option so the user does not retype it.

### 02 Expense Tracker
10. Add a `delete_expense()` option.
11. Add a date to each expense (use `datetime.date.today()`).
12. Add a "most expensive category" option.
13. Add a monthly total option.

### 03 Student Management
14. Add `update_student()` for name, age and course (not only marks).
15. Add a `top_student()` function.
16. Add `average_marks()` and a grade letter (A, B, C, F).
17. Sort the students by marks in `view_students()`.

### 04 Banking
18. Add `transfer(from_acc, to_acc, amount)` that never loses money (if the second step fails, undo the first).
19. Keep a transaction history for each account.
20. Add a minimum balance rule.
21. Store the balance in whole cents (integer) instead of a float. What changes?

### 05 Inventory
22. Add a "low stock" report (quantity below 5).
23. Add `total_inventory_value()` (price × quantity for every product).
24. Add an "update price" option.

### 06 Library
25. Add a `delete_book()` option.
26. Store who borrowed the book and the date.
27. Add a "search by title or author" option.
28. List only available books.

### 07 File Organizer
29. Add an undo: record every move and move the files back.
30. Add a "dry run" mode that only prints what would move.
31. Rewrite `organize_files` using `pathlib.Path` instead of `os.path`.
32. Group by type (images, documents, videos) instead of by extension.

### 08 Password Manager
33. Add a `generate_password(length)` function using the `secrets` module.
34. Add a password strength check (length, digits, symbols).
35. Save the passwords **encrypted** with `cryptography.fernet`.
36. Add a master password that must be entered before using the program.

### 09 Employee Management
37. Add `update_employee()` for salary and department.
38. Add a "total salary by department" report.
39. Add "highest paid employee".

### 10 Contact Book
40. Add `update_contact()`.
41. Add a "search by part of a name" option (for example `ka` finds `Kalid`).
42. Export all contacts to a CSV file.
43. Import contacts from a CSV file and skip duplicates.

## Code Reading

44. Why is `find_student` a separate function? List the places it is used.
45. What does `Path(__file__).with_name("students.json")` do, and why is it better than just `"students.json"`?
46. Why is `save_data()` called after every change and not only when exiting?
47. Why does `load_data()` have a `try / except json.JSONDecodeError`?
48. Why does `get_folder_name` add `_files` to the folder name?

## Challenge Projects

49. Combine projects 03 and 09 into one "People Manager" that shares the helpers.
50. Convert the Banking System to use classes (`Account`, `Bank`).
51. Write a small to-do list app with priorities, due dates and a JSON file.
52. Write a quiz game that reads questions from a JSON file and tracks the high score.