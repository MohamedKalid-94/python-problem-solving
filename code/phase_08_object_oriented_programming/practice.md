# Phase 8 — Object-Oriented Programming (OOP)
# Practice Problems

## Beginner Level

### 1. Student Class
Create a `Student` class with:

- name
- age

Create two objects and display their details.

---

### 2. Employee Class

Create an `Employee` class with:

- employee_id
- name
- salary

Display employee information.

---

### 3. Rectangle Class

Create a class that stores:

- length
- width

Create methods to calculate:

- Area
- Perimeter

---

### 4. Circle Class

Create a class that stores:

- radius

Create methods to calculate:

- Area
- Circumference

---

### 5. Book Class

Create a class with:

- title
- author
- price

Display book details.

---

### 6. Mobile Class

Store:

- brand
- model
- price

Create multiple objects.

---

### 7. Laptop Class

Store:

- brand
- processor
- RAM

Print all details.

---

### 8. Movie Class

Store:

- title
- rating
- language

Display information.

---

### 9. Bank Account

Create methods:

- Deposit
- Withdraw
- Check Balance

---

### 10. Calculator

Create methods:

- Add
- Subtract
- Multiply
- Divide

---

# Methods

### 11. Car Class

Create methods:

- Start
- Stop
- Accelerate

---

### 12. TV Class

Create methods:

- Power On
- Change Channel
- Increase Volume

---

### 13. Shopping Cart

Create methods:

- Add Item
- Remove Item
- Show Items

---

### 14. Library

Create methods:

- Add Book
- Issue Book
- Return Book

---

### 15. Student Result

Create methods:

- Calculate Total
- Calculate Average
- Display Grade

---

# Constructors

### 16. Product Class

Initialize:

- name
- price

Display information.

---

### 17. User Class

Constructor should initialize:

- username
- email
- password

---

### 18. Vehicle

Initialize:

- brand
- model
- year

Display all information.

---

### 19. Hotel Room

Initialize:

- room number
- room type
- price

---

### 20. ATM Card

Initialize:

- card number
- balance

Display account information.

---

# Inheritance

### 21. Animal

Create:

- Animal
- Dog

Dog should inherit Animal.

---

### 22. Vehicle

Create:

- Vehicle
- Car

Car should inherit Vehicle.

---

### 23. Employee

Create:

- Employee
- Manager

Manager should inherit Employee.

---

### 24. Shape

Create:

- Shape
- Rectangle
- Circle

---

### 25. Account

Create:

- BankAccount
- SavingsAccount

---

# Polymorphism

### 26. Payment

Implement:

- Credit Card
- UPI
- Wallet

Each should implement:

```python
pay()
```

---

### 27. Animal Sound

Implement:

- Dog
- Cat
- Cow

Each should implement:

```python
sound()
```

---

### 28. Employee Work

Implement:

- Developer
- Tester
- Manager

Each should implement:

```python
work()
```

---

### 29. Notification

Implement:

- Email
- SMS
- Push

---

### 30. Shape Area

Implement:

- Circle
- Rectangle
- Triangle

---

# Encapsulation

### 31. Bank Account

Create private balance.

Use getter and setter.

---

### 32. Student

Store private marks.

Validate before updating.

---

### 33. Employee

Store private salary.

Increase salary using setter.

---

### 34. User

Store private password.

Do not allow direct access.

---

### 35. Product

Store private price.

Validate positive values only.

---

# Abstraction

### 36. Payment System

Create abstract class:

```python
Payment
```

Implement:

- UPI
- Credit Card

---

### 37. Vehicle

Abstract method:

```python
start()
```

Implement:

- Bike
- Car

---

### 38. Employee

Abstract method:

```python
work()
```

Implement:

- Developer
- Tester

---

### 39. Animal

Abstract method:

```python
sound()
```

---

### 40. Notification

Abstract method:

```python
send()
```

Implement:

- Email
- SMS

---

# Magic Methods

### 41. Implement `__str__()`

Create a class that prints object details in a readable format.

---

### 42. Implement `__repr__()`

Return a detailed object representation.

---

### 43. Implement `__len__()`

Return the number of items stored in a custom object.

---

### 44. Implement `__add__()`

Add two custom objects.

---

### 45. Implement `__eq__()`

Compare two objects.

---

# Dataclasses

### 46. Student Dataclass

Create a dataclass with:

- name
- age
- marks

---

### 47. Employee Dataclass

Store:

- id
- name
- department

---

### 48. Product Dataclass

Store:

- name
- price
- quantity

---

### 49. Address Dataclass

Store:

- city
- state
- country

Use it inside another class.

---

### 50. Shopping Cart Dataclass

Store:

- customer name
- items list

Use:

```python
field(default_factory=list)
```

---

# Real-World Problems

### 51. Student Management System

Features:

- Add Student
- Display Students
- Search Student

---

### 52. Employee Management System

Features:

- Add Employee
- Update Salary
- Display Employees

---

### 53. Banking System

Features:

- Deposit
- Withdraw
- Transfer
- Balance Enquiry

---

### 54. Library Management System

Features:

- Add Books
- Issue Books
- Return Books

---

### 55. Hospital Management System

Manage:

- Doctors
- Patients
- Appointments

---

### 56. Hotel Booking System

Manage:

- Rooms
- Customers
- Reservations

---

### 57. Inventory Management

Manage:

- Products
- Stock
- Sales

---

### 58. E-Commerce System

Implement:

- Product
- Customer
- Shopping Cart
- Orders

---

### 59. Vehicle Rental System

Manage:

- Cars
- Bikes
- Customers
- Rentals

---

### 60. AI Model Management System

Create classes for:

- Dataset
- EmbeddingModel
- VectorStore
- Retriever
- LLM
- Agent

Simulate a simple AI workflow using OOP.

---

# Mini Projects

- Student Management System
- Employee Management System
- Banking Application
- ATM Simulation
- Hospital Management
- Library Management
- Inventory Management
- Hotel Booking System
- E-Commerce Shopping Cart
- AI Model Management System

---

# Challenge Problems

1. Build a complete Library Management System using OOP.
2. Create a Banking System with inheritance and polymorphism.
3. Design an Employee Management System using abstraction.
4. Build an E-Commerce Shopping Cart using dataclasses.
5. Create an AI Pipeline using classes for Loader, EmbeddingModel, VectorStore, Retriever, and Agent.

---

# Learning Outcome

After completing these practice problems, you should be able to:

- Design classes and objects
- Use constructors effectively
- Implement inheritance and polymorphism
- Protect data using encapsulation
- Build abstract class hierarchies
- Use Python magic methods
- Create clean data models with dataclasses
- Develop real-world object-oriented applications
- Apply OOP principles in backend development and AI/GenAI projects