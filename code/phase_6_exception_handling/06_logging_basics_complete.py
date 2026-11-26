"""
=========================================================
Topic : Logging Basics in Python

Covered:

1. Understanding logging
2. Logging levels
3. Create log file
4. Debug information
5. Error tracking
6. Exception logging
7. Application logging
8. AI pipeline logging

=========================================================
"""

import logging
from pathlib import Path



def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



logging.basicConfig(
    filename="application.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)



def basic_logging():

    separator("1. Basic Logging")


    logging.debug(
        "Debug message"
    )

    logging.info(
        "Application started"
    )

    logging.warning(
        "Memory usage is high"
    )

    logging.error(
        "Database connection failed"
    )

    logging.critical(
        "System failure"
    )


    print(
        "Logs written"
    )



def user_login_logging():

    separator("2. User Login Logging")


    username = "kalid"


    try:

        if username == "kalid":

            logging.info(
                "User login successful"
            )

            print(
                "Login success"
            )


    except Exception as error:

        logging.error(
            error
        )



def exception_logging():

    separator("3. Exception Logging")


    try:

        result = 10 / 0

        print(result)


    except ZeroDivisionError:

        logging.exception(
            "Division error occurred"
        )

        print(
            "Error handled"
        )



def file_processing_logging():

    separator("4. File Processing Logging")


    file = Path(
        "data.txt"
    )


    try:

        content = file.read_text()


        logging.info(
            "File read successfully"
        )


        print(
            content
        )


    except FileNotFoundError:

        logging.error(
            "File does not exist"
        )



def api_request_logging():

    separator("5. API Request Logging")


    try:

        logging.info(
            "API request started"
        )


        response = {

            "status": "success"

        }


        if response["status"] == "success":

            logging.info(
                "API response received"
            )


    except Exception as error:

        logging.error(
            f"API failed: {error}"
        )



def ai_pipeline_logging():

    separator("6. AI Pipeline Logging")


    try:

        logging.info(
            "Document upload started"
        )


        logging.info(
            "Text extraction completed"
        )


        logging.info(
            "Chunking completed"
        )


        logging.info(
            "Embedding generation completed"
        )


        logging.info(
            "Vector storage completed"
        )


        print(
            "AI pipeline completed"
        )


    except Exception as error:

        logging.exception(
            "AI pipeline failed"
        )



def custom_logger():

    separator("7. Custom Logger")


    logger = logging.getLogger(
        "AI_System"
    )


    logger.setLevel(
        logging.DEBUG
    )


    logger.info(
        "Custom AI logger created"
    )


    print(
        "Custom logger executed"
    )



def main():

    basic_logging()

    user_login_logging()

    exception_logging()

    file_processing_logging()

    api_request_logging()

    ai_pipeline_logging()

    custom_logger()



if __name__ == "__main__":
    main()