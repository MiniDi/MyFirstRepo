import os
from datetime import datetime


def get_diary_path():
    path = input("Укажите путь к файлу дневника (нажмите Enter для diary.txt в текущей папке): ").strip() #TODO: Ругается на то что нет прав на запись
    return path if path else "diary.txt"


def add_entry(file_path): #TODO: Разобрать вместе происходящее
    entry = input("Введите текст записи:\n")
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    try:
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(f"{timestamp} {entry}\n")
        print("Запись добавлена.")
    except Exception as e:
        print(f"Ошибка при записи в файл: {e}")


def view_entries(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        if content:
            print("\nСодержимое дневника:\n")
            print(content)
        else:
            print("Дневник пока пуст.")
    except FileNotFoundError:
        print("Файл дневника не найден.")
    except PermissionError:
        print("Нет прав для чтения файла.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")


def search_entries(file_path):
    keyword = input("Введите слово для поиска: ").lower()
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        results = [line for line in lines if keyword in line.lower()]
        if results:
            print("\nНайденные записи:")
            for entry in results:
                print(entry.strip())
        else:
            print("Совпадений не найдено.")
    except FileNotFoundError:
        print("Файл дневника не найден.")
    except PermissionError:
        print("Нет прав для чтения файла.")
    except Exception as e:
        print(f"Ошибка при поиске: {e}")


def main():
    file_path = get_diary_path()

    # Создание файла, если не существует
    if not os.path.exists(file_path):
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write("")  # Пустой файл
        except Exception as e:
            print(f"Ошибка при создании файла: {e}")
            return

    while True:
        print("\nВыберите действие:")
        print("1 - Добавить запись")
        print("2 - Просмотреть записи")
        print("3 - Найти запись по слову")
        print("4 - Выход")

        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            add_entry(file_path)
        elif choice == "2":
            view_entries(file_path)
        elif choice == "3":
            search_entries(file_path)
        elif choice == "4":
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите 1, 2, 3 или 4.")


if __name__ == "__main__":
    main()