# Создать класс List (список), в котором реализовать методы для работы со
# списком (не менее 5).

def menu():
    print("\n1 - добавить элемент в список")
    print("2 - удалить элемент из списка по индексу")
    print("3 - удалить элемент из списка по значению")
    print("4 - получить длину списка")
    print("5 - вывод списка")
    print("6 - очистить список\n")


class List:
    def __init__(self):
        self.data = []

    def add_el(self, el):
        self.data.append(el)

    def pop_el(self, index):
        try:
            self.data.pop(index)

        except IndexError:
            print("Указан Неверный индекс")

    def remove_el(self, value):
        try:
            self.data.remove(value)

        except ValueError:
            print("Такого элемента в списке нет")

    def __len__(self):
        return len(self.data)

    def clear(self):
        self.data = []

    def __str__(self):
        data_as_strings = [str(item) for item in self.data]
        return ', '.join(data_as_strings)


l = List()
while True:
    menu()
    n = int(input("Введите число: "))

    match n:
        case 1:
            el = int(input("Введите значение: "))
            l.add_el(el)
        case 2:
            index = int(input("Введите индекс: "))
            l.pop_el(index)
        case 3:
            el = int(input("Введите значение для удаления из списка: "))
            l.remove_el(el)
        case 4:
            print(len(l))
        case 5:
            print(l)
        case 6:
            l.clear()
        case _:
            print("Неверный выбор")
