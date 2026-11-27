"""
=========================================================
Topic : Polymorphism in Python

Covered:

1. Method Overriding
2. Duck Typing
3. Polymorphism with Functions
4. Polymorphism with Inheritance
5. Built-in Polymorphism
6. Real-World Example

=========================================================
"""
def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

# ---------------------------------------------------------
# Method Overriding
# ---------------------------------------------------------

class Animal:
    def sound(self):
        print("Animal makes a sound.")
class Dog(Animal):
    def sound(self):
        print("Dog says: Bark")
class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")

def method_overriding_example():
    separator("1. Method Overriding")
    dog = Dog()
    cat = Cat()
    dog.sound()
    cat.sound()

# ---------------------------------------------------------
# Duck Typing
# ---------------------------------------------------------

class Bird:
    def move(self):
        print("Bird is flying.")
class Fish:
    def move(self):
        print("Fish is swimming.")
def show_movement(animal):
    animal.move()
def duck_typing_example():
    separator("2. Duck Typing")

    bird = Bird()
    fish = Fish()
    show_movement(bird)
    show_movement(fish)

# ---------------------------------------------------------
# Polymorphism with Functions
# ---------------------------------------------------------

class Circle:
    def area(self):
        print("Area of Circle = π × r²")
class Rectangle:
    def area(self):
        print("Area of Rectangle = Length × Width")
class Triangle:
    def area(self):
        print("Area of Triangle = 1/2 × Base × Height")
def display_area(shape):
    shape.area()

def function_polymorphism_example():
    separator("3. Function Polymorphism")
    display_area(Circle())
    display_area(Rectangle())
    display_area(Triangle())

# ---------------------------------------------------------
# Polymorphism with Inheritance
# ---------------------------------------------------------

class Employee:
    def work(self):
        print("Employee is working.")
class Developer(Employee):
    def work(self):
        print("Developer is writing Python code.")
class Tester(Employee):
    def work(self):
        print("Tester is testing the application.")

def inheritance_polymorphism_example():
    separator("4. Inheritance Polymorphism")
    employees = [Developer(),Tester()]

    for employee in employees:
        employee.work()

# ---------------------------------------------------------
# Built-in Polymorphism
# ---------------------------------------------------------
def built_in_polymorphism_example():
    separator("5. Built-in Polymorphism")
    numbers = [10, 20, 30, 40]
    name = "Python"
    print("Length of List:", len(numbers))
    print("Length of String:", len(name))

# ---------------------------------------------------------
# Real-World Example
# ---------------------------------------------------------

class CreditCardPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")
class UPIPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")
class WalletPayment:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Wallet.")
def process_payment(payment_method, amount):
    payment_method.pay(amount)


def real_world_example():
    separator("6. Real-World Payment System")
    process_payment(CreditCardPayment(), 2500)
    process_payment(UPIPayment(), 1500)
    process_payment(WalletPayment(), 750)

def main():
    method_overriding_example()
    duck_typing_example()
    function_polymorphism_example()
    inheritance_polymorphism_example()
    built_in_polymorphism_example()
    real_world_example()

if __name__ == "__main__":
    main()