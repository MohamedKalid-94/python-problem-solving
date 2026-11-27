# Python Comprehensions - Practice Problems

## Phase 4 Practice Goal

The goal of these exercises is to improve:

- Pythonic coding style
- Data transformation skills
- Filtering logic
- Problem-solving ability
- AI/data processing patterns

---

# Level 1 — Basic List Comprehension

## 1. Create a list from 1 to 10

### Task

Create a list containing numbers from 1 to 10 using list comprehension.

Expected output:

```text
[1,2,3,4,5,6,7,8,9,10]
```

---

## 2. Create squares

### Task

Create a list of squares from 1 to 10.

Example:

```python
[1,4,9,16,25]
```

---

## 3. Convert numbers to strings

Input:

```python
numbers = [1,2,3,4,5]
```

Expected:

```python
["1","2","3","4","5"]
```

---

## 4. Extract characters from string

Input:

```python
word = "Python"
```

Expected:

```text
['P','y','t','h','o','n']
```

---

# Level 2 — Filtering Using Conditions

## 5. Find even numbers

Input:

```python
numbers = range(1,50)
```

Return only even numbers.

---

## 6. Find numbers divisible by 5

Input:

```python
numbers = range(1,100)
```

Output:

```text
[5,10,15,...]
```

---

## 7. Remove negative numbers

Input:

```python
numbers = [-5,10,-2,20,30,-1]
```

Expected:

```text
[10,20,30]
```

---

## 8. Remove empty strings

Input:

```python
names = [
    "Alice",
    "",
    "Bob",
    "",
    "Chris"
]
```

Expected:

```text
["Alice","Bob","Chris"]
```

---

# Level 3 — If-Else Comprehension

## 9. Even or Odd classification

Input:

```python
numbers = range(1,10)
```

Expected:

```text
[
"Odd",
"Even",
...
]
```

---

## 10. Pass or Fail system

Input:

```python
marks = [90,40,75,30]
```

Condition:

- >= 50 → Pass
- < 50 → Fail

Expected:

```text
["Pass","Fail","Pass","Fail"]
```

---

## 11. Temperature converter

Input:

```python
temperatures = [0,10,20,30]
```

Convert Celsius to Fahrenheit.

Formula:

```
F = (C * 9/5) + 32
```

---

# Level 4 — Dictionary Comprehension

## 12. Create square dictionary

Expected:

```python
{
1:1,
2:4,
3:9,
4:16
}
```

---

## 13. Create dictionary from two lists

Input:

```python
keys = [
"name",
"role",
"experience"
]

values = [
"Kalid",
"AI Engineer",
8
]
```

Expected:

```python
{
"name":"Kalid",
"role":"AI Engineer",
"experience":8
}
```

---

## 14. Filter dictionary values

Input:

```python
scores = {
"Alice":90,
"Bob":40,
"Chris":80
}
```

Return only scores >= 50.

---

## 15. Swap dictionary keys and values

Input:

```python
data = {
"Python":1,
"AI":2
}
```

Expected:

```python
{
1:"Python",
2:"AI"
}
```

---

# Level 5 — Set Comprehension

## 16. Remove duplicates

Input:

```python
numbers = [
1,2,2,3,4,4,5
]
```

Expected:

```text
{1,2,3,4,5}
```

---

## 17. Extract unique characters

Input:

```python
word = "programming"
```

Return unique characters.

---

## 18. Extract unique file extensions

Input:

```python
files = [
"app.py",
"data.csv",
"test.py",
"image.png"
]
```

Expected:

```text
{
"py",
"csv",
"png"
}
```

---

# Level 6 — Nested Comprehension

## 19. Flatten a matrix

Input:

```python
matrix = [
[1,2],
[3,4],
[5,6]
]
```

Expected:

```text
[1,2,3,4,5,6]
```

---

## 20. Create multiplication table

Create a 5x5 multiplication matrix.

Expected:

```text
[
[1,2,3,4,5],
[2,4,6,8,10],
...
]
```

---

## 21. Generate combinations

Input:

```python
colors = [
"Red",
"Blue"
]

sizes = [
"S",
"M",
"L"
]
```

Expected:

```text
[
("Red","S"),
("Red","M"),
("Red","L"),
...
]
```

---

# Level 7 — Real-World Data Processing

## 22. Process User Data

Input:

```python
users = [
{
"name":"Alice",
"active":True
},
{
"name":"Bob",
"active":False
}
]
```

Extract active users.

Expected:

```text
["Alice"]
```

---

## 23. Extract API Response Data

Input:

```python
response = [
{
"id":1,
"name":"Python"
},
{
"id":2,
"name":"AI"
}
]
```

Create:

```python
{
1:"Python",
2:"AI"
}
```

---

## 24. Process Documents

Input:

```python
documents = [
{
"id":1,
"text":"Python tutorial"
},
{
"id":2,
"text":"AI"
},
{
"id":3,
"text":"RAG system"
}
]
```

Extract documents where text length > 5.

---

# Level 8 — AI/GenAI Practice

## 25. RAG Chunk Filtering

Input:

```python
chunks = [
"short",
"Python is a programming language",
"AI"
]
```

Keep chunks with length > 10.

---

## 26. Extract Document Metadata

Input:

```python
documents = [
{
"id":"doc1",
"topic":"Python"
},
{
"id":"doc2",
"topic":"AI"
}
]
```

Create:

```python
{
"doc1":"Python",
"doc2":"AI"
}
```

---

## 27. Token Cleaning

Input:

```python
sentence = "Python AI LLM RAG"
```

Convert all tokens to lowercase.

Expected:

```text
["python","ai","llm","rag"]
```

---

## 28. Remove Duplicate Tokens

Input:

```python
tokens = [
"ai",
"python",
"ai",
"rag"
]
```

Expected:

```text
{
"ai",
"python",
"rag"
}
```

---

# Interview Challenge Problems

## 29. Find Common Elements

Input:

```python
list1 = [1,2,3,4]
list2 = [3,4,5,6]
```

Expected:

```text
[3,4]
```

---

## 30. Find Words Longer Than 5 Characters

Input:

```python
sentence = "Python programming language is powerful"
```

Expected:

```text
[
"Python",
"programming",
"language",
"powerful"
]
```

---

# Final Challenge

Build a mini data pipeline:

Input:

```python
documents = [
{
"id":1,
"title":"Python",
"length":500
},
{
"id":2,
"title":"AI",
"length":50
},
{
"id":3,
"title":"RAG",
"length":700
}
]
```

Tasks:

1. Filter documents where length > 200
2. Extract titles
3. Create id → title dictionary
4. Create unique title set

Expected concepts:

✅ List comprehension  
✅ Dictionary comprehension  
✅ Set comprehension  
✅ Conditional filtering  

---

# Practice Completion Checklist

```
List comprehension              ☐
Dictionary comprehension        ☐
Set comprehension               ☐
Nested comprehension            ☐
Conditional comprehension       ☐
AI data processing examples     ☐
Interview problems              ☐
```