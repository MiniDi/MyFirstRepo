def main():
    file_name = input("Введите имя текстового файла: ")

    try:
        with open(file_name, 'r', encoding='utf-8') as original_file:
            lines = original_file.readlines()
            print("\nСодержимое файла:")
            for line in lines:
                print(line, end='')

        new_file_name = "new_" + file_name
        with open(new_file_name, 'w', encoding='utf-8') as new_file:
            for idx, line in enumerate(lines, start=1):
                new_file.write(f"{idx}: {line}")

        print(f"\n\nФайл с пронумерованными строками сохранён как: {new_file_name}")

    except FileNotFoundError:
        print("Файл не найден. Убедитесь, что имя файла указано правильно.")


if __name__ == "__main__":
    main()