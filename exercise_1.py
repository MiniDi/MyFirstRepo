def print_hi():
    print("Hello, World!") # С помощью кавычек программа понимает, что передается строка


def get_name():
    while True:
        last_name = input("Введите вашу фамилию: ").strip() # Ввод фамилии и удаление пробелов
        if last_name and all(char.isalpha() or char in "- " for char in last_name): # Проверяем, что фамилия не пустая и не содержит цифр
            print(f"{last_name} - сладкая булочка")
            break
        else:
            print("Ошибка: это не фамилия, не надо нам врать.")


if __name__ == '__main__':
    print_hi()
    get_name()