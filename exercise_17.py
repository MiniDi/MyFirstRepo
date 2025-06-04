class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")

class Student:
    def __init__(self, university):
        self.university = university

    def get_info(self):
        print(f"Имя: {self.name}") # надо ли вообще повторять? Можно ли как-то переиспользовать то, что уже объявлено
        print(f"Возраст: {self.age}")
        print(f"Университет: {self.university}")