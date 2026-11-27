"""
=========================================================
Topic : Abstraction in Python

Covered:

1. Abstract Classes
2. Abstract Methods
3. Concrete Classes
4. Multiple Implementations
5. Runtime Polymorphism
6. Real-World Example

=========================================================
"""

from abc import ABC, abstractmethod

def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

# ---------------------------------------------------------
# Abstract Class
# ---------------------------------------------------------
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        area = 3.14 * self.radius * self.radius
        print("Circle Area:", area)

def abstract_class_example():
    separator("1. Abstract Class")
    circle = Circle(5)
    circle.area()

# ---------------------------------------------------------
# Multiple Implementations
# ---------------------------------------------------------

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog says: Bark")

class Cat(Animal):
    def sound(self):
        print("Cat says: Meow")

def multiple_implementation_example():
    separator("2. Multiple Implementations")
    dog = Dog()
    cat = Cat()
    dog.sound()
    cat.sound()

# ---------------------------------------------------------
# Runtime Polymorphism
# ---------------------------------------------------------

class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card.")

class UPI(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI.")

class Wallet(Payment):
    def pay(self, amount):
        print(f"Paid ₹{amount} using Wallet.")

def process_payment(payment, amount):
    payment.pay(amount)

def runtime_polymorphism_example():
    separator("3. Runtime Polymorphism")
    process_payment(CreditCard(), 2500)
    process_payment(UPI(), 1200)
    process_payment(Wallet(), 800)

# ---------------------------------------------------------
# Employee Management
# ---------------------------------------------------------

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass

class Developer(Employee):
    def work(self):
        print("Developer is writing Python code.")

class Tester(Employee):
    def work(self):
        print("Tester is testing the application.")

def employee_example():
    separator("4. Employee Management")
    employees = [Developer(), Tester()]

    for employee in employees:
        employee.work()

# ---------------------------------------------------------
# Vehicle Example
# ---------------------------------------------------------
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car started.")

class Bike(Vehicle):
    def start(self):
        print("Bike started.")

def vehicle_example():
    separator("5. Vehicle Example")
    car = Car()
    bike = Bike()
    car.start()
    bike.start()

# ---------------------------------------------------------
# Real-World Example
# ---------------------------------------------------------
class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print("Email:", message)

class SMSNotification(Notification):
    def send(self, message):
        print("SMS:", message)

class PushNotification(Notification):
    def send(self, message):
        print("Push Notification:", message)

def send_notification(notification, message):
    notification.send(message)

def real_world_example():
    separator("6. Real-World Notification System")
    send_notification(EmailNotification(), "Welcome to our application.")
    send_notification(SMSNotification(), "Your OTP is 123456.")
    send_notification(PushNotification(), "You have a new message.")

def main():
    abstract_class_example()
    multiple_implementation_example()
    runtime_polymorphism_example()
    employee_example()
    vehicle_example()
    real_world_example()

if __name__ == "__main__":
    main()