# Python Collections Module - Practice Exercises

Topics:

- Counter
- defaultdict
- deque
- namedtuple

Goal:

Practice collections module patterns used in
Python development, AI engineering, and interviews.

---

# Level 1 - Counter Basics

---

## 1. Count Elements in a List

Input:

```python
numbers = [
    10,
    20,
    10,
    30,
    20,
    10
]

Expected Output:
10 -> 3
20 -> 2
30 -> 1

Task:

Use Counter to find frequency.
2. Character Frequency
Input:
text = "python programming"


Find:
- Most common character
- Least common character
3. Word Frequency Analyzer
Input:
Python is powerful.
Python is easy.
Python is popular.

Find:
- Word frequency
- Top 3 words
4. Find First Non-Repeating Character
Input:
text = "aabbcdde"


Expected:
c

Hint:

Use Counter.
5. Find Most Sold Product
Input:
products = ["Laptop","Phone","Laptop","Mouse","Laptop","Phone"]


Output:
Laptop

Level 2 - defaultdict Practice
6. Group Numbers by Even and Odd
Input:
numbers = [1,2,3,4,5,6]


Expected:
{"even":[2,4,6],"odd":[1,3,5]}


Use:
defaultdict(list)


7. Group Students by Department
Input:
students = [("Alice","AI"),("Bob","Web"),("Chris","AI"),("David","Data")]


Expected:
{"AI":["Alice","Chris"]}


8. Count Word Occurrences
Input:
words = ["python","java","python","sql"]


Use:
defaultdict(int)


9. Group Files by Extension
Input:
files = ["app.py","main.py","index.html","style.css"]


Expected:
{".py":["app.py","main.py"]}


10. Build Nested Dictionary
Create:
companydepartmentemployeeskills


Example:
company["AI"]["Backend"]=["Python","LangChain"]


Use:
nested defaultdict


Level 3 - deque Practice
11. Implement Queue
Create:
Customer Queue

Operations:
- Add customer
- Serve customer
- Display queue
Use:
deque


12. Implement Stack
Create:
Browser Back Button

Operations:
- Visit page
- Go back
Use:
append()pop()


13. Reverse String
Input:
text = "Python"


Expected:
nohtyP

Use:
deque


14. Sliding Window
Input:
numbers = [1,2,3,4,5,6]


Window size:
3

Output:
1 2 3
2 3 4
3 4 5
4 5 6

15. Recent Search History
Create:
Maximum history = 5

When new search comes:

Remove oldest automatically.

Use:
deque(maxlen=5)


Level 4 - namedtuple Practice
16. Employee Record
Create:
Employee


Fields:
id
name
department
salary

Create 5 employees.
17. Student Database
Create:
Student


Fields:
name
age
course

Display:
All students in Python course

18. API Response Object
Create:
Response


Fields:
status
message
data

Example:
Response(200,"Success",{})


19. Convert namedtuple to Dictionary
Use:
_asdict()


20. Update namedtuple
Use:
_replace()


Change:
employee salary

Level 5 - Real World Mini Projects
Project 1: Log Analyzer
Build:
Log Analyzer System

Input:
INFO
ERROR
WARNING
ERROR
INFO

Output:
ERROR : 2
INFO  : 2
WARNING :1

Use:
Counter

Project 2: E-Commerce Analytics
Input:

Orders:
Laptop
Phone
Laptop
Mouse

Generate:
- Most sold product
- Product count
- Category count
Use:
Counter
defaultdict

Project 3: Student Management
Features:
- Add students
- Group by department
- Count students
- Display records
Use:
defaultdict
namedtuple
Counter

Project 4: Task Scheduler
Features:
- Add tasks
- Process tasks
- Maintain recent tasks
Use:
deque

Project 5: Browser History
Features:
- Visit website
- Back button
- Maximum history limit
Use:
deque(maxlen)

Interview Coding Challenges
Challenge 1
Find duplicate elements in a list.

Input:
[1,2,3,2,4,1]


Expected:
1,2

Challenge 2
Find top 3 most frequent numbers.

Input:
[1,1,2,2,2,3,4]


Expected:
2,1,3

Challenge 3
Group anagrams.

Input:
["eat","tea","tan","ate"]


Expected:
[
["eat","tea","ate"],
["tan"]
]

Hint:

Use:
defaultdict(list)
Counter

Challenge 4
Implement LRU Cache.

Requirements:
- Store recent items
- Remove oldest item
Use:
deque(maxlen)

Challenge 5
Perform BFS traversal of graph.

Input:
graph = {"A":["B","C"],"B":["D"],"C":["E"]}


Use:
deque

Practice Checklist
Counter
- [ ] Frequency counting
- [ ] Top K elements
- [ ] Duplicate detection
- [ ] Word analyzer
defaultdict
- [ ] Grouping
- [ ] Counting
- [ ] Nested structures
deque
- [ ] Queue
- [ ] Stack
- [ ] Sliding window
- [ ] BFS
namedtuple
- [ ] Data records
- [ ] API objects
- [ ] Database rows
Completion Criteria
Before moving forward:

✅ Solve Level 1
✅ Solve Level 2
✅ Solve Level 3
✅ Solve Level 4
✅ Complete at least 3 mini projects
✅ Solve interview challenges  