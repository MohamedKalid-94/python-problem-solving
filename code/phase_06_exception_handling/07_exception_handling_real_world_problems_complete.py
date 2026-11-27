"""
=========================================================
Topic : Exception Handling Real World Problems

Covered:

1. Bank transaction system
2. File processing system
3. User registration system
4. API response handling
5. Data processing pipeline
6. AI document processing pipeline
7. Retry style error handling

=========================================================
"""

import json
import logging
from pathlib import Path



def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



logging.basicConfig(
    filename="system_errors.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



class InsufficientBalanceError(Exception):
    pass



class InvalidUserError(Exception):
    pass



class DocumentProcessingError(Exception):
    pass



def bank_transaction_system():

    separator("1. Bank Transaction System")


    balance = 5000

    withdrawal = 7000


    try:

        if withdrawal > balance:

            raise InsufficientBalanceError(
                "Insufficient account balance"
            )


        balance -= withdrawal


        print(
            "Transaction successful"
        )


    except InsufficientBalanceError as error:

        logging.error(
            error
        )

        print(
            "Transaction Failed:",
            error
        )



def file_processing_system():

    separator("2. File Processing System")


    file_path = Path(
        "input.txt"
    )


    try:

        if not file_path.exists():

            raise FileNotFoundError(
                "Input file missing"
            )


        content = file_path.read_text()


        print(
            content
        )


    except FileNotFoundError as error:

        logging.error(
            error
        )

        print(
            error
        )


    except PermissionError as error:

        logging.error(
            error
        )

        print(
            "Permission denied"
        )



def user_registration_system():

    separator("3. User Registration System")


    user = {

        "name": "",

        "email": "kalid"

    }


    try:

        if not user["name"]:

            raise InvalidUserError(
                "Name required"
            )


        if "@" not in user["email"]:

            raise InvalidUserError(
                "Invalid email"
            )


        print(
            "User registered"
        )


    except InvalidUserError as error:

        logging.error(
            error
        )

        print(
            "Registration Failed:",
            error
        )



def api_response_handler():

    separator("4. API Response Handling")


    response = {

        "status": "error",

        "message": "Server unavailable"

    }


    try:

        if response["status"] != "success":

            raise ConnectionError(
                response["message"]
            )


        print(
            "API Success"
        )


    except ConnectionError as error:

        logging.error(
            error
        )

        print(
            "API Error:",
            error
        )



def json_data_processing():

    separator("5. JSON Data Processing")


    json_data = """

    {
        "name":"Kalid",
        "skill":"Python"
    }

    """


    try:

        data = json.loads(
            json_data
        )


        print(
            data
        )


    except json.JSONDecodeError as error:

        logging.error(
            error
        )

        print(
            "Invalid JSON"
        )



def ai_document_processing():

    separator("6. AI Document Processing Pipeline")


    document = {

        "file":"resume.pdf",

        "content":""

    }


    try:

        logging.info(
            "Document upload started"
        )


        if not document["content"]:

            raise DocumentProcessingError(
                "Empty document cannot process"
            )


        logging.info(
            "Text extraction completed"
        )


        logging.info(
            "Embedding generation completed"
        )


        print(
            "Document processed"
        )


    except DocumentProcessingError as error:

        logging.error(
            error
        )

        print(
            "AI Pipeline Error:",
            error
        )



def retry_mechanism_example():

    separator("7. Retry Mechanism Example")


    attempts = 3


    for attempt in range(1, attempts + 1):

        try:

            if attempt < 3:

                raise ConnectionError(
                    "API unavailable"
                )


            print(
                "API Connected"
            )

            break


        except ConnectionError as error:

            logging.warning(
                f"Attempt {attempt}: {error}"
            )


            print(
                "Retrying..."
            )



def main():

    bank_transaction_system()

    file_processing_system()

    user_registration_system()

    api_response_handler()

    json_data_processing()

    ai_document_processing()

    retry_mechanism_example()



if __name__ == "__main__":
    main()