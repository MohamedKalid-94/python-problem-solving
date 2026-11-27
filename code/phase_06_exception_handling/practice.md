# Python Exception Handling Practice Problems

## Level 1 — Basic Exception Handling


## 1. Division Calculator

Problem:

Create a calculator that divides two numbers.

Requirements:

- Handle division by zero
- Handle invalid input
- Display meaningful error messages


Example:

Input:


10 / 2

Output:


Result: 5


Error Case:


10 / 0

Output:


Cannot divide by zero


---

## 2. User Age Validator

Problem:

Validate user age.

Rules:

- Age should be integer
- Age should not be negative
- Age should be above 18


Use:

- try
- except
- raise


---

## 3. Number Conversion

Problem:

Convert user input into integer.

Input:


"100"

Output:


100


Error:


"Python"

Handle:


ValueError


---

# Level 2 — Multiple Exception Problems


## 4. Safe List Access

Problem:

Access an element from a list.

Example:

```python
numbers = [10,20,30]

Handle:
- IndexError
- TypeError
5. Dictionary Data Reader
Problem:

Read user information.

Example:
user = {"name":"Kalid","role":"AI Engineer"}


Handle missing keys.

Exception:
KeyError

6. File Reader
Problem:

Read a file.

Handle:
- FileNotFoundError
- PermissionError
Flow:
Check File
    |
Read File
    |
Process Data

Level 3 — Else and Finally Problems
7. File Processing System
Create a file processing program.

Requirements:

Use:
- try
- except
- else
- finally
Flow:
Open File
    |
Read Content
    |
Success Message
    |
Close File

8. Database Connection Simulation
Simulate:
Connect Database
        |
Execute Query
        |
Close Connection

Use:
- finally for cleanup
9. API Request Simulation
Create fake API response.

Handle:
- Success response
- Failed response
- Cleanup process
Level 4 — Raise Keyword Problems
10. Password Validator
Rules:

Password must:
- Have minimum 8 characters
- Contain number
- Contain special character
Raise:
ValueError

11. Bank Withdrawal System
Rules:
- Withdrawal amount should be positive
- Amount should not exceed balance
Raise:
InsufficientBalanceError

12. Student Marks Validation
Rules:

Marks:
0 <= marks <= 100

Invalid:
-10
150

Use raise keyword.
Level 5 — Custom Exception Problems
13. Create Custom User Exception
Create:
InvalidUserError

Validate:
- Username
- Email
- Password
14. Payment System
Create:
PaymentFailedError

Handle:
- Invalid card
- Insufficient balance
- Payment timeout
15. Authentication System
Create:
AuthenticationError

Validate:
- Username
- Password
Level 6 — Logging Problems
16. Application Logger
Create logging system.

Store:
Application started
User logged in
File uploaded
Error occurred

Use:
logging module

17. Error Log Analyzer
Input:
INFO Server Started
ERROR Database Failed
WARNING Memory High
ERROR API Timeout

Output:
{"INFO":1,"ERROR":2,"WARNING":1}


18. Exception Logger
Create program that:
- Generates error
- Catches exception
- Stores error in log file
Level 7 — Real World Problem Solving
19. File Upload System
Design:
User Upload
      |
Validate File
      |
Check Size
      |
Save File
      |
Generate Response

Handle:
- Invalid file
- Large file
- Permission issue
20. Employee Registration System
Requirements:

Validate:
- Name
- Email
- Age
- Salary
Use:
- Custom exceptions
- Logging
21. API Data Processing Pipeline
Design:
API Request
      |
Receive Response
      |
Validate Data
      |
Process Data
      |
Return Result

Handle:
- Connection error
- Invalid response
- Timeout
Level 8 — AI / GenAI Exception Problems
22. Document Upload Validation
Create validation system.

Check:
- File exists
- File type
- File size
- Empty content
Raise:
InvalidDocumentError

23. RAG Pipeline Error Handling
Design:
PDF Upload
     |
Text Extraction
     |
Chunking
     |
Embedding
     |
Vector Storage
     |
LLM Response

Handle failures:
- PDF parsing error
- Empty chunks
- Embedding failure
- Vector database error
24. LLM API Failure Handler
Handle:
- API timeout
- Rate limit
- Invalid API key
- Server error
Add:
- Logging
- Retry mechanism
Interview Practice Challenges
25. Explain Exception Handling Flow
Draw:
try
 |
Error?
 |
except
 |
else
 |
finally

26. Design Production Error Handling
Create architecture:
Application
      |
Validation
      |
Exception Handler
      |
Logger
      |
Monitoring System

27. Debug This Code
Find the issue:
try:    result = 10 / 0except:    pass


Improve it using best practices.
28. Build Retry Logic
Create retry system:
Attempt 1
   |
Failure
   |
Attempt 2
   |
Success

Requirements:
- Maximum retries
- Logging
- Error handling
Final Interview Goal
After completing these problems, you should be able to:

✅ Handle runtime failures
✅ Design safe Python programs
✅ Create custom exceptions
✅ Implement logging
✅ Debug production issues
✅ Handle AI pipeline failures