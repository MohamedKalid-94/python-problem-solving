# Phase 13 - Writing Clean Python - Docstrings

def separator(title): print("\n"+"="*50+"\n"+title+"\n"+"="*50)


def add_numbers(a:int,b:int)->int:
    """
    Add two numbers and return result.
    """
    return a+b


class User:
    """
    Represents a user object.
    """

    def __init__(self,name):
        self.name=name


def main():
    separator("Docstrings")

    print(add_numbers(10,20))

    user=User("Kalid")

    print(user.name)

    print("""
Docstrings explain:

- Function purpose
- Parameters
- Return values
- Class responsibility

Used for:
Documentation
API development
Team collaboration
""")


if __name__=="__main__": main()