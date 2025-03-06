def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число.")

def expression_output ():
    num1 = get_number("Введите первое число: ")
    num2 = get_number("Введите второе число: ")

    sum_result = num1 + num2
    diff_result = num1 - num2
    prod_result = num1 * num2
    div_result = num1 / num2 if num2 != 0 else "Деление на ноль невозможно, увы"

    print(f"Сумма: {sum_result}")
    print(f"Разность: {diff_result}")
    print(f"Произведение: {prod_result}")
    print(f"Частное: {div_result}")

if __name__ == '__main__':
    expression_output()