# Phase 13 - Writing Clean Python - Assertions

def separator(title): print("\n"+"="*50+"\n"+title+"\n"+"="*50)


def divide(a,b):
    assert b!=0,"Cannot divide by zero"
    return a/b


def main():
    separator("Assertions")

    print(divide(10,2))

    print("""
Assertions validate assumptions.

Used for:

- Finding bugs early
- Checking conditions
- Developer mistakes

Example:

assert value > 0
""")


if __name__=="__main__": main()