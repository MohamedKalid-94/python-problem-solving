# Phase 13 - Writing Clean Python - Code Organization

def separator(title): print("\n"+"="*50+"\n"+title+"\n"+"="*50)


def load_data(): return "Data Loaded"


def process_data(data): return data.upper()


def save_result(result): print(result)


def main():
    separator("Code Organization")

    data=load_data()

    result=process_data(data)

    save_result(result)

    print("""
Good Project Structure:

project/

app/
services/
models/
utils/
tests/

Benefits:

- Maintainability
- Scalability
- Easy debugging
""")


if __name__=="__main__": main()