"""
Phase 15 - Interview-Level Python
09 File Handling Problems
"""


def write_file(filename="sample.txt"):
    # "w" creates the file (or overwrites it)
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Python Interview")


def read_file(filename="sample.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()


def count_words(filename="sample.txt"):
    return len(read_file(filename).split())


def main():
    write_file()
    print("Content:", read_file())
    print("Words:", count_words())


if __name__ == "__main__":
    main()