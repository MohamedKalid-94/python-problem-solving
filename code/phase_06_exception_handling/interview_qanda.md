interview_qanda.md content:
# Python Exception Handling Interview Q&A

## 1. What is an exception?

An exception is a runtime error that interrupts the normal flow of a program.

Example:

```python
10 / 0

Output:
ZeroDivisionError

2. Why do we use exception handling?
Exception handling prevents application crashes and allows the program to handle errors gracefully.

Benefits:
- Prevent program termination
- Show meaningful messages
- Debug failures
- Improve reliability
3. What are the keywords used in exception handling?
Python provides:
- try
- except
- else
- finally
- raise
4. Explain try and except.
try contains risky code.

except handles errors.

Example:
try:    result = 10 / 0except ZeroDivisionError:    print("Cannot divide by zero")


5. Difference between error and exception?
Error:
- Usually serious problem
- Program may stop
Exception:
- Runtime problem
- Can be handled using try-except
6. What happens if an exception is not handled?
The program stops and Python displays a traceback message.
7. What is the purpose of finally?
finally always executes whether an exception occurs or not.

Used for:
- Closing files
- Releasing resources
- Database cleanup
Example:
try:    file.open()finally:    file.close()


8. What is else block in exception handling?
else executes only when no exception occurs.

Example:
try:    result = 10 / 2except:    print("Error")else:    print("Success")


9. Difference between else and finally?
else:
- Runs only on success
finally:
- Always runs
10. What is raise keyword?
raise is used to manually create an exception.

Example:
if age < 0:    raise ValueError("Invalid age")


11. Why do we create custom exceptions?
Custom exceptions make errors more meaningful and easier to understand.

Example:
class InvalidUserError(Exception):    pass


12. What are multiple exceptions?
Handling different errors separately.

Example:
try:    value = int(data)except ValueError:    passexcept TypeError:    pass


13. Can we handle multiple exceptions in one except block?
Yes.

Example:
except (ValueError, TypeError):    pass


14. Common built-in exceptions?
Frequently used:
- ValueError
- TypeError
- FileNotFoundError
- ZeroDivisionError
- KeyError
- IndexError
- PermissionError
15. Difference between ValueError and TypeError?
ValueError:

Correct type but invalid value.

Example:
int("abc")


TypeError:

Wrong data type.

Example:
"Python" + 10


16. How do you handle file errors?
Using try-except.

Example:
try:    open("file.txt")except FileNotFoundError:    print("File missing")


17. What is logging?
Logging records application events and errors for monitoring and debugging.
18. Difference between print and logging?
print:
- Temporary debugging
logging:
- Production monitoring
- Stores history
- Has severity levels
19. Logging levels in Python?
Levels:
1. DEBUG
2. INFO
3. WARNING
4. ERROR
5. CRITICAL
20. How do you log exceptions?
Use:
logging.exception()


It stores error details with traceback.
21. How do you handle API failures?
Common approach:
- Use try-except
- Validate response
- Handle timeout
- Retry failed requests
- Log errors
22. How do you handle large file processing errors?
Approach:
- Process line by line
- Catch file errors
- Log failures
- Continue processing valid data
23. How do you design exception handling in production?
Follow:
Input Validation
        |
Try Operation
        |
Catch Specific Errors
        |
Log Failure
        |
Return Meaningful Response

24. How is exception handling used in AI systems?
Examples:
- Invalid document upload
- Embedding failures
- LLM API failures
- Vector database errors
- Parsing failures
25. How do you handle RAG pipeline failures?
Handle:
- File loading errors
- Empty documents
- Chunking failures
- Embedding API errors
- Vector database failures
- LLM response errors
26. What is the best practice for exception handling?
Best practices:
- Catch specific exceptions
- Avoid empty except blocks
- Log errors
- Create meaningful messages
- Do not hide unexpected failures
27. Difference between Exception and BaseException?
BaseException is the parent class.

Exception handles normal application errors.

Most applications use:
Exception


28. How do you retry failed operations?
Use:
- Loop based retry
- Exponential backoff
- Maximum retry limit
Example:
Attempt 1
   |
Fail
   |
Attempt 2
   |
Success

29. How do you validate user input?
Steps:
Receive Input
      |
Check Format
      |
Validate Rules
      |
Raise Exception
      |
Process Data

30. Explain exception handling flow.
Flow:
try
 |
Error?
 |
 +---- No ---> else
 |
 Yes
 |
except
 |
finally