"""
=========================================================
Topic : Dataclasses in Python

Covered:

1. Basic Dataclass
2. Default Values
3. Field Function
4. Comparison
5. Sorting Objects
6. Real-World Example

=========================================================
"""

from dataclasses import dataclass, field

def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

# ---------------------------------------------------------
# Basic Dataclass
# ---------------------------------------------------------

@dataclass
class Student:
    name: str
    age: int
    marks: float

def basic_dataclass_example():
    separator("1. Basic Dataclass")
    student = Student("Kalid", 25, 92.5)
    print(student)
    print("Name:", student.name)
    print("Age:", student.age)
    print("Marks:", student.marks)

# ---------------------------------------------------------
# Default Values
# ---------------------------------------------------------

@dataclass
class Employee:
    name: str
    department: str = "Software"
    salary: int = 50000

def default_values_example():
    separator("2. Default Values")
    employee1 = Employee("Alice")
    employee2 = Employee("Bob", "AI", 85000)
    print(employee1)
    print(employee2)

# ---------------------------------------------------------
# field() Function
# ---------------------------------------------------------

@dataclass
class ShoppingCart:
    customer: str
    items: list = field(default_factory=list)

    def add_item(self, item):
        self.items.append(item)

def field_example():
    separator("3. field() Function")
    cart = ShoppingCart("Kalid")
    cart.add_item("Laptop")
    cart.add_item("Mouse")
    cart.add_item("Keyboard")
    print(cart)

# ---------------------------------------------------------
# Comparison
# ---------------------------------------------------------

@dataclass
class Product:
    name: str
    price: int

def comparison_example():
    separator("4. Comparison")
    product1 = Product("Laptop", 75000)
    product2 = Product("Laptop", 75000)
    product3 = Product("Keyboard", 3000)
    print("product1 == product2 :", product1 == product2)
    print("product1 == product3 :", product1 == product3)

# ---------------------------------------------------------
# Sorting Objects
# ---------------------------------------------------------

@dataclass(order=True)
class Player:
    score: int
    name: str

def sorting_example():
    separator("5. Sorting Dataclass Objects")
    players = [
        Player(90, "John"),
        Player(75, "Alice"),
        Player(98, "Kalid"),
        Player(82, "David")
    ]
    players.sort()
    for player in players:
        print(player)


# ---------------------------------------------------------
# Real-World Example
# ---------------------------------------------------------
@dataclass
class User:
    username: str
    email: str
    role: str = "User"
    active: bool = True

def real_world_example():
    separator("6. Real-World User Management")
    user1 = User("kalid", "kalid@example.com")
    user2 = User("admin", "admin@example.com", "Administrator", True)
    print(user1)
    print(user2)
    print("Username:", user1.username)
    print("Role:", user2.role)

def main():
    basic_dataclass_example()
    default_values_example()
    field_example()
    comparison_example()
    sorting_example()
    real_world_example()

if __name__ == "__main__":
    main()