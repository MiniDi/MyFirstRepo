def filter_capitalized(strings):
    return [s for s in strings if s and s[0].isupper()]

if __name__ == '__main__':
    user_input = input("Введите строки через запятую: ")
    string_list = [s.strip() for s in user_input.split(',')]
    result = filter_capitalized(string_list)
    print("Строки, начинающиеся с заглавной буквы:", result)