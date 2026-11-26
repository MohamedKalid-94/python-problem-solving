"""
=========================================================
Topic : Custom Exceptions in Python

Covered:

1. Creating custom exceptions
2. Using custom errors
3. Business logic validation
4. Banking example
5. Authentication example
6. File processing example
7. AI pipeline example

=========================================================
"""


from pathlib import Path



def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



class InvalidAgeError(Exception):
    pass



class InsufficientBalanceError(Exception):
    pass



class AuthenticationError(Exception):
    pass



class InvalidDocumentError(Exception):
    pass



def age_validation():

    separator("1. Custom Age Exception")


    age = -10


    try:

        if age < 0:

            raise InvalidAgeError(
                "Age cannot be negative"
            )


        print(
            "Valid age"
        )


    except InvalidAgeError as error:

        print(
            error
        )



def bank_transaction():

    separator("2. Banking Custom Exception")


    balance = 5000

    withdraw_amount = 7000


    try:

        if withdraw_amount > balance:

            raise InsufficientBalanceError(
                "Insufficient account balance"
            )


        balance -= withdraw_amount


        print(
            "Withdrawal successful"
        )


    except InsufficientBalanceError as error:

        print(
            "Transaction Failed:",
            error
        )



def user_authentication():

    separator("3. Authentication Exception")


    username = "admin"

    password = "wrong"


    try:

        if username != "admin" or password != "1234":

            raise AuthenticationError(
                "Invalid username or password"
            )


        print(
            "Login successful"
        )


    except AuthenticationError as error:

        print(
            error
        )



def file_processing_validation():

    separator("4. File Processing Exception")


    file = Path(
        "empty_document.txt"
    )


    file.write_text(
        ""
    )


    try:

        content = file.read_text()


        if not content:

            raise InvalidDocumentError(
                "Document content is empty"
            )


        print(
            content
        )


    except InvalidDocumentError as error:

        print(
            "File Error:",
            error
        )



def employee_registration():

    separator("5. Employee Registration")


    employee = {

        "name": "",

        "email": "invalid"

    }


    try:

        if not employee["name"]:

            raise ValueError(
                "Employee name required"
            )


        if "@" not in employee["email"]:

            raise ValueError(
                "Invalid email"
            )


        print(
            "Employee registered"
        )


    except ValueError as error:

        print(
            error
        )



def ai_document_pipeline():

    separator("6. AI Document Processing Exception")


    document = {

        "name": "report.pdf",

        "text": ""

    }


    try:

        if not document["text"]:

            raise InvalidDocumentError(
                "Cannot create embeddings from empty document"
            )


        print(
            "Creating embeddings"
        )


    except InvalidDocumentError as error:

        print(
            "RAG Pipeline Error:",
            error
        )



def api_validation():

    separator("7. API Request Validation")


    request = {

        "user_id": None,

        "query": ""

    }


    try:

        if request["user_id"] is None:

            raise AuthenticationError(
                "User authentication required"
            )


        if not request["query"]:

            raise ValueError(
                "Query cannot be empty"
            )


        print(
            "Request processed"
        )


    except (
        AuthenticationError,
        ValueError
    ) as error:

        print(
            "API Error:",
            error
        )



def main():

    age_validation()

    bank_transaction()

    user_authentication()

    file_processing_validation()

    employee_registration()

    ai_document_pipeline()

    api_validation()



if __name__ == "__main__":
    main()