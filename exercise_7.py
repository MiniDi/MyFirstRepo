import random
from units import common_function


def get_random():
    random_number = random.randint(1, 100)
    attempts = 1

    print("Я загадала число от 1 до 100. Попробуйте угадать! У вас есть 10 попыток.")
    number = common_function.get_number("Введите число: ")

    while random_number != number:
        if random_number > number and attempts < 10:
            print("Загаданное число больше.")
            number = common_function.get_number("Введите число: ")
            attempts += 1
        elif random_number < number and attempts <10:
            print("Загаданное число меньше.")
            number = common_function.get_number("Введите число: ")
            attempts += 1
    print(f"Умничка! Вы угадали число {random_number} за {attempts} попыток")


if __name__ == '__main__':
    get_random()