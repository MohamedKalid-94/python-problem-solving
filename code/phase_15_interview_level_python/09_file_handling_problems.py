# Phase 15 - Interview-Level Python
# 09 File Handling Problems

def write_file():
    with open("sample.txt","w") as file: file.write("Python Interview")

def read_file():
    with open("sample.txt","r") as file: return file.read()

def count_words():
    return len(read_file().split())

def main():
    write_file()
    print("Content:",read_file())
    print("Words:",count_words())

if __name__=="__main__": main()