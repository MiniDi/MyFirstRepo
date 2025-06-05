def is_even(n):
    """Проверяет, является ли число чётным"""
    return n % 2 == 0

def is_prime(n):
    """Проверяет, является ли число простым"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    """Вычисляет факториал числа"""
    if n < 0:
        raise ValueError("Факториал не определён для отрицательных чисел")
    result = 1
    for i in range(2, n+1):
        result *= i
    return result