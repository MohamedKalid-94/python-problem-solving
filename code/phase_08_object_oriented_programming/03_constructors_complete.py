"""
=========================================================
Topic : Constructors in Python

Covered:

1. Default Constructor
2. Parameterized Constructor
3. Constructor with Default Values
4. Multiple Objects
5. Updating Object State
6. Real-World Example

=========================================================
"""
def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

# ---------------------------------------------------------
# Default Constructor
# ---------------------------------------------------------

class Student:
    def __init__(self):
        self.name = "Kalid"
        self.age = 25

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

def default_constructor_example():
    separator("1. Default Constructor")

    student = Student()
    student.display()

# ---------------------------------------------------------
# Parameterized Constructor
# ---------------------------------------------------------

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee:", self.name)
        print("Salary:", self.salary)

def parameterized_constructor_example():
    separator("2. Parameterized Constructor")
    employee = Employee("Alice", 65000)
    employee.display()

# ---------------------------------------------------------
# Constructor with Default Values
# ---------------------------------------------------------

class Product:
    def __init__(self, name, price=0):
        self.name = name
        self.price = price

    def display(self):
        print("Product:", self.name)
        print("Price:", self.price)


def default_value_constructor_example():
    separator("3. Constructor with Default Values")
    product1 = Product("Laptop", 75000)
    product2 = Product("Mouse")
    product1.display()
    print("-" * 30)
    product2.display()

# ---------------------------------------------------------
# Multiple Objects
# ---------------------------------------------------------

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)

def multiple_objects_example():
    separator("4. Multiple Objects")
    car1 = Car("Toyota", "Camry")
    car2 = Car("Tesla", "Model 3")
    car1.display()
    print("-" * 30)
    car2.display()

# ---------------------------------------------------------
# Updating Object State
# ---------------------------------------------------------
class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def display(self):
        print("Account Holder:", self.account_holder)
        print("Balance:", self.balance)

def object_state_example():
    separator("5. Updating Object State")
    account = BankAccount("Kalid", 10000)
    account.display()
    account.deposit(5000)
    print("After Deposit")
    account.display()

# ---------------------------------------------------------
# Real-World Example
# ---------------------------------------------------------

class User:
    def __init__(self, username, email, active=True):
        self.username = username
        self.email = email
        self.active = active

    def display(self):
        print("Username:", self.username)
        print("Email:", self.email)
        print("Active:", self.active)

def real_world_example():
    separator("6. Real-World User Registration")
    user1 = User("kalid", "kalid@example.com")
    user2 = User("john", "john@example.com", False)
    user1.display()
    print("-" * 30)
    user2.display()

def main():
    default_constructor_example()
    parameterized_constructor_example()
    default_value_constructor_example()
    multiple_objects_example()
    object_state_example()
    real_world_example()

if __name__ == "__main__":
    main()