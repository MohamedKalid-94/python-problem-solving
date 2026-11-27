# Python Modules & Packages Interview Q&A

## 1. What is a module in Python?

A module is a Python file that contains reusable code such as:

- Functions
- Classes
- Variables
- Statements

Example:


calculator.py

Import:

```python
import calculator

2. Why do we use modules?
Modules help to:
- Reuse code
- Organize large programs
- Improve maintainability
- Avoid duplicate code
3. What is a package in Python?
A package is a collection of related Python modules organized inside a directory.

Example:
utils/

├── __init__.py
├── math_utils.py
└── string_utils.py

4. Difference between module and package?
Module	Package
Single Python file	Collection of modules
.py file	Directory
Small reusable code	Large project organization


5. How do you import a module?
Example:
import mathprint(math.sqrt(25))


6. How do you import specific functions?
Example:
from math import sqrtprint(sqrt(25))


7. What is module aliasing?
Giving a module another name.

Example:
import datetime as dtprint(dt.datetime.now())


Benefits:
- Shorter code
- Better readability
8. What happens when Python imports a module?
Python:
1. Searches module location
2. Loads module code
3. Executes module code
4. Creates module object
9. What is init.py?
__init__.py identifies a directory as a Python package.

Used for:
- Package initialization
- Controlling imports
- Package metadata
Example:
utils/

├── __init__.py
└── helper.py

10. What is name in Python?
__name__ is a special built-in variable.

When a file runs directly:
__name__ == "__main__"


When imported:
__name__ == "module_name"


11. Why do we use if name == "main"?
It prevents code execution when the file is imported.

Example:
def main():    print("Application Started")if __name__ == "__main__":    main()


Used in:
- Scripts
- Applications
- Libraries
12. What is pip?
pip is Python's package manager.

Used to:
- Install packages
- Remove packages
- Upgrade packages
Example:
pip install requests

13. How do you check installed packages?
Command:
pip list

14. How do you uninstall a package?
Command:
pip uninstall package_name

15. How do you upgrade a package?
Command:
pip install --upgrade package_name

16. What is a virtual environment?
A virtual environment creates an isolated Python environment for a project.

Benefits:
- Dependency isolation
- Avoid version conflicts
- Project separation
17. How do you create a virtual environment?
Command:
python -m venv venv

18. How do you activate virtual environment?
Windows:
venv\Scripts\activate

Linux/Mac:
source venv/bin/activate

19. How do you deactivate virtual environment?
Command:
deactivate

20. Why do we use virtual environments?
Example:

Project A:
Django 4.0

Project B:
Django 5.0

Both projects can run independently.
21. What is requirements.txt?
A file that stores project dependencies.

Example:
fastapi==0.115.0
requests==2.32.3
numpy==2.1.0

22. How to create requirements.txt?
Command:
pip freeze > requirements.txt

23. How to install dependencies from requirements.txt?
Command:
pip install -r requirements.txt

24. Difference between pip and requirements.txt?
pip:
- Installs packages
requirements.txt:
- Stores package list
25. How are modules used in real projects?
Example:
application/

├── main.py
├── database/
├── services/
├── models/
├── utils/
└── config/

Each folder contains reusable modules.
26. How are packages useful in AI projects?
Example:
RAG Application

├── loaders/
│   └── pdf_loader.py
│
├── embeddings/
│   └── embedding.py
│
├── vector_store/
│   └── database.py
│
└── utils/
    └── text_processing.py

27. How do you handle project dependencies in a team?
Workflow:
Developer
    |
Create venv
    |
Install packages
    |
pip freeze
    |
requirements.txt
    |
GitHub
    |
Team member installs dependencies

28. Difference between global and virtual environment packages?
Global:
- Installed for entire system
Virtual environment:
- Installed only for one project
29. What are common Python standard library modules?
Examples:
- math
- datetime
- os
- pathlib
- json
- random
- logging
30. How do modules improve software design?
Modules provide:
- Separation of concerns
- Reusability
- Easy testing
- Better maintenance
- Clean architecture
Interview Key Points
Remember:
- Module → Single Python file
- Package → Collection of modules
- pip → Package installer
- venv → Isolated environment
- requirements.txt → Dependency list
- name → Module execution identifier
- main → Direct execution entry point