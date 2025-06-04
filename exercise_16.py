class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        print(f"Название книги: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Год выпуска: {self.year}")

    def is_old(self):
        if self.year < 1975:
            return True
        else:
            return False