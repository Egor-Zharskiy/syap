# Создать классы: «Книга», «Отдел», «Библиотека». В классах реализовать
# следующие методы: добавление, удаление, изменение названия книг из
# отделов. Классы должны содержать методы доступа и изменения всех поле.
# Предусмотреть метод записи информации в файл. –
import json


def menu():
    print("1 - добавить книгу в отделение")
    print("2 - изменить название книги")
    print("3 - удалить книгу")
    print("4 - вывод книг библиотеки")


class Book:
    def __init__(self, name, author):
        self.__name = name
        self.__author = author

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, val):
        self.__name = val

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, val):
        self.__author = val

    def set_name(self, name):
        self.name = name

    @staticmethod
    def create_book():
        name = input("Введите название книги: ")
        author = input("Введите автора книги: ")
        return Book(name, author)


class Department:
    def __init__(self, name):
        self.name = name
        self.__books = []

    @property
    def books(self):
        return self.__books

    @books.setter
    def books(self, val):
        self.__books = val

    def add_book(self, name):
        self.books.append(name)

    def edit_book_name(self, index, name):
        self.books[index].name = name

    def delete_book(self, index):
        try:
            self.books.pop(index)
        except IndexError:
            print("Введен неверный индекс книги")

    def __str__(self):
        return f"\n{self.name}" + '\n'.join(f"{i + 1} - {self.books[i].name}" for i in range(len(self.books)))

    def print_books(self):
        for i in range(len(self.books)):
            print(f"{i + 1} - {self.books[i].name}")


class Library:
    def __init__(self):
        self.__deps = []

    @property
    def deps(self):
        return self.__deps

    @deps.setter
    def deps(self, val):
        self.__deps = val

    def add_department(self, department):
        self.deps.append(department)

    def write_to_file(self):
        data = {}
        for department in self.deps:
            data[department.name] = [book.name for book in department.books]
            with open("library.json", 'w') as file:
                json.dump(data, file, ensure_ascii=False)

        print(data)

    def print_departments(self):
        for i in range(len(self.deps)):
            print(f"{i + 1} - {self.deps[i].name}")

    def print_all_books(self):
        for department in self.deps:
            for book in department.books:
                print(book.name)


book1 = Book('eminem', 'Egor')
book2 = Book('YAYAYA', 'Ilya')
book3 = Book('OLOLOLOLO', 'Fedya')

department1 = Department('Фентези')
department1.add_book(book1)
department1.add_book(book2)

department2 = Department('История')
department2.add_book(book3)

lib = Library()
lib.add_department(department1)
lib.add_department(department2)

while True:
    menu()
    n = int(input("Ваш выбор: "))
    match n:
        case 1:
            # x - 1
            lib.print_departments()
            x = int(input("Выберите, в какое отделение будет добавлена новая книга: "))
            book = Book.create_book()
            lib.deps[x - 1].add_book(book)

        case 2:
            lib.print_departments()
            x = int(input("Выберите, в каком подразделении находится книга, название которой вы хотите "
                          "отредактировать: "))
            lib.deps[x - 1].print_books()
            ind = int(input("Выберите книгу для изменения названия: "))
            name = input("Введите новое название книги: ")
            lib.deps[x - 1].books[ind - 1].name = name
            for book in lib.deps[x - 1].books:
                print(book.name)

        case 3:
            lib.print_departments()
            x = int(input("Выберите, из какого отделения будет удалена книга: "))
            lib.deps[x - 1].print_books()
            ind = int(input("Выберите книгу для удаления: "))

            lib.deps[x - 1].delete_book(ind - 1)

        case 4:
            lib.print_all_books()
