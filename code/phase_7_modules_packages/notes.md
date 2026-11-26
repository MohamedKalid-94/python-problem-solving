# Python Modules & Packages Notes

## 1. Introduction

Modules and packages help organize Python code into reusable and maintainable components.

They are essential for:

- Backend development
- Automation projects
- Data science projects
- AI/GenAI applications


Basic idea:


Large Application
|
↓
Small Reusable Modules
|
↓
Packages

---

# 2. Module

## Definition

A module is a single Python file (`.py`) containing reusable code.

A module can contain:

- Functions
- Classes
- Variables
- Constants


Example:


calculator.py

Content:

```python
def add(a, b):
    return a + b

Import:
import calculator


Usage:
calculator.add(10,20)


3. Types of Modules
1. Built-in Modules
Provided by Python.

Examples:
math
os
datetime
json
random
pathlib
logging

Example:
import mathprint(math.sqrt(25))


2. Custom Modules
Created by developers.

Example:
project/

main.py
calculator.py

calculator.py:
def add(a,b):    return a+b


main.py:
from calculator import add


3. Third Party Modules
Installed using pip.

Examples:
requests
numpy
pandas
fastapi
langchain

Installation:
pip install requests

4. Import Statement
Import Complete Module
import math


Usage:
math.sqrt(16)


Import Specific Function
from math import sqrt


Usage:
sqrt(16)


Import With Alias
import datetime as dt


Usage:
dt.datetime.now()


Benefits:
- Shorter code
- Better readability
5. Module Search Process
When importing:
import module_name

Python searches:
1. Current directory

2. Standard library

3. Installed packages

4. PYTHONPATH

6. Package
Definition
A package is a folder containing multiple Python modules.

Example:
utils/

├── __init__.py
├── math_utils.py
└── string_utils.py

Purpose:
- Organize related modules
- Manage large applications
- Improve code structure
7. init.py
__init__.py initializes a package.

Example:
utils/

├── __init__.py
├── helper.py

Responsibilities:
- Mark directory as package
- Package initialization
- Control exports
8. Package Import
Example:

Structure:
project/

main.py

utils/

├── __init__.py
└── math_utils.py

Import:
from utils.math_utils import add


9. name Variable
__name__ is a special Python variable.

When file runs directly:
__name__ == "__main__"


When imported:
__name__ == "module_name"


10. main Pattern
Professional Python programs use:
def main():    print("Application Started")if __name__ == "__main__":    main()


Benefits:
- Prevent unwanted execution
- Create clean entry point
- Support importing
11. pip Package Manager
Definition
pip is Python's package management tool.

Used for:
- Installing packages
- Removing packages
- Updating packages
Install Package
pip install package_name

Example:
pip install requests

Remove Package
pip uninstall package_name

Check Packages
pip list

Package Information
pip show package_name

Upgrade Package
pip install --upgrade package_name

12. Virtual Environment
Definition
A virtual environment creates an isolated Python environment for a project.

Without venv:
System Python

Package A
Package B
Package C

Problem:

Version conflicts

With venv:
Project A

venv
 |
 Packages


Project B

venv
 |
 Different Packages

13. Creating Virtual Environment
Command:
python -m venv venv

Creates:
project/

├── venv/
├── app.py

14. Activating Virtual Environment
Windows
venv\Scripts\activate

Linux/Mac
source venv/bin/activate

15. Deactivate Environment
Command:
deactivate

16. requirements.txt
Definition
A file containing all project dependencies.

Example:
requirements.txt

Content:
fastapi==0.115.0
requests==2.32.3
numpy==2.1.0

17. Creating requirements.txt
Command:
pip freeze > requirements.txt

Flow:
Installed Packages

        ↓

pip freeze

        ↓

requirements.txt

18. Installing Requirements
Command:
pip install -r requirements.txt

Used when:
- Setting up another machine
- Deployment
- Team collaboration
19. Real Project Structure
Professional Python application:
application/

├── main.py

├── config/

│   └── settings.py

├── services/

│   └── user_service.py

├── utils/

│   └── helpers.py

├── models/

│   └── user.py

└── requirements.txt

20. AI/GenAI Project Structure
Example:
rag_application/

├── main.py

├── loaders/

│   └── pdf_loader.py

├── embeddings/

│   └── embedding_model.py

├── vector_store/

│   └── database.py

├── agents/

│   └── workflow.py

├── utils/

│   └── text_processing.py

└── requirements.txt

21. Module vs Package
Module	Package
Single .py file	Folder containing modules
Small reusable code	Large application organization
Easy import	Structured imports


22. Professional Development Workflow
Create Project

        ↓

Create venv

        ↓

Install Packages

        ↓

Write Modules

        ↓

Organize Packages

        ↓

Create requirements.txt

        ↓

Push to GitHub

        ↓

Deploy

23. Best Practices
Do:
✅ Keep modules small
✅ Use meaningful names
✅ Separate responsibilities
✅ Maintain requirements.txt
✅ Use virtual environments  
Avoid:
❌ One huge Python file
❌ Installing everything globally
❌ Duplicate code
❌ Poor folder organization  
24. Interview Quick Revision
Remember:
Module
↓
Single Python file


Package
↓
Collection of modules


pip
↓
Package manager


venv
↓
Isolated environmen