# Python File Handling Notes

## 1. File Handling Overview

File handling allows Python programs to store, read, update, and process data from files.

Common operations:

- Create files
- Read files
- Write files
- Append data
- Update content
- Process structured data
- Manage folders and paths


## 2. Opening Files

Syntax:

```python
open(filename, mode)

Example:
file = open("data.txt", "r")


Recommended:
with open("data.txt", "r") as file:    content = file.read()


Benefits:
- Automatically closes file
- Prevents resource leaks
- Handles exceptions safely
3. File Modes
Mode	Description
r	Read existing file
w	Write new content, overwrite existing
a	Append new content
x	Create new file
rb	Read binary file
wb	Write binary file


4. Reading Files
read()
Reads complete file content.
content = file.read()


readline()
Reads one line.
line = file.readline()


readlines()
Reads all lines as a list.
lines = file.readlines()


5. Writing Files
write():
file.write("Hello Python")


Important:

w mode removes previous content.

Example:
with open("data.txt", "w") as file:    file.write("New Data")


6. Append Operations
Append mode:
with open("log.txt", "a") as file:    file.write("New Log")


Used for:
- Application logs
- User history
- Audit records
- Transaction history
7. Word Frequency Problem
Common pattern:
Read File
    |
Split Words
    |
Count Frequency
    |
Dictionary Output

Tools:
collections.Counter


8. Text Processing Operations
Common problems:
- Search text
- Replace text
- Count words
- Remove empty lines
- Clean unwanted characters
Example:
content.replace("old", "new")


9. Log File Processing
Log format:
INFO Server Started
ERROR Database Failed
WARNING Memory High

Processing:
Read Lines
     |
Identify Log Level
     |
Count Messages
     |
Generate Report

10. CSV Processing
CSV:

Comma Separated Values

Used for:
- Datasets
- Reports
- Data exchange
Import:
import csv


Reader:
csv.reader()


Dictionary Reader:
csv.DictReader()


Writer:
csv.writer()


Dict Writer:
csv.DictWriter()


11. CSV Processing Workflow
CSV File
   |
Read Data
   |
Validate Data
   |
Clean Records
   |
Analyze
   |
Generate Output

12. JSON Processing
JSON:

JavaScript Object Notation

Used for:
- API communication
- Configuration files
- Metadata storage
Import:
import json


Write JSON:
json.dump()


Read JSON:
json.load()


Convert Python object to JSON string:
json.dumps()


Convert JSON string to Python object:
json.loads()


13. Serialization and Deserialization
Serialization:
Python Object
      |
      ↓
JSON

Deserialization:
JSON
 |
 ↓
Python Object

14. Context Manager
Context manager manages resources automatically.

Example:
with open("file.txt") as file:    data = file.read()


Internally:
__enter__()
    |
Execute Code
    |
__exit__()

Benefits:
- Automatic cleanup
- Exception safety
- Resource management
15. Custom Context Manager
Structure:
class Manager:    def __enter__(self):        pass    def __exit__(self):        pass


Used in:
- Database connections
- Logging
- API sessions
- File operations
16. Pathlib
Modern file path handling.

Import:
from pathlib import Path


Common methods:
Path.exists()Path.mkdir()Path.read_text()Path.write_text()Path.glob()Path.rglob()Path.unlink()


17. File Searching
Example:
Path(".").glob("*.py")


Recursive:
Path(".").rglob("*.py")


18. File Metadata
Get information:
file.namefile.suffixfile.stat().st_size


19. Real-World File Processing Pattern
Input Files
     |
     ↓
Validation
     |
     ↓
Reading
     |
     ↓
Processing
     |
     ↓
Transformation
     |
     ↓
Output File

20. AI / GenAI File Handling Usage
File handling is the first step in AI pipelines.

Example RAG workflow:
PDF/TXT Files
       |
       ↓
Read Documents
       |
       ↓
Extract Text
       |
       ↓
Clean Content
       |
       ↓
Chunk Text
       |
       ↓
Create Embeddings
       |
       ↓
Vector Database

21. Best Practices
- Always use with statement
- Validate file existence
- Handle exceptions
- Avoid loading huge files completely
- Use pathlib for paths
- Separate input and output folders
- Keep logs for failures
22. Large File Processing
Bad approach:
content = file.read()


Loads everything into memory.

Better:
for line in file:    process(line)


Processes one line at a time.
23. Exception Handling
Common errors:
- FileNotFoundError
- PermissionError
- IsADirectoryError
- JSONDecodeError
Example:
try:    file.read()except FileNotFoundError:    print("File missing")


24. Complexity
Reading file:
Time Complexity: O(n)
Space Complexity: O(n)

Line-by-line processing:
Time Complexity: O(n)
Space Complexity: O(1)

25. File Handling in Production Systems
Used in:
- Backend applications
- Data pipelines
- Machine learning workflows
- RAG systems
- Document management systems
- Logging systems