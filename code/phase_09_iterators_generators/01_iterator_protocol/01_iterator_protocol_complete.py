"""
=========================================================
Topic : Iterator Protocol in Python

Covered:

1. Iterable vs Iterator
2. iter() Function
3. next() Function
4. __iter__() Method
5. __next__() Method
6. StopIteration Exception
7. Creating Custom Iterator
8. Real-World Example

=========================================================
"""

def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)

# ---------------------------------------------------------
# Iterable vs Iterator
# ---------------------------------------------------------

def iterable_vs_iterator_example():
    separator("1. Iterable vs Iterator")

    numbers = [10, 20, 30]
    print("Iterable:", numbers)
    iterator = iter(numbers)
    print("Iterator:", iterator)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))


# ---------------------------------------------------------
# iter() Function
# ---------------------------------------------------------

def iter_function_example():
    separator("2. iter() Function")

    name = "Python"
    iterator = iter(name)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

# ---------------------------------------------------------
# next() Function
# ---------------------------------------------------------

def next_function_example():
    separator("3. next() Function")

    numbers = [1, 2, 3]
    iterator = iter(numbers)
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))

# ---------------------------------------------------------
# __iter__() and __next__()
# ---------------------------------------------------------

class Count:
    def __init__(self, maximum):
        self.maximum = maximum
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.maximum:
            value = self.current
            self.current += 1
            return value
        raise StopIteration

def custom_iterator_example():
    separator("4. Custom Iterator")
    counter = Count(5)
    for number in counter:
        print(number)

# ---------------------------------------------------------
# Manual Iterator Usage
# ---------------------------------------------------------

def manual_iterator_example():
    separator("5. Manual Iterator Usage")
    numbers = [100, 200, 300]
    iterator = iter(numbers)

    try:
        while True:
            print(next(iterator))
    except StopIteration:
        print("Iteration completed.")


# ---------------------------------------------------------
# StopIteration Exception
# ---------------------------------------------------------

def stop_iteration_example():
    separator("6. StopIteration Exception")
    numbers = [10, 20]
    iterator = iter(numbers)
    print(next(iterator))
    print(next(iterator))

    try:
        print(next(iterator))
    except StopIteration:
        print("No more elements available.")

# ---------------------------------------------------------
# Real-World Example
# ---------------------------------------------------------

class EmployeeIterator:
    def __init__(self, employees):
        self.employees = employees
        self.index = 0

    def __iter__(self):
        return self
    def __next__(self):
        if self.index < len(self.employees):
            employee = self.employees[self.index]
            self.index += 1
            return employee
        raise StopIteration


def real_world_example():
    separator("7. Real-World Employee Iterator")
    employees = [
        "John",
        "Alice",
        "Kalid",
        "David"
    ]

    employee_iterator = EmployeeIterator(employees)
    for employee in employee_iterator:
        print("Employee:", employee)

def main():
    iterable_vs_iterator_example()
    iter_function_example()
    next_function_example()
    custom_iterator_example()
    manual_iterator_example()
    stop_iteration_example()
    real_world_example()

if __name__ == "__main__":
    main()