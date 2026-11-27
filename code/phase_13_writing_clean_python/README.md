# Phase 13 — Writing Clean Python Practice

## Objective

Practice writing Python code using professional standards:

- Meaningful naming
- PEP 8 style
- Documentation
- Type hints
- Logging
- Assertions
- Code organization
- Refactoring

---

# 1. Naming Conventions Practice

## Problem 1: Improve Variable Names

### Bad Code

```python
x = "Kalid"
y = 50000
z = True

Task
Convert into meaningful variable names.

Expected:
user_name = "Kalid"monthly_salary = 50000is_active = True


Problem 2: Function Naming
Bad Code
def calc(a,b):    return a+b


Task
Rename the function using Python convention.

Expected:
def calculate_total_amount(a,b):    return a+b


Problem 3: Class Naming
Bad Code
class userprofile:    pass


Task
Convert into PascalCase.

Expected:
class UserProfile:    pass


2. PEP 8 Practice
Problem 4: Fix Indentation
Bad Code
def greet():print("Hello")


Task
Follow PEP 8.

Expected:
def greet():    print("Hello")


Problem 5: Organize Imports
Arrange imports correctly.

Given:
from utils import helperimport pandasimport osimport json


Expected:
import osimport jsonimport pandasfrom utils import helper


3. Docstring Practice
Problem 6: Add Function Documentation
Given:
def calculate_discount(price,discount):    return price-discount


Add:
- Function purpose
- Parameters
- Return value
Expected:
def calculate_discount(price,discount):    """    Calculate final price after discount.    Args:        price: Original price        discount: Discount amount    Returns:        Final price    """


4. Type Hint Practice
Problem 7: Add Type Hints
Before:
def multiply(a,b):    return a*b


Convert to:
def multiply(a:int,b:int)->int:    return a*b


Problem 8: List Type Hint
Add type hints:
def get_names():    return ["AI","Python"]


Expected:
def get_names()->list[str]:    return ["AI","Python"]


5. Logging Practice
Problem 9: Replace Print With Logging
Before:
print("Database connected")


Convert:
logging.info("Database connected")


Problem 10: Error Logging
Create error handling:
try:    result = 10/0except Exception as error:    logging.error(error)


6. Assertion Practice
Problem 11: Validate Input
Create validation:
def withdraw(amount):    pass


Requirement:

Amount should always be positive.

Expected:
assert amount > 0


Problem 12: Validate Model
AI Example:
model = None


Add assertion:
assert model is not None


7. Code Organization Practice
Problem 13: Create Project Structure
Create:
ai_project/

├── app/
├── services/
├── models/
├── utils/
└── tests/

Problem 14: RAG Project Organization
Create:
rag_system/

├── ingestion/
│
├── retrieval/
│
├── generation/
│
├── evaluation/
│
└── config/

8. Refactoring Practice
Problem 15: Improve Function
Before:
def process(a,b,c):    x=a*b    y=x+c    return y


Task:

Improve:
- Variable names
- Readability
- Function name
Expected:
def calculate_total_price(price,quantity,tax):    subtotal = price * quantity    return subtotal + tax


Problem 16: Remove Duplicate Code
Before:
print("Loading data")print("Loading data")print("Loading data")


Task:

Create reusable function.

Expected:
def load_message():    print("Loading data")


9. Real-World AI Engineering Practice
Problem 17: Clean RAG Function
Bad:
def rag(q):    pass


Improve:
def generate_rag_response(user_query:str)->str:    pass


Problem 18: Add Logging to AI Pipeline
Create logs:
Query received

Documents retrieved

LLM response generated

Evaluation completed

Problem 19: Add Type Hints to AI Components
Example:
def retrieve_documents(query):    pass


Improve:
def retrieve_documents(query:str)->list[str]:    pass


Problem 20: Refactor AI Pipeline
Before:
main.py

500 lines

Refactor:
project/

api/

retrieval/

generation/

evaluation/

utils/

Final Challenge
Build a small clean Python project:
clean_python_project/

├── main.py
├── config.py
├── logger.py
├── services/
│
├── models/
│
├── utils/
│
└── tests/

Requirements:

✅ Meaningful names
✅ Type hints
✅ Docstrings
✅ Logging
✅ Assertions
✅ Modular design