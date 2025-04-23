import pytest
from exercise_8 import is_palindrome


def test_is_palindrome_positive():
    assert is_palindrome("мадам") == True


def test_is_palindrome_positive_eng():
    assert is_palindrome("madam") == True


def test_palindrome_spaces():
    assert is_palindrome("мадам и мадам") == True


def test_is_palindrome_negative():
    assert is_palindrome("hello") == False


def test_only_spaces():
    assert is_palindrome("   ") == True