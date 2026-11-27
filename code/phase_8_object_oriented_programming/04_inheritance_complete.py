"""
=========================================================
Topic : Inheritance in Python

Covered:

1. Single Inheritance
2. Multilevel Inheritance
3. Multiple Inheritance
4. Method Overriding
5. super() Function
6. Real-World Example

=========================================================
"""
def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

# ---------------------------------------------------------
# Single Inheritance
# ---------------------------------------------------------
class Animal:
    def eat(self):
        print("Animal is eating.")

class Dog(Animal):
    def bark(self):
        print("Dog is barking.")

def single_inheritance_example():
    separator("1. Single Inheritance")
    dog = Dog()
    dog.eat()
    dog.bark()

# ---------------------------------------------------------
# Multilevel Inheritance
# ---------------------------------------------------------
class Vehicle:
    def start(self):
        print("Vehicle started.")

class Car(Vehicle):
    def drive(self):
        print("Car is driving.")

class SportsCar(Car):
    def turbo(self):
        print("Turbo mode enabled.")

def multilevel_inheritance_example():
    separator("2. Multilevel Inheritance")
    car = SportsCar()
    car.start()
    car.drive()
    car.turbo()

# ---------------------------------------------------------
# Multiple Inheritance
# ---------------------------------------------------------
class Camera:
    def capture(self):
        print("Capturing photo.")

class MusicPlayer:
    def play_music(self):
        print("Playing music.")

class Smartphone(Camera, MusicPlayer):
    def call(self):
        print("Making a phone call.")

def multiple_inheritance_example():
    separator("3. Multiple Inheritance")
    phone = Smartphone()
    phone.capture()
    phone.play_music()
    phone.call()

# ---------------------------------------------------------
# Method Overriding
# ---------------------------------------------------------

class Employee:
    def work(self):
        print("Employee is working.")

class Manager(Employee):
    def work(self):
        print("Manager is managing the team.")

def method_overriding_example():
    separator("4. Method Overriding")
    employee = Employee()
    manager = Manager()
    employee.work()
    manager.work()

# ---------------------------------------------------------
# super() Function
# ---------------------------------------------------------

class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

class Developer(Person):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def display(self):
        super().display()
        print("Programming Language:", self.language)

def super_function_example():
    separator("5. super() Function")
    developer = Developer("Kalid", "Python")
    developer.display()

# ---------------------------------------------------------
# Real-World Example
# ---------------------------------------------------------

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    def display(self):
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    def calculate_interest(self):
        interest = self.balance * self.interest_rate / 100
        print("Interest:", interest)
    def display(self):
        super().display()
        print("Interest Rate:", self.interest_rate, "%")


def real_world_example():
    separator("6. Real-World Banking System")
    account = SavingsAccount("SB1001", 50000, 6.5)
    account.display()
    account.calculate_interest()

def main():
    single_inheritance_example()
    multilevel_inheritance_example()
    multiple_inheritance_example()
    method_overriding_example()
    super_function_example()
    real_world_example()

if __name__ == "__main__":
    main()