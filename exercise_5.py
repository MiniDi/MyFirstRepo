def even_numbers ():
    print("Чётные числа от 1 до 20:")
    for i in range(1, 21):
        if i % 2 == 0:
            print(i, end=" ")
    print("\n")

def odd_numbers ():
    print("Нечётные числа от 1 до 20:")
    for i in range(1, 21):
        if i % 2 != 0:
            print(i, end=" ")
    print("\n")

def div_3 ():
    print("Числа делимые нацело на 3")
    for i in range(1, 21):
        if i % 3 == 0:
            print(i, end=" ")
    print("\n")

def print_numbers(start, end, condition, message):
    print(message)
    for i in range(start, end + 1):
        if condition(i):  # Проверяем условие
            print(i, end=" ")
    print("\n")


if __name__ == '__main__':
    print_numbers(1, 20, lambda x: x % 2 == 0, "Чётные числа от 1 до 20:")
    print_numbers(1, 20, lambda x: x % 2 != 0, "Нечётные числа от 1 до 20:")
    print_numbers(1, 20, lambda x: x % 3 == 0, "Числа, делимые на 3:")
    print_numbers(1, 20, lambda x: x % 3 != 0, "Числа, не делимые на 3:")