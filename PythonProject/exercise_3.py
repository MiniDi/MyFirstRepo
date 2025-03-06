def get_string():
    while True:
        user_input = input("Введите строку: ").strip() # Удаляем пробелы в начале и в конце строки
        if user_input:
            for number, char in enumerate(user_input, start=1): # Функция проходит по строке посимвольно TODO: уточнить подробнее, что тут происходит
                if char == " ":  # Если символ — пробел
                    print(f"{number}-й символ: пробел")
                else:
                    print(f"{number}-й символ: {char}")
            break
        else:
            print("Ошибка: пустая строка.")

if __name__ == '__main__':
    get_string()