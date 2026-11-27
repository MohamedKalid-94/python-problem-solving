# Python File Handling Practice Problems

## Level 1 — Basic File Operations

## 1. Create and Write File

Problem:

Create a file named `student.txt`.

Write:


Name: Kalid
Skill: Python
Goal: AI Engineer

Requirements:

- Create file
- Write content
- Read and display content


---

## 2. Read File Line by Line

Problem:

Read a file and print each line with line number.

Input:


Python
AI
RAG

Expected Output:


1. Python
2. AI
3. RAG


---

## 3. Count Lines in File

Problem:

Count total lines in a text file.

Input:


Python
Machine Learning
Deep Learning

Output:


Total Lines: 3


---

# Level 2 — Text Processing Problems


## 4. Count Word Frequency

Problem:

Read a file and count each word frequency.

Input:


python ai python rag

Output:

```python
{
    "python": 2,
    "ai": 1,
    "rag": 1
}

Concepts:
- File reading
- split()
- Dictionary
- Counter
5. Search Word in File
Problem:

Search whether a word exists in a file.

Input:
Search Word: AI

Output:
AI Found

6. Replace Text in File
Problem:

Replace a word in an existing file.

Input:
Python is powerful

Replace:
Python -> Python Programming

Output:
Python Programming is powerful

7. Remove Empty Lines
Problem:

Clean a file by removing empty lines.

Input:
Python

AI

RAG

Output:
Python
AI
RAG

Level 3 — Append and Logging Problems
8. Application Logger
Problem:

Create an application log system.

Every execution should append:
2026-11-26 User Login
2026-11-26 File Uploaded

Requirements:
- Use append mode
- Preserve old logs
9. Error Log Analyzer
Input:
INFO Server Started
ERROR Database Failed
WARNING Memory High
ERROR API Timeout

Output:
{    "INFO": 1,    "ERROR": 2,    "WARNING": 1}


Concepts:
- File reading
- String processing
- Dictionary
Level 4 — CSV Problems
10. Employee CSV Analyzer
Input:

employees.csv
name,role,salary
Alice,Developer,90000
Bob,Tester,50000
Chris,Developer,80000

Find:
- Average salary
- Highest salary employee
- Developer count
11. CSV Data Cleaning
Remove:
- Empty rows
- Invalid emails
- Duplicate records
Input:
Alice,alice@gmail.com
,
Bob,bob@gmail.com
Alice,alice@gmail.com

Output:
Clean CSV file

12. CSV to JSON Converter
Problem:

Convert:
employees.csv

to:
employees.json

Flow:
CSV
 |
Read
 |
Process
 |
JSON Output

Level 5 — JSON Problems
13. User Profile Manager
Input:
{
    "name":"Kalid",
    "skills":[
        "Python",
        "AI"
    ]
}

Operations:
- Add skill
- Remove skill
- Update profile
14. API Response Analyzer
Input:
{
    "users":[
        {
            "id":1,
            "active":true
        },
        {
            "id":2,
            "active":false
        }
    ]
}

Find:
Active Users

15. Configuration Manager
Create:
config.json

Store:
{
    "model":"LLM",
    "temperature":0.2
}

Operations:
- Read config
- Update values
- Save changes
Level 6 — Pathlib Problems
16. Project File Scanner
Given a project folder:

Find:
- Python file count
- JSON file count
- CSV file count
17. Large File Finder
Find files larger than:
1 MB

Output:
filename
size

18. Duplicate File Detector
Find duplicate files using:
- File content
- Hash comparison
Concepts:
- pathlib
- hashlib
Level 7 — Real World AI Problems
19. Document Loader
Input:
documents/

doc1.txt
doc2.txt
doc3.txt

Pipeline:
Read Files
      |
Clean Text
      |
Create Chunks
      |
Save Metadata JSON

Output:
[
    {
        "file":"doc1.txt",
        "chunks":5
    }
]

20. RAG Knowledge Base Preparation
Build:
Documents
      |
      ↓
Read Files
      |
      ↓
Extract Text
      |
      ↓
Chunk Data
      |
      ↓
Store Metadata

Output:
[
    {
        "file":"ai.txt",
        "chunk_id":1,
        "text":"AI content"
    }
]

Interview Practice Challenges
21. Large File Processing
How will you process a 10GB file without loading everything into memory?
22. Safe File Update
How will you prevent data loss while updating a file?
23. Production Logging
How will you design a logging system for an application?
24. Document Ingestion Pipeline
Design a pipeline:
Upload File
     |
Validate
     |
Extract Text
     |
Chunk
     |
Store Metadata

25. RAG File Pipeline
Design:
PDF/TXT Files
       |
       ↓
Loader
       |
       ↓
Text Splitter
       |
       ↓
Embeddings
       |
       ↓
Vector Database
