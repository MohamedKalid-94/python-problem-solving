# Phase 8 — Object-Oriented Programming (OOP)

## Overview

Object-Oriented Programming (OOP) is a programming paradigm that models real-world entities as objects. An object combines data (attributes) and behavior (methods) into a single unit. OOP helps build software that is modular, reusable, maintainable, and scalable.

Python is a multi-paradigm language, but OOP is widely used in backend development, desktop applications, web frameworks, automation, machine learning, and AI systems.

---

# Why OOP?

Without OOP, large applications become difficult to maintain because data and functions are scattered throughout the program.

OOP solves this by grouping related data and behavior together.

Benefits include:

- Code reusability
- Better organization
- Easier maintenance
- Improved readability
- Scalability
- Security through encapsulation

---

# OOP Terminology

| Term | Description |
|------|-------------|
| Class | Blueprint for creating objects |
| Object | Instance of a class |
| Attribute | Variable inside a class |
| Method | Function inside a class |
| Constructor | Initializes an object |
| Inheritance | Reusing code from another class |
| Polymorphism | Same interface, different implementation |
| Encapsulation | Hiding internal data |
| Abstraction | Hiding implementation details |

---

# Class

A class is a blueprint that defines the structure and behavior of objects.

Example:

```python
class Student:
    pass
```

A class itself does not store data until objects are created.

---

# Object

An object is an instance of a class.

Example:

```python
student = Student()
```

Multiple objects can be created from the same class.

---

# Attributes

Attributes store information about an object.

There are two types:

## Class Attribute

Shared by all objects.

```python
class Student:
    school = "ABC School"
```

---

## Instance Attribute

Unique for each object.

```python
self.name
self.age
```

---

# Methods

Methods define object behavior.

Example:

```python
def display(self):
    print(self.name)
```

Types:

- Instance Method
- Class Method
- Static Method

---

# self

`self` refers to the current object.

Example:

```python
self.name
```

Without `self`, Python cannot identify which object's data should be accessed.

---

# Constructor

The constructor automatically runs when an object is created.

Python constructor:

```python
__init__()
```

Example:

```python
class Student:
    def __init__(self, name):
        self.name = name
```

---

# Inheritance

Inheritance allows one class to acquire properties and methods from another class.

Example:

```text
Animal
   |
   └── Dog
```

Advantages:

- Code reuse
- Less duplication
- Easy maintenance

---

## Types of Inheritance

### Single

```text
A
|
B
```

---

### Multilevel

```text
A
|
B
|
C
```

---

### Multiple

```text
A     B
 \   /
   C
```

---

### Hierarchical

```text
     A
   / | \
  B  C  D
```

---

# Method Overriding

A child class provides its own implementation of a parent class method.

Example:

```python
class Animal:
    def sound(self):
        print("Sound")


class Dog(Animal):
    def sound(self):
        print("Bark")
```

---

# super()

`super()` calls methods or constructors of the parent class.

Example:

```python
super().__init__(name)
```

Benefits:

- Reuse parent logic
- Avoid duplicate code

---

# Polymorphism

Polymorphism means one interface with multiple implementations.

Example:

```python
payment.pay()
```

Different payment objects perform different actions.

Examples:

- Credit Card
- UPI
- Wallet

All implement:

```python
pay()
```

---

# Duck Typing

Python follows duck typing.

"If it behaves like a duck, treat it as a duck."

Python checks behavior instead of object type.

---

# Encapsulation

Encapsulation combines data and methods while restricting direct access.

Benefits:

- Data protection
- Validation
- Better control

---

## Public Members

```python
self.name
```

Accessible everywhere.

---

## Protected Members

```python
self._salary
```

Should only be accessed inside the class and subclasses.

---

## Private Members

```python
self.__balance
```

Cannot be directly accessed outside the class.

---

# Getter and Setter

Getter returns private data.

Setter updates private data with validation.

Example:

```python
get_balance()

set_balance()
```

---

# Abstraction

Abstraction hides implementation details and exposes only essential functionality.

Example:

```python
pay()
```

Users know how to call the method without knowing how it works internally.

---

# Abstract Class

Defined using:

```python
ABC
```

Cannot create objects directly.

Example:

```python
class Payment(ABC):
```

---

# Abstract Method

Declared using:

```python
@abstractmethod
```

Must be implemented by child classes.

---

# Magic Methods

Magic methods begin and end with double underscores.

Examples:

```python
__init__()
__str__()
__repr__()
__len__()
__add__()
__eq__()
```

---

## __init__()

Constructor

Automatically initializes objects.

---

## __str__()

Returns a readable string.

Used by:

```python
print(object)
```

---

## __repr__()

Returns a detailed representation.

Mostly used for debugging.

---

## __len__()

Supports:

```python
len(object)
```

---

## __add__()

Supports:

```python
object1 + object2
```

---

## __eq__()

Supports:

```python
object1 == object2
```

---

# Operator Overloading

Magic methods allow operators to work with custom objects.

Examples:

```python
+
==
<
>
```

---

# Dataclasses

Introduced in Python 3.7.

Module:

```python
dataclasses
```

Decorator:

```python
@dataclass
```

Automatically creates:

- Constructor
- String representation
- Equality comparison

---

# field()

Used for advanced dataclass customization.

Example:

```python
items = field(default_factory=list)
```

Useful for mutable objects.

---

# Composition

Composition means one class contains another class.

Example:

```text
Employee
    |
    └── Address
```

This is called a "has-a" relationship.

---

# Inheritance vs Composition

| Inheritance | Composition |
|-------------|-------------|
| Is-a relationship | Has-a relationship |
| Extends parent | Uses another object |
| Strong coupling | Loose coupling |
| Code reuse | Object reuse |

---

# Advantages of OOP

- Modular code
- Reusable components
- Better maintenance
- Easier debugging
- Improved scalability
- Better security
- Real-world modeling
- Cleaner architecture

---

# Limitations of OOP

- More planning required
- Higher memory usage
- Slightly slower execution
- Can be excessive for small scripts

---

# Real-World Applications

- Banking System
- ATM Software
- Student Management
- Employee Management
- Hospital Management
- Hotel Booking
- Food Delivery
- Inventory Management
- E-Commerce
- Vehicle Management

---

# OOP in AI and GenAI

Common classes include:

```text
Application
│
├── DocumentLoader
├── TextSplitter
├── EmbeddingModel
├── VectorStore
├── Retriever
├── PromptTemplate
├── LLM
├── Agent
├── Memory
└── Workflow
```

Each component is implemented as a class with clearly defined responsibilities.

---

# Best Practices

- Keep classes focused on one responsibility.
- Prefer composition over inheritance when appropriate.
- Make attributes private when they should not be modified directly.
- Use meaningful class and method names.
- Avoid deep inheritance hierarchies.
- Write reusable methods.
- Use dataclasses for simple data containers.
- Use abstract classes to define common interfaces.
- Follow the DRY (Don't Repeat Yourself) principle.

---

# Phase Summary

After completing this phase, you should be able to:

- Create classes and objects
- Write constructors
- Build reusable methods
- Apply inheritance
- Implement polymorphism
- Protect data using encapsulation
- Design abstract classes
- Use magic methods
- Build data models with dataclasses
- Develop real-world object-oriented applications

These concepts form the foundation of professional Python development and are extensively used in frameworks such as Django, Flask, FastAPI, LangChain, LangGraph, and production AI/GenAI systems.