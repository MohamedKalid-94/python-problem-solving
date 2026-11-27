# Phase 13 - Writing Clean Python - Logging

import logging

def separator(title): print("\n"+"="*50+"\n"+title+"\n"+"="*50)


logging.basicConfig(level=logging.INFO)


def process_data():
    logging.info("Processing started")
    result="Success"
    logging.info("Processing completed")
    return result


def main():
    separator("Logging")

    result=process_data()

    print(result)

    try:
        value=10/0
    except Exception as error:
        logging.error(error)

    print("""
Logging Levels:

DEBUG
INFO
WARNING
ERROR
CRITICAL

Used in production systems
for monitoring and debugging.
""")


if __name__=="__main__": main()