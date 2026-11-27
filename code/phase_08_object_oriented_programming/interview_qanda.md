# Phase 8 — Object-Oriented Programming (OOP)
# Interview Questions and Answers

---

## 1. What is Object-Oriented Programming (OOP)?

Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects. Objects contain both data (attributes) and behavior (methods), making code reusable, modular, and easier to maintain.

---

## 2. What are the four pillars of OOP?

- Encapsulation
- Inheritance
- Polymorphism
- Abstraction

---

## 3. What is a class?

A class is a blueprint for creating objects. It defines the properties and behaviors that objects will have.

Example:

```python
class Student:
    pass
```

---

## 4. What is an object?

An object is an instance of a class.

Example:

```python
student = Student()
```

---

## 5. What is the difference between a class and an object?

| Class | Object |
|-------|--------|
| Blueprint | Instance |
| Logical entity | Physical entity |
| Created once | Multiple objects can be created |

---

## 6. What is an attribute?

An attribute is a variable that belongs to a class or object.

Example:

```python
self.name
```

---

## 7. What is a method?

A method is a function defined inside a class.

Example:

```python
def display(self):
    print(self.name)
```

---

## 8. What is `self`?

`self` refers to the current object of the class.

---

## 9. What is a constructor?

A constructor initializes an object automatically when it is created.

Python uses:

```python
__init__()
```

---

## 10. Can a class have multiple constructors?

Python does not support multiple constructors directly.

Instead, use:

- Default arguments
- Class methods
- Variable-length arguments (`*args`, `**kwargs`)

---

## 11. What is inheritance?

Inheritance allows one class to acquire the properties and methods of another class.

---

## 12. Why is inheritance used?

- Code reuse
- Easier maintenance
- Better organization
- Extensibility

---

## 13. Types of inheritance in Python

- Single
- Multiple
- Multilevel
- Hierarchical

---

## 14. What is method overriding?

When a child class provides its own implementation of a parent class method.

---

## 15. What is `super()`?

`super()` is used to access methods or constructors of the parent class.

Example:

```python
super().__init__(name)
```

---

## 16. What is polymorphism?

Polymorphism means one interface with multiple implementations.

---

## 17. Types of polymorphism

- Method overriding
- Duck typing
- Operator overloading

---

## 18. What is duck typing?

If an object behaves like the expected object, Python accepts it regardless of its actual type.

---

## 19. What is encapsulation?

Encapsulation means wrapping data and methods into a single unit while restricting direct access to data.

---

## 20. What are public members?

Public members can be accessed from anywhere.

Example:

```python
self.name
```

---

## 21. What are protected members?

Protected members use a single underscore.

Example:

```python
self._salary
```

By convention, they should only be accessed inside the class and subclasses.

---

## 22. What are private members?

Private members use double underscores.

Example:

```python
self.__balance
```

They cannot be accessed directly outside the class.

---

## 23. Why use getter and setter methods?

They provide controlled access to private data and allow validation before updating values.

---

## 24. What is abstraction?

Abstraction hides implementation details and exposes only essential functionality.

---

## 25. Which module supports abstraction?

```python
abc
```

---

## 26. What is an abstract class?

An abstract class cannot be instantiated directly.

It serves as a blueprint for child classes.

---

## 27. What is an abstract method?

An abstract method has no implementation in the parent class and must be implemented by child classes.

---

## 28. What are magic methods?

Magic methods are special methods surrounded by double underscores.

Example:

```python
__init__()
__str__()
__len__()
__add__()
__eq__()
```

---

## 29. What does `__init__()` do?

Automatically initializes object attributes.

---

## 30. What does `__str__()` do?

Returns a user-friendly string representation of an object.

---

## 31. What does `__repr__()` do?

Returns an unambiguous representation of an object, mainly for debugging.

---

## 32. What does `__len__()` do?

Defines the behavior of the built-in `len()` function.

---

## 33. What does `__add__()` do?

Overloads the `+` operator for custom objects.

---

## 34. What does `__eq__()` do?

Defines how two objects are compared using `==`.

---

## 35. What is operator overloading?

Giving special meaning to operators for user-defined objects using magic methods.

---

## 36. What is a dataclass?

A dataclass automatically generates common methods such as:

- `__init__()`
- `__repr__()`
- `__eq__()`

---

## 37. Which module provides dataclasses?

```python
dataclasses
```

---

## 38. What is the `@dataclass` decorator?

It automatically generates boilerplate code for classes that mainly store data.

---

## 39. What is `field()`?

`field()` customizes dataclass attributes.

Example:

```python
items = field(default_factory=list)
```

---

## 40. Why use `default_factory`?

To avoid mutable default argument problems.

---

## 41. Difference between normal class and dataclass

| Normal Class | Dataclass |
|--------------|-----------|
| Manual constructor | Auto constructor |
| More code | Less code |
| Manual `__repr__()` | Automatic |
| Manual `__eq__()` | Automatic |

---

## 42. What is composition?

Composition is a "has-a" relationship.

Example:

```text
Employee
    |
    └── Address
```

---

## 43. Difference between inheritance and composition

| Inheritance | Composition |
|-------------|-------------|
| Is-a relationship | Has-a relationship |
| Extends parent | Uses another object |
| Strong coupling | Loose coupling |

---

## 44. What are the advantages of OOP?

- Reusability
- Maintainability
- Modularity
- Scalability
- Security
- Easier testing

---

## 45. What are the disadvantages of OOP?

- More memory usage
- Slightly slower execution
- More design effort
- Can be overkill for very small programs

---

## 46. Real-world examples of OOP

- Banking System
- ATM
- Library Management
- Student Management
- Employee Management
- Hospital Management
- E-Commerce
- Vehicle Management
- Food Delivery Apps

---

## 47. How is OOP used in AI/GenAI projects?

Typical classes include:

- DocumentLoader
- EmbeddingModel
- VectorStore
- Retriever
- LLM
- PromptTemplate
- Agent
- Tool
- Memory
- Workflow

---

## 48. Why is OOP important for Python developers?

It helps build:

- Clean code
- Reusable code
- Scalable applications
- Production-ready software

---

## 49. Why do interviewers ask OOP questions?

To evaluate your ability to:

- Design software
- Organize code
- Apply design principles
- Write maintainable applications

---

## 50. OOP Interview Summary

Remember these key concepts:

- Class
- Object
- Attribute
- Method
- Constructor
- Inheritance
- Polymorphism
- Encapsulation
- Abstraction
- Magic Methods
- Dataclasses
- Composition
- Method Overriding
- `super()`
- `self`

Mastering these concepts provides a strong foundation for Python backend development, automation, data engineering, and AI/GenAI applications.