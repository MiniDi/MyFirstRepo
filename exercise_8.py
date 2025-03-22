def is_palindrome(text):
    # Удаляем пробелы и приводим к нижнему регистру
    cleaned_text = text.replace(" ", "").lower()
    # Сравниваем строку с её реверсированной копией
    if cleaned_text == cleaned_text[::-1]:
        print("Да, это палиндром!")
    else:
        print("Нет, это не палиндром.")


def get_text():
    user_input = input("Введите строку: ").strip()
    if user_input:
        is_palindrome(user_input)
    else:
        print("Ошибка: пустая строка.")


if __name__ == '__main__':
    get_text()