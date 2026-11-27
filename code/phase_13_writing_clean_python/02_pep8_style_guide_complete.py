# Phase 13 - Writing Clean Python - PEP 8 Style Guide

def separator(title): print("\n"+"="*50+"\n"+title+"\n"+"="*50)

def calculate_total(price, tax): return price + tax

def main():
    separator("PEP 8 Style Guide")

    user_name = "Kalid"
    total_price = calculate_total(1000,100)

    print("User:", user_name)
    print("Total:", total_price)

    print("""
PEP 8 Rules:

- Use 4 spaces indentation
- Use snake_case variables/functions
- Use PascalCase classes
- Keep imports organized
- Add blank lines between functions
- Keep code readable
- Avoid unnecessary complexity
""")


if __name__ == "__main__": main()