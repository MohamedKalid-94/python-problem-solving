# Run this file to see the output of every Phase 0 solution.

from phase_0_basics.sum_of_list import sum_of_list
from phase_0_basics.max_of_list import max_of_list
from phase_0_basics.even_or_odd import even_or_odd
from phase_0_basics.is_prime import is_prime
from phase_0_basics.factorial import factorial
from phase_0_basics.fibonacci import fibonacci
from phase_0_basics.reverse_string import reverse_string
from phase_0_basics.palindrome import is_palindrome
from phase_0_basics.count_vowels import count_vowels
from phase_0_basics.word_frequency import word_frequency


print("001 Sum of list")
print("  [1, 2, 3]  ->", sum_of_list([1, 2, 3]))
print("  []         ->", sum_of_list([]))

print("002 Max of list")
print("  [3, 9, 2]     ->", max_of_list([3, 9, 2]))
print("  [-5, -2, -9]  ->", max_of_list([-5, -2, -9]))

print("003 Even or odd")
print("  4  ->", even_or_odd(4))
print("  7  ->", even_or_odd(7))

print("004 Is prime")
print("  17 ->", is_prime(17))
print("  25 ->", is_prime(25))

print("005 Factorial")
print("  5  ->", factorial(5))
print("  0  ->", factorial(0))

print("006 Fibonacci")
print("  10 ->", fibonacci(10))

print("007 Reverse string")
print("  hello ->", reverse_string("hello"))

print("008 Palindrome")
print("  racecar ->", is_palindrome("racecar"))
print("  hello   ->", is_palindrome("hello"))

print("009 Count vowels")
print("  Hello World ->", count_vowels("Hello World"))

print("010 Word frequency")
print("  a a b ->", word_frequency("a a b"))