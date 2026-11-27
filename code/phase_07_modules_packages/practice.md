# Python Modules & Packages Practice Problems

## Level 1 — Import Basics


## 1. Math Module Calculator

Problem:

Create a calculator using Python built-in `math` module.

Requirements:

- Import math module
- Calculate square root
- Calculate power
- Calculate factorial


Example:

Input:


Number = 25

Output:


Square Root = 5


---

## 2. Date Time Application

Problem:

Create a program that displays:

- Current date
- Current time
- Current year
- Current month


Use:

```python
datetime

3. Random Password Generator
Problem:

Create a password generator.

Requirements:
- Use random module
- Generate random characters
- Create 8 character password
Example:
Password: A8kP91xz

4. File Path Analyzer
Problem:

Create a program to analyze file paths.

Use:
pathlib


Display:
- File name
- Extension
- Parent directory
Level 2 — Custom Modules
5. Create Calculator Module
Create:
calculator.py

Functions:
add()subtract()multiply()divide()


Import into:
main.py

Expected:
10 + 5 = 15

6. Student Management Module
Create:
student.py

Functions:
- add_student()
- calculate_average()
- display_student()
Use from:
main.py

7. Employee Utility Module
Create:
employee_utils.py

Functions:
- calculate_salary()
- calculate_bonus()
- display_employee()
Level 3 — Package Structure
8. Create Utility Package
Create:
utils/

├── __init__.py
├── math_utils.py
└── string_utils.py

math_utils.py:

Create:
- add()
- multiply()
- average()
string_utils.py:

Create:
- clean_text()
- word_count()
Import into:
main.py

9. Create AI Utility Package
Create:
ai_utils/

├── __init__.py
├── text_cleaner.py
├── chunking.py
└── embedding_utils.py

Functions:

text_cleaner:
- clean_text()
chunking:
- split_text()
embedding_utils:
- create_embedding()
Level 4 — name and main
10. Create Application Entry Point
Create:
app.py

Requirements:

Create:
main()


Execute only:
if __name__ == "__main__":


Output:
Application Started

11. Import Execution Test
Create:
module_a.py
main.py

module_a.py:

Print message when imported.

Observe:
- Direct execution
- Import execution
Level 5 — pip Practice
12. Package Installation Practice
Install:
requests

Commands:
pip install requests

Verify:
pip list

13. Package Information
Find details about:
requests

Use:
pip show requests

Find:
- Version
- Location
- Dependencies
14. Package Upgrade Practice
Upgrade a package.

Command:
pip install --upgrade package_name

Level 6 — Virtual Environment
15. Create Project Environment
Create:
python_project/

Steps:
1. Create venv
2. Activate environment
3. Install package
4. Run program
16. Compare Global vs venv Packages
Check:
pip list

Inside venv:
pip list

Observe differences.
17. Multiple Project Environment
Create:

Project A:
django environment

Project B:
fastapi environment

Use separate virtual environments.
Level 7 — requirements.txt
18. Create requirements.txt
Install:
requests
pandas
numpy

Generate:
pip freeze > requirements.txt

19. Install From requirements.txt
Create new environment.

Install:
pip install -r requirements.txt

Verify packages.
20. Dependency Management Practice
Create project:
my_project/

├── app.py
├── requirements.txt
└── README.md

Prepare for GitHub.
Level 8 — Real World Problems
21. Backend Project Structure
Design:
backend/

├── main.py
├── config/
├── services/
├── models/
├── utils/
└── requirements.txt

Explain purpose of each folder.
22. AI Document Processing Structure
Create:
document_ai/

├── main.py
├── loaders/
├── processors/
├── embeddings/
├── vector_db/
├── utils/
└── requirements.txt

Implement module separation.
23. Configuration Management
Create:
config/

└── settings.py

Store:
- Application name
- Version
- Database URL
- API settings
Import into main application.
24. Build Mini Package
Create:
calculator_package/

├── __init__.py
├── operations.py
└── formatter.py

Features:
- Mathematical operations
- Result formatting
Level 9 — Interview Problem Solving
25. Debug Import Error
Problem:
ModuleNotFoundError

Find possible causes:
- Wrong file name
- Wrong path
- Missing package
- Wrong import statement
26. Fix Circular Import
Scenario:
module_a imports module_b

module_b imports module_a

Find solution.
27. Design Production Folder Structure
Create structure for:
FastAPI + AI Application

Include:
- API
- Services
- Database
- Models
- Utils
- Config
28. Dependency Conflict Problem
Scenario:

Project A needs:
numpy 1.x

Project B needs:
numpy 2.x

Solution:

Use:
Virtual environments

Final Practice Goal
After completing these problems:

✅ Understand Python imports
✅ Create reusable modules
✅ Build packages
✅ Use pip professionally
✅ Manage virtual environments
✅ Handle dependencies
✅ Structure real-world Python projects
✅ Prepare for FastAPI and GenAI projects