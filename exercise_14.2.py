def main():
    file_name = input("Введите имя нового текстового файла: ")
    user_text = input("Введите текст для записи в файл: ")
    upper_text = user_text.upper()

    try:
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(upper_text)

        print(f"Файл '{file_name}' успешно создан и сохранён.")
    except Exception as e:
        print(f"Произошла ошибка при записи файла: {e}")


if __name__ == "__main__":
    main()