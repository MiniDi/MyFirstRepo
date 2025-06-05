def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число.")


def safe_division(num1, num2):
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Деление на ноль невозможно, увы"
