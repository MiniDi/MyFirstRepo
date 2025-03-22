from units import common_function


def expression_output ():
    num1 = common_function.get_number("Введите первое число: ")
    num2 = common_function.get_number("Введите второе число: ")

    sum_result = num1 + num2
    diff_result = num1 - num2
    prod_result = num1 * num2
    div_result = common_function.safe_division(num1, num2)

    print(f"Сумма: {sum_result}")
    print(f"Разность: {diff_result}")
    print(f"Произведение: {prod_result}")
    print(f"Частное: {div_result}")


if __name__ == '__main__':
    expression_output()