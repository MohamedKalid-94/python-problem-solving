# Phase 13 — Writing Clean Python Notes

## Overview

Clean Python means writing code that is:

- Readable
- Maintainable
- Testable
- Scalable
- Easy for teams to understand

Professional developers focus not only on making code work, but also on making code easy to improve.

---

# 1. Naming Conventions

Good naming improves code readability.

## Variables

Use:


snake_case

Example:

```python
user_name = "Kalid"
total_amount = 5000

Avoid:
x = 5000


because the purpose is unclear.
Functions
Functions should describe actions.

Use:
calculate_total_price()load_customer_data()generate_response()


Avoid:
calc()process()do_task()


Classes
Use:
PascalCase

Example:
class UserProfile:    pass


Examples:
CustomerAccount
DocumentLoader
RAGPipeline

Constants
Use:
UPPER_CASE

Example:
MAX_RETRY_COUNT = 3API_TIMEOUT = 30


Private Variables
Use:
_single_underscore

Example:
_internal_cache = {}


Meaning:

Used internally inside the module/class.
2. PEP 8 Style Guide
PEP 8 is Python's official coding style guide.

It improves:
- Code consistency
- Readability
- Team collaboration
Indentation
Use 4 spaces.

Correct:
if user_exists:    print("Welcome")


Line Length
Keep code readable.

Avoid very long lines.

Break complex statements into multiple lines.
Imports
Organize imports:
1. Standard libraries
2. Third-party libraries
3. Local modules
Example:
import osimport jsonimport pandasfrom utils import helper


Blank Lines
Use blank lines between:
- Functions
- Classes
- Logical sections
3. Docstrings
Docstrings explain what code does.

Example:
def calculate_sum(a,b):    """    Calculate sum of two numbers.    """


Docstring Contains
- Function purpose
- Parameters
- Return values
- Usage information
Benefits
- Better documentation
- Easier maintenance
- IDE support
- API documentation
4. Type Hints
Type hints specify expected data types.

Without type hints:
def add(a,b):    return a+b


Problem:

Developer does not know input types.
With type hints:
def add(a:int,b:int)->int:    return a+b


Common Type Hints
String:
name: str


Integer:
age: int


Float:
price: float


List:
names: list[str]


Dictionary:
scores: dict[str,int]


Benefits
- Better readability
- IDE suggestions
- Early error detection
- Easier team development
5. Logging
Logging is used for production monitoring.

Avoid:
print("Error")


Production applications use:
logging.error("Error")


Logging Levels
DEBUG
INFO
WARNING
ERROR
CRITICAL

Examples
INFO:

Application started.

WARNING:

Something unusual happened.

ERROR:

Application failure.

CRITICAL:

System-level problem.
AI Engineering Logging Example
RAG Pipeline:
User Query Received

↓

Documents Retrieved

↓

LLM Response Generated

↓

Evaluation Completed

Logs help track:
- Query failures
- Retrieval issues
- LLM errors
- Performance problems
6. Assertions
Assertions check assumptions.

Example:
assert age >= 0


If the condition fails:
AssertionError

Used For
- Finding bugs early
- Validating developer assumptions
- Checking internal logic
Assertion Example
def divide(a,b):    assert b != 0    return a/b


Assertion vs Exception
Assertion:

Developer mistake.

Example:
assert model_loaded


Exception:

Runtime/user problem.

Example:
raise FileNotFoundError


7. Code Organization
Large projects should be divided into modules.

Bad structure:
project/

main.py
utils.py
database.py
model.py

Everything becomes difficult to maintain.
Professional Structure
project/

app/

services/

models/

utils/

tests/

config/

AI Project Example
RAG System:
rag_project/

ingestion/

loader.py
splitter.py


retrieval/

vector_store.py
retriever.py


generation/

llm.py


evaluation/

metrics.py

Benefits
- Better maintenance
- Easy debugging
- Reusable components
- Team collaboration
8. Refactoring
Refactoring means improving code without changing functionality.

Goal:

Make code:
- Cleaner
- Faster to understand
- Easier to maintain
Common Refactoring Techniques
1. Rename Variables
Before:
x = 100


After:
total_amount = 100


2. Split Large Functions
Before:
100 lines function

After:
load_data()

process_data()

save_result()

3. Remove Duplicate Code
Bad:

Same logic repeated everywhere.

Better:

Create reusable functions.
4. Improve Error Handling
Bad:
except:    pass


Better:
except ValueError as error:    logging.error(error)


Clean Python Checklist
Naming
✅ Meaningful names
✅ snake_case variables
✅ PascalCase classes
✅ UPPER_CASE constants  
Style
✅ Follow PEP 8
✅ Proper indentation
✅ Organized imports  
Documentation
✅ Add docstrings
✅ Add type hints  
Production Quality
✅ Use logging
✅ Handle errors
✅ Validate assumptions  
Maintainability
✅ Small functions
✅ No duplicate code
✅ Clear project structure  
AI Engineer Connection
Production AI applications require clean Python.

Example:
API

↓

Authentication

↓

Data Processing

↓

Retriever

↓

Vector Database

↓

LLM

↓

Evaluation

↓

Monitoring

Without clean code:
- Debugging becomes difficult
- Scaling becomes difficult
- Team collaboration becomes difficult
With clean code:
- Faster development
- Better reliability
- Easier deployment