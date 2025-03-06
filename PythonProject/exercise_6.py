def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число.")

def calculation():
    numbers_sum = 0
    while True:
        number = get_number("Введите число (0 чтобы закончить): ")
        if number == 0:
            break
        if number % 2 == 0:
            numbers_sum += number
    return numbers_sum

def print_sum(numbers_sum):
    print(f"Сумма чисел равна {numbers_sum}")

if __name__ == '__main__':
    total = calculation()
    print_sum(total)