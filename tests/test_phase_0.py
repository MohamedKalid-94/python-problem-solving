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


def test_sum_of_list():
    assert sum_of_list([1, 2, 3]) == 6
    assert sum_of_list([]) == 0
    assert sum_of_list([-1, 1]) == 0


def test_max_of_list():
    assert max_of_list([3, 9, 2]) == 9
    assert max_of_list([-5, -2, -9]) == -2
    assert max_of_list([7]) == 7
    assert max_of_list([]) is None


def test_even_or_odd():
    assert even_or_odd(4) == "even"
    assert even_or_odd(7) == "odd"
    assert even_or_odd(0) == "even"
    assert even_or_odd(-3) == "odd"


def test_is_prime():
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(2) is True
    assert is_prime(17) is True
    assert is_prime(25) is False


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120


def test_fibonacci():
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("a") == "a"
    assert reverse_string("") == ""


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("a") is True
    assert is_palindrome("") is True
    assert is_palindrome("ab") is False


def test_count_vowels():
    assert count_vowels("Hello World") == 3
    assert count_vowels("AEIOU") == 5
    assert count_vowels("xyz") == 0
    assert count_vowels("") == 0


def test_word_frequency():
    assert word_frequency("a a b") == {"a": 2, "b": 1}
    assert word_frequency("The the THE cat") == {"the": 3, "cat": 1}
    assert word_frequency("") == {}