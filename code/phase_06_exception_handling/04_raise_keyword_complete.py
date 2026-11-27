"""
=========================================================
Topic : Raise Keyword in Python

Covered:

1. Understanding raise
2. Manual exception creation
3. Input validation
4. Business rule validation
5. API validation example
6. File validation example
7. Real-world examples

=========================================================
"""


from pathlib import Path



def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



def basic_raise():

    separator("1. Basic Raise Example")


    age = -5


    try:

        if age < 0:

            raise ValueError(
                "Age cannot be negative"
            )


        print(
            "Valid age"
        )


    except ValueError as error:

        print(
            error
        )



def password_validation():

    separator("2. Password Validation")


    password = "123"


    try:

        if len(password) < 8:

            raise ValueError(
                "Password must contain 8 characters"
            )


        print(
            "Password accepted"
        )


    except ValueError as error:

        print(
            "Error:",
            error
        )



def marks_validation():

    separator("3. Student Marks Validation")


    marks = 120


    try:

        if marks > 100 or marks < 0:

            raise ValueError(
                "Marks should be between 0 and 100"
            )


        print(
            "Valid marks"
        )


    except ValueError as error:

        print(
            error
        )



def salary_validation():

    separator("4. Salary Validation")


    salary = -5000


    try:

        if salary < 0:

            raise Exception(
                "Salary cannot be negative"
            )


        print(
            "Salary accepted"
        )


    except Exception as error:

        print(
            error
        )



def file_validation():

    separator("5. File Validation")


    file = Path(
        "report.txt"
    )


    try:

        if not file.exists():

            raise FileNotFoundError(
                "Required file is missing"
            )


        print(
            file.read_text()
        )


    except FileNotFoundError as error:

        print(
            error
        )



def api_request_validation():

    separator("6. API Request Validation")


    request = {

        "username": "",

        "email": "kalid"

    }


    try:

        if not request["username"]:

            raise ValueError(
                "Username required"
            )


        if "@" not in request["email"]:

            raise ValueError(
                "Invalid email format"
            )


        print(
            "Request accepted"
        )


    except ValueError as error:

        print(
            "Validation Error:",
            error
        )



def bank_transaction():

    separator("7. Bank Transaction Example")


    balance = 5000

    amount = 7000


    try:

        if amount > balance:

            raise Exception(
                "Insufficient balance"
            )


        balance -= amount


        print(
            "Transaction successful"
        )


    except Exception as error:

        print(
            "Transaction failed:",
            error
        )



def ai_document_validation():

    separator("8. AI Document Validation")


    document = ""


    try:

        if not document:

            raise ValueError(
                "Document content is empty"
            )


        print(
            "Document ready for processing"
        )


    except ValueError as error:

        print(
            "AI Pipeline Error:",
            error
        )



def main():

    basic_raise()

    password_validation()

    marks_validation()

    salary_validation()

    file_validation()

    api_request_validation()

    bank_transaction()

    ai_document_validation()



if __name__ == "__main__":
    main()