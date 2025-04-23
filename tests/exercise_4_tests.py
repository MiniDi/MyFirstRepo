import pytest

from exercise_4 import get_average


def test_exercise_4_positive_1():
    numbers = [1,2,3,4,5,6]
    count = 6
    assert get_average(numbers, count) is True


def test_exercise_4_zero():
    numbers = [-10, 0, 10]
    count = 3
    assert get_average(numbers, count) == False


def test_exercise_4_negative():
    numbers = [-5, -10, -15]
    count = 3
    assert get_average(numbers, count) == False


def test_average_zero_count():
    with pytest.raises(ZeroDivisionError):
        get_average([1, 2, 3], 0)


