# Phase 13 - Writing Clean Python - Refactoring

def separator(title): print("\n"+"="*50+"\n"+title+"\n"+"="*50)


# Before:
def bad_function(a,b,c): return a*b+c


# After:
def calculate_total_price(price,quantity,tax):
    subtotal=price*quantity
    return subtotal+tax


def main():
    separator("Refactoring")

    print(calculate_total_price(100,5,50))

    print("""
Refactoring means:

Improving code without changing behavior.

Techniques:

- Rename variables
- Split large functions
- Remove duplicate code
- Improve readability
- Add error handling
""")


if __name__=="__main__": main()