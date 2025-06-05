def process_list(numbers):
    positives = [num for num in numbers if num > 0]
    if positives:
        print(max(positives))
    else:
        print("Нет положительных чисел")


def get_text():
    user_input = input("Введите список чисел через пробел: ")
    if user_input:
        try:
            numbers = list(map(int, user_input.split()))
            process_list(numbers)
        except ValueError:
            print("Ошибка: ввод должен содержать только числа.")
    else:
        print("Ошибка: пустая строка.")


if __name__ == '__main__':
    get_text()