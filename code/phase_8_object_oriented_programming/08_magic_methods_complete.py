"""
=========================================================
Topic : Magic Methods in Python

Covered:

1. __init__()
2. __str__()
3. __repr__()
4. __len__()
5. __add__()
6. __eq__()
7. Real-World Example

=========================================================
"""

def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

# ---------------------------------------------------------
# __init__()
# ---------------------------------------------------------

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

def init_method_example():
    separator("1. __init__()")
    student = Student("Kalid", 92)
    print("Name:", student.name)
    print("Marks:", student.marks)

# ---------------------------------------------------------
# __str__()
# ---------------------------------------------------------

class Employee:
    def __init__(self, name, department):
        self.name = name
        self.department = department

    def __str__(self):
        return f"Employee(Name={self.name}, Department={self.department})"


def str_method_example():
    separator("2. __str__()")
    employee = Employee("Alice", "AI")
    print(employee)

# ---------------------------------------------------------
# __repr__()
# ---------------------------------------------------------

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def __repr__(self):
        return f"Product('{self.name}', {self.price})"

def repr_method_example():
    separator("3. __repr__()")
    product = Product("Laptop", 75000)
    print(product)
    print(repr(product))

# ---------------------------------------------------------
# __len__()
# ---------------------------------------------------------

class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self, item):
        self.items.append(item)
    def __len__(self):
        return len(self.items)

def len_method_example():
    separator("4. __len__()")
    cart = ShoppingCart()
    cart.add_item("Laptop")
    cart.add_item("Mouse")
    cart.add_item("Keyboard")
    print("Items in Cart:", len(cart))


# ---------------------------------------------------------
# __add__()
# ---------------------------------------------------------

class Salary:
    def __init__(self, amount):
        self.amount = amount
    def __add__(self, other):
        return Salary(self.amount + other.amount)
    def __str__(self):
        return f"₹{self.amount}"

def add_method_example():
    separator("5. __add__()")
    salary1 = Salary(50000)
    salary2 = Salary(30000)
    total = salary1 + salary2
    print("Salary 1:", salary1)
    print("Salary 2:", salary2)
    print("Total Salary:", total)

# ---------------------------------------------------------
# __eq__()
# ---------------------------------------------------------

class User:
    def __init__(self, username):
        self.username = username
    def __eq__(self, other):
        return self.username == other.username

def eq_method_example():
    separator("6. __eq__()")
    user1 = User("kalid")
    user2 = User("kalid")
    user3 = User("john")
    print("user1 == user2 :", user1 == user2)
    print("user1 == user3 :", user1 == user3)

# ---------------------------------------------------------
# Real-World Example
# ---------------------------------------------------------

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f"Account({self.account_number}) Balance: ₹{self.balance}"

    def __add__(self, other):
        return BankAccount("TOTAL", self.balance + other.balance)

    def __eq__(self, other):
        return self.account_number == other.account_number


def real_world_example():
    separator("7. Real-World Banking Example")
    account1 = BankAccount("SB1001", 25000)
    account2 = BankAccount("SB1002", 15000)
    account3 = BankAccount("SB1001", 40000)
    print(account1)
    print(account2)
    total = account1 + account2
    print("Combined Balance:", total)
    print("account1 == account2 :", account1 == account2)
    print("account1 == account3 :", account1 == account3)

def main():
    init_method_example()
    str_method_example()
    repr_method_example()
    len_method_example()
    add_method_example()
    eq_method_example()
    real_world_example()

if __name__ == "__main__":
    main()