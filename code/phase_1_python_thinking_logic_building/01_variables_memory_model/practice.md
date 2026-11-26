# Phase 1 Practice - Variables & Memory Model

## Step 1 - Variables

### Beginner Level

### 1. Student Information

Create variables to store:

- Student name
- Age
- Course
- College name

Display all details.

---

### 2. Employee Details

Store:

- Employee name
- Employee ID
- Department
- Salary

Print employee information.

---

### 3. Rectangle Calculation

Create variables:

- Length
- Width

Calculate:

- Area
- Perimeter


Formula:

Area = Length × Width

Perimeter = 2 × (Length + Width)


---

### 4. Circle Calculation

Store radius and calculate:

- Area
- Circumference


---

# Step 2 - Object References

## Practice

### 5. Predict Output

What will be the output?

```python
numbers = [1,2,3]

copy = numbers

copy.append(4)

print(numbers)

Explain why.
6. Shopping Cart
Create a shopping cart list.

Assign it to another variable.

Add a new product using the second variable.

Observe the result.
7. Team Members
Create:
team = ["John", "David"]


Create another reference.

Add a new member.

Check both variables.
Step 3 - Assignment
Practice
8. Swap Values
Swap:
a = 100b = 200


Expected:
a = 200
b = 100

9. Multiple Assignment
Assign values:
nameagecity


in a single statement.
10. Tuple Unpacking
Given:
student = ("Kalid",28,"Python")


Extract values into variables.
11. Variable Reassignment
Create a variable:
salary = 50000

Update it three times.
Step 4 - Dynamic Typing
12. Change Data Type
Create a variable:
value = 100


Change it into:
- String
- Float
- Boolean
13. Type Checking
Find the type of:
10
10.5
"Python"
True

14. Type Conversion
Convert:

String → Integer

Integer → String

Float → Integer
Step 5 - Mutable vs Immutable
15. List Modification
Create a list.

Add:
- Item
- Remove item
- Update item
Observe the change.
16. String Modification
Try changing:
name = "Python"


Explain what happens.
17. Tuple Modification
Try changing:
numbers = (1,2,3)


Explain the error.
18. Dictionary Update
Create employee dictionary.

Update salary value.
19. Copy vs Reference
Create:
list1 = [1,2,3]


Create:
- Reference
- Copy
Modify both and compare.
Step 6 - Memory Concepts
20. Same Reference
Create two variables pointing to same list.

Modify one.

Observe.
21. Copy Memory
Create a copy of a list.

Modify copy.

Check original.
22. Integer Memory
Assign:
a = 100b = a


Change b.

Observe.
23. String Memory
Assign:
x = "Python"y = x


Modify y.

Observe.
Step 7 - Object Identity
24. Using id()
Print id of:
- Integer
- String
- List
25. == vs is
Compare:
list1 = [1,2,3]list2 = [1,2,3]


Check:
list1 == list2

list1 is list2

Step 8 - Garbage Collection
26. Delete Variable
Create a variable.

Delete using:
del


Observe.
27. Reference Count
Create multiple references to an object.

Remove references one by one.
28. Garbage Collection
Import gc module.

Check:
- Enabled status
- Collection
Challenge Problems
29. Create a student management example using variables and dictionaries.
30. Create a bank account example demonstrating references.
31. Demonstrate mutable and immutable behavior together.
32. Explain memory behavior using id().