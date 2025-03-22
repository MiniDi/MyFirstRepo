from units import common_function


def get_count():
    while True:
        try:
            count = int(input("Сколько чисел вы хотите ввести? "))
            if count > 0:
                return count
            else: print("Введите число больше 0.")
        except ValueError:
            print("Ошибка: введите целое число.")


def get_average(numbers, count):
    average = sum(numbers) / count  # Вычисляем среднее арифметическое
    return average # Возвращает значение, тогда как print выводит строку


def main():
    count = get_count()
    numbers = []

    for i in range(1, count + 1):
        num = common_function.get_number(f"Введите число {i}: ")
        numbers.append(num)

    result = get_average(numbers, count)
    print(f"Среднее арифметическое: {result}")

if __name__ == '__main__':
    main()