"""
=========================================================
Topic : Else and Finally in Exception Handling

Covered:

1. try block
2. except block
3. else block
4. finally block
5. File cleanup
6. Resource management
7. Database style handling
8. Real-world examples

=========================================================
"""


from pathlib import Path



def separator(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)



def try_except_else():

    separator("1. Try Except Else")

    try:

        number = 10 / 2


    except ZeroDivisionError:

        print(
            "Division failed"
        )


    else:

        print(
            "Calculation successful:",
            number
        )



def try_except_else_failure():

    separator("2. Else Block When Error Occurs")


    try:

        number = 10 / 0


    except ZeroDivisionError:

        print(
            "Cannot divide by zero"
        )


    else:

        print(
            "Success:",
            number
        )



def finally_execution():

    separator("3. Finally Block")


    try:

        file = open(
            "data.txt",
            "w"
        )

        file.write(
            "Python Exception Handling"
        )


    except Exception as error:

        print(
            error
        )


    finally:

        file.close()

        print(
            "File closed"
        )



def safe_file_operation():

    separator("4. Safe File Operation")


    file_path = Path(
        "example.txt"
    )


    try:

        with open(
            file_path,
            "w"
        ) as file:

            file.write(
                "Learning Python"
            )


    except PermissionError:

        print(
            "Permission denied"
        )


    else:

        print(
            "File created successfully"
        )


    finally:

        print(
            "File operation completed"
        )



def user_login_validation():

    separator("5. User Login Example")


    username = "kalid"

    password = "1234"


    try:

        if username != "kalid":

            raise ValueError(
                "Invalid username"
            )


        if password != "1234":

            raise ValueError(
                "Invalid password"
            )


    except ValueError as error:

        print(
            "Login Failed:",
            error
        )


    else:

        print(
            "Login Successful"
        )


    finally:

        print(
            "Login process completed"
        )



def database_connection_pattern():

    separator("6. Database Connection Pattern")


    connection = None


    try:

        print(
            "Database connected"
        )

        connection = True


        print(
            "Executing query"
        )


    except Exception:

        print(
            "Database error"
        )


    else:

        print(
            "Transaction successful"
        )


    finally:

        if connection:

            print(
                "Database connection closed"
            )



def api_request_pattern():

    separator("7. API Request Pattern")


    try:

        print(
            "Calling API"
        )


        response = {

            "status": "success"

        }


        if response["status"] != "success":

            raise Exception(
                "API failed"
            )


    except Exception as error:

        print(
            "API Error:",
            error
        )


    else:

        print(
            "API Response:",
            response
        )


    finally:

        print(
            "API request completed"
        )



def main():

    try_except_else()

    try_except_else_failure()

    finally_execution()

    safe_file_operation()

    user_login_validation()

    database_connection_pattern()

    api_request_pattern()



if __name__ == "__main__":
    main()