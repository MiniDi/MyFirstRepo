def phone_book_program():
    phone_book = {}

    print("Введите контакты в формате имя и телефон, через пробел. Для завершения введите 0")

    while True:
        user_input = input("Добавить контакт: ")
        if user_input == "0":
            break

        try:
            name, number = user_input.split()
        except ValueError:
            print("Неверный формат. Введите имя и номер через пробел.")
            continue

        # Добавляем или обновляем контакт
        if name in phone_book:
            phone_book[name].append(number)
        else:
            phone_book[name] = [number]

    print("Телефонная книга:")
    print(phone_book)


if __name__ == '__main__':
    phone_book_program()