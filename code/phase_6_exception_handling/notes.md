# Python Exception Handling Notes

## 1. Exception Handling Overview

Exception handling is a mechanism to handle runtime errors without stopping program execution.

Example problems:

- Invalid user input
- File not found
- Database failure
- API failure
- Invalid data processing


Basic flow:


Program Execution
|
↓
Error Occurs
|
↓
Exception Handling
|
↓
Continue / Recover


---

# 2. Exception vs Error

## Error

A serious problem that usually stops program execution.

Examples:

- SyntaxError
- IndentationError


## Exception

A runtime problem that can be handled.

Examples:

- ValueError
- TypeError
- FileNotFoundError
- ZeroDivisionError


---

# 3. try Block

`try` contains code that may generate an exception.

Example:

```python
try:
    result = 10 / 2

Purpose:
- Execute risky operations
- Monitor failures
4. except Block
except handles exceptions.

Example:
try:    number = int(value)except ValueError:    print("Invalid number")


Benefits:
- Prevent application crash
- Provide meaningful messages
5. Common Built-in Exceptions
ValueError
Wrong value format.

Example:
int("python")


TypeError
Wrong data type operation.

Example:
"Python" + 10


ZeroDivisionError
Division by zero.

Example:
10 / 0


FileNotFoundError
File does not exist.

Example:
open("missing.txt")


KeyError
Dictionary key missing.

Example:
user["age"]


IndexError
List index does not exist.

Example:
items[10]


6. Multiple Exception Handling
Two approaches:
Separate except blocks
try:    operation()except ValueError:    passexcept TypeError:    pass


Single except block
except (ValueError, TypeError):    pass


Use separate blocks when different handling is required.
7. else Block
else runs only when no exception occurs.

Structure:
try:    operation()except:    handle_error()else:    success()


Use cases:
- Successful calculations
- Valid file processing
- API success handling
8. finally Block
finally always executes.

Example:
try:    file.read()finally:    file.close()


Used for:
- Closing files
- Database cleanup
- Releasing resources
9. Exception Flow
try
 |
 |
Error?
 |
 +----------------+
 |                |
No               Yes
 |                |
else           except
 |
 |
finally

10. raise Keyword
raise creates an exception manually.

Example:
if age < 0:    raise ValueError("Invalid age")


Used for:
- Input validation
- Business rules
- Custom validation
11. Custom Exceptions
Custom exceptions create meaningful application errors.

Example:
class InvalidUserError(Exception):    pass


Usage:
raise InvalidUserError(    "User not valid")


Common custom exceptions:
- AuthenticationError
- PaymentError
- InvalidDocumentError
- InsufficientBalanceError
12. Logging
Logging records application events and failures.

Import:
import logging


Example:
logging.error(    "Database failed")


13. Logging Levels
Level	Purpose
DEBUG	Detailed debugging
INFO	Normal events
WARNING	Possible problems
ERROR	Application failures
CRITICAL	Serious failures


14. Exception Logging
Use:
logging.exception(    "Operation failed")


Advantages:
- Stores traceback
- Helps debugging
- Useful in production
15. File Handling Exception Pattern
Open File
    |
Try Reading
    |
Success?
    |
+-----------+
|           |
Yes         No
|           |
Process   Handle Error

Common errors:
- FileNotFoundError
- PermissionError
16. API Exception Handling Pattern
Send Request
      |
Validate Response
      |
Success?
      |
+-------------+
|             |
Yes           No
|             |
Process     Retry / Log

Handle:
- Timeout
- Connection error
- Invalid response
- Authentication failure
17. Database Exception Pattern
Production flow:
Connect Database
        |
Execute Query
        |
Commit
        |
Close Connection

Handle:
- Connection failure
- Query failure
- Transaction rollback
18. AI / GenAI Exception Handling
RAG pipeline:
Upload Document
        |
Validate File
        |
Extract Text
        |
Create Chunks
        |
Generate Embeddings
        |
Store Vector
        |
LLM Response

Possible failures:
- Invalid file
- Empty document
- Parser failure
- Embedding API error
- Vector DB failure
- LLM timeout
19. Best Practices
Do:
- Catch specific exceptions
- Use meaningful error messages
- Log failures
- Validate inputs
- Use custom exceptions
Avoid:
- Empty except blocks
- Catching all exceptions unnecessarily
- Hiding errors
- Using exceptions for normal logic
20. Production Error Handling Pattern
Input
 |
Validation
 |
Business Logic
 |
Exception Handling
 |
Logging
 |
Response

21. Problem Solving Checklist
When handling a problem:
1. Identify possible failure points
2. Choose correct exception type
3. Add try-except
4. Add validation
5. Log failures
6. Return useful message
22. Interview Key Points
Remember:
- try → risky code
- except → error handling
- else → successful execution
- finally → cleanup
- raise → manual exception
- custom exception → business errors
- logging → production monitoring