# Phase 13 - Writing Clean Python - Naming Conventions

def separator(title): print("\n" + "="*50 + "\n" + title + "\n" + "="*50)

def main():
    separator("Naming Conventions")

    user_name = "Kalid"
    total_amount = 5000
    MAX_RETRY_COUNT = 3

    print("Variable:", user_name)
    print("Amount:", total_amount)
    print("Constant:", MAX_RETRY_COUNT)

    class UserProfile:
        def __init__(self, name): self.name = name

        def display(self): print(self.name)

    user = UserProfile("Kalid")
    user.display()

    def calculate_total_price(price, tax): return price + tax

    print("Function Result:", calculate_total_price(1000,100))

    print("""
Rules:
Variables -> snake_case
Functions -> snake_case
Classes -> PascalCase
Constants -> UPPER_CASE
Private variables -> _single_underscore
""")


if __name__ == "__main__": main()