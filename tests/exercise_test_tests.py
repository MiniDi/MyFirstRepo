import pytest
from exercise_test import is_even, is_prime, factorial


def test_is_even_true():
    assert is_even(4) == True

def test_is_even_false():
    assert is_even(5) == False


def test_is_prime_true():
    assert is_prime(7) == True

def test_is_prime_false():
    assert is_prime(9) == False

def test_is_prime_edge():
    assert is_prime(1) == False
    assert is_prime(2) == True


def test_factorial_basic():
    assert factorial(5) == 120

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-3)