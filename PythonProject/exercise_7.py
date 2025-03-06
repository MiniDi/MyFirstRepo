import random

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число.")

def get_random():
    random_number = random.randint(1, 100)
    attempts = 1

    print("Я загадала число от 1 до 100. Попробуйте угадать! У вас есть 10 попыток.")
    number = get_number("Введите число: ")

    while random_number != number:
        if random_number > number and attempts < 10:
            print("Загаданное число больше.")
            number = get_number("Введите число: ")
            attempts += 1
        elif random_number < number and attempts <10:
            print("Загаданное число меньше.")
            number = get_number("Введите число: ")
            attempts += 1
    print(f"Умничка! Вы угадали число {random_number} за {attempts} попыток")

if __name__ == '__main__':
    get_random()