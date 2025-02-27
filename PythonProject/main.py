# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hello, World!")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число.")

num1 = get_number("Введите первое число: ")
num2 = get_number("Введите второе число: ")

sum = num1 + num2
diff = num1 - num2
prod = num1 * num2
div = num1 / num2 if num2 != 0 else "Деление на ноль невозможно"

print(f"Сумма: {sum}")
print(f"Разность: {diff}")
print(f"Произведение: {prod}")
print(f"Частное: {div}")


user_input = input("Введите строку: ")
if user_input:
    print(f"Первый символ: {user_input[0]}")
    print(f"Последний символ: {user_input[-1]}")
else:
    print("Ошибка: пустая строка.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
