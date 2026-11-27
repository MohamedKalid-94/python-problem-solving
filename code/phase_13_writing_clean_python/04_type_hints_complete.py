# Phase 13 - Writing Clean Python - Type Hints

def separator(title): print("\n"+"="*50+"\n"+title+"\n"+"="*50)


def calculate_sum(a:int,b:int)->int:
    return a+b


def get_user_name()->str:
    return "Kalid"


def get_scores()->list[int]:
    return [90,80,70]


def main():
    separator("Type Hints")

    print(calculate_sum(10,20))
    print(get_user_name())
    print(get_scores())

    print("""
Type hints improve:

- Code readability
- IDE suggestions
- Error detection
- Large project maintenance

Examples:

str
int
float
list[str]
dict[str,int]
""")


if __name__=="__main__": main()