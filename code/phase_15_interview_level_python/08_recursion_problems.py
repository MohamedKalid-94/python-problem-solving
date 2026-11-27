# Phase 15 - Interview-Level Python
# 08 Recursion Problems

def factorial(n):
    if n==0:return 1
    return n*factorial(n-1)

def fibonacci(n):
    if n<=1:return n
    return fibonacci(n-1)+fibonacci(n-2)

def sum_numbers(n):
    if n==0:return 0
    return n+sum_numbers(n-1)

def main():
    print("Factorial:",factorial(5))
    print("Fibonacci:",fibonacci(6))
    print("Sum:",sum_numbers(5))

if __name__=="__main__": main()