"""
=========================================================
Topic : collections.namedtuple

Author: Mohamed Kalid

namedtuple is an extension of tuple.

It allows accessing tuple values using names
instead of indexes.

Normal Tuple:

employee[0]
employee[1]

namedtuple:

employee.name
employee.salary


Advantages:

1. Readability
2. Memory efficient
3. Immutable
4. Lightweight alternative to class


Common Uses:

- Database records
- API responses
- Configuration objects
- Data transfer objects

=========================================================
"""


from collections import namedtuple



def separator(title):

    print("\n" + "=" * 70)
    print(title)
    print("=" * 70)



def main():


    # =====================================================
    # 1. Normal Tuple Problem
    # =====================================================

    separator("1. Normal Tuple Problem")


    employee = (

        "Mohamed",

        "AI Engineer",

        80000

    )


    print(employee)


    print(
        "Name:",
        employee[0]
    )


    print(
        "Role:",
        employee[1]
    )


    print(
        "Salary:",
        employee[2]
    )


    print(
        """
        Problem:
        We need to remember index positions.
        """
    )



    # =====================================================
    # 2. Creating namedtuple
    # =====================================================

    separator("2. Creating namedtuple")


    Employee = namedtuple(

        "Employee",

        [

            "name",

            "role",

            "salary"

        ]

    )


    emp1 = Employee(

        "Mohamed",

        "AI Engineer",

        80000

    )


    print(emp1)



    # =====================================================
    # 3. Access using field names
    # =====================================================

    separator("3. Access Fields")


    print(
        emp1.name
    )


    print(
        emp1.role
    )


    print(
        emp1.salary
    )



    # =====================================================
    # 4. Access using index
    # =====================================================

    separator("4. Index Access")


    print(emp1[0])

    print(emp1[1])

    print(emp1[2])



    # =====================================================
    # 5. namedtuple is Immutable
    # =====================================================

    separator("5. Immutable")


    print(emp1)


    print(
        """
        Values cannot be changed.
        
        emp1.salary = 90000
        
        gives AttributeError
        """
    )



    # =====================================================
    # 6. _fields
    # =====================================================

    separator("6. _fields")


    print(
        Employee._fields
    )



    # =====================================================
    # 7. _make()
    # Create object from iterable
    # =====================================================

    separator("7. _make()")


    data = [

        "Alice",

        "Data Scientist",

        90000

    ]


    emp2 = Employee._make(data)


    print(emp2)



    # =====================================================
    # 8. _asdict()
    # Convert namedtuple to dictionary
    # =====================================================

    separator("8. _asdict()")


    employee_dict = emp1._asdict()


    print(employee_dict)

    print(
        type(employee_dict)
    )



    # =====================================================
    # 9. _replace()
    # Create updated copy
    # =====================================================

    separator("9. _replace()")


    print(emp1)


    updated_employee = emp1._replace(

        salary=100000

    )


    print(updated_employee)


    print(
        "Original:",
        emp1
    )



    # =====================================================
    # 10. Multiple Employees
    # =====================================================

    separator("10. Employee Database Example")


    Employee = namedtuple(

        "Employee",

        [

            "id",

            "name",

            "department"

        ]

    )


    employees = [

        Employee(

            1,

            "Alice",

            "IT"

        ),

        Employee(

            2,

            "Bob",

            "HR"

        ),

        Employee(

            3,

            "Chris",

            "Finance"

        )

    ]


    for employee in employees:

        print(
            employee.name,
            "-",
            employee.department
        )



    # =====================================================
    # 11. API Response Example
    # =====================================================

    separator("11. API Response Example")


    Response = namedtuple(

        "Response",

        [

            "status",

            "message",

            "data"

        ]

    )


    response = Response(

        200,

        "Success",

        {

            "user": "Mohamed"

        }

    )


    print(response)


    print(
        response.data
    )



    # =====================================================
    # 12. Database Row Example
    # =====================================================

    separator("12. Database Row Example")


    User = namedtuple(

        "User",

        [

            "id",

            "username",

            "email"

        ]

    )


    row = User(

        101,

        "kalid",

        "kalid@example.com"

    )


    print(row)


    print(
        row.email
    )



    # =====================================================
    # 13. namedtuple vs tuple
    # =====================================================

    separator("13. namedtuple vs tuple")


    print(
        """
        Tuple:

        user[0]
        user[1]


        namedtuple:

        user.name
        user.email


        Both are immutable.

        namedtuple provides readability.
        """
    )



    # =====================================================
    # 14. namedtuple vs Class
    # =====================================================

    separator("14. namedtuple vs Class")


    print(
        """
        namedtuple:

        - Less code
        - Immutable
        - Memory efficient
        - Data storage


        Class:

        - Mutable
        - Methods
        - Business logic
        - Complex behavior

        """
    )



    # =====================================================
    # 15. Memory Example
    # =====================================================

    separator("15. Memory Efficiency")


    import sys


    normal_tuple = (

        "Python",

        "AI",

        "ML"

    )


    Named = namedtuple(

        "Named",

        [

            "language",

            "field",

            "topic"

        ]

    )


    named_object = Named(

        "Python",

        "AI",

        "ML"

    )


    print(
        "Tuple Size:",
        sys.getsizeof(normal_tuple)
    )


    print(
        "Namedtuple Size:",
        sys.getsizeof(named_object)
    )



if __name__ == "__main__":

    main()