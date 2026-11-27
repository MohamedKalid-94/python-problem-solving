"""
=========================================================
Topic : Classes and Objects

Covered:

1. Creating classes
2. Creating objects
3. Class attributes
4. Instance attributes

=========================================================
"""


class Student:
    school_name = "Python Academy"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")
        print(f"School : {Student.school_name}")

def main():
    student1 = Student("Kalid", 25)
    student2 = Student("John", 22)

    student1.display()
    print("-" * 40)
    student2.display()

if __name__ == "__main__":
    main()