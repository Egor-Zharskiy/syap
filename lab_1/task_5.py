# Реализуйте программу «Кондитерская», которая будет включать
# в себя шесть пунктов меню. У вас есть словарь, где ключ – название
# продукции (торт, пирожное, маффин и т.д.). Значение – список,
# который содержит состав, цену (за 100гр) и кол-во (в граммах).
# 1. Просмотр описания: название – описание
# 2. Просмотр цены: название – цена.
# 3. Просмотр количества: название – количество.
# 4. Всю информацию.
# 5. Покупка
# В пункте «Покупка» необходимо совершить покупку, с
# клавиатуры вводите название продукции и его кол-во, n – выход из
# программы. Посчитать цену выбранных товаров и сколько товаров
# осталось в изначальном списке
# 6. До свидания

def get_menu():
    return """\n
    1 - Описание продукта
    2 - Цена продукта
    3 - Количество продукта
    4 - Просмотр информации о продукте
    5 - Купить
    6 - Просмотр вашей корзины
    7 - Завершение работы программы\n
    """


# {'cake': [quantity, price]}
class Basket:
    def __init__(self):
        self.__basket = {}

    def add_dessert(self, val):
        if val[0] not in self.__basket.keys():
            self.__basket[val[0]] = val[1]
        else:
            self.__basket[val[0]][0] += val[1][0]

    def calc_price(self):
        res = sum(item[0] * item[1] for item in self.__basket.values())
        return res

    def __str__(self):
        return "; ".join(f"{key}: {el[0]}" for key, el in self.__basket.items())


class Confectionery:
    def __init__(self, data):
        self.data = data
        self.values = ['', 'р', 'г']

    def get_description(self, key):
        return self.data[key][0]

    def get_quantity(self, key):
        return self.data[key][2]

    def get_price(self, key):
        return self.data[key][1]

    def get_formatted(self, key, val, case):
        return f"{key} - {val} {self.values[case]}"

    def print_keys(self):
        print(", ".join(self.data.keys()))

    def get_info(self, key):
        val = self.data[key]
        return f"Состав - {val[0]} \nЦена - {val[1]}\nКоличество - {val[2]}"

    def buy(self, key, quantity):
        self.data[key][2] -= quantity * 100


confect = Confectionery({"maffin": ['water, etc', 125, 4000], 'cake': ['water, salt, jam', 200, 5000],
                         "truffel": ['water, sugar, milk, eggs, butter', 50, 5000]})
basket = Basket()

while True:
    try:
        # print("Десерты:", end=' ')
        # confect.print_keys()

        # print("\nМеню:")
        # for product in confect.data:
        #     print("____________")
        #     print(confect.get_info(product))

        choice = int(input("Выберите одно из предложенных действий: " + get_menu()))

        match choice:
            case 1:
                for product_name in confect.data.keys():
                    print("Описание для", confect.get_formatted(product_name, confect.get_description(product_name), 0))

            case 2:
                for product_name in confect.data.keys():
                    print("Цена за 100 гр для", confect.get_formatted(product_name, confect.get_price(product_name), 1))

            case 3:
                for product_name in confect.data.keys():
                    print("Количество ", confect.get_formatted(product_name, confect.get_quantity(product_name), 2))

            case 4:
                for product_name in confect.data.keys():
                    print(confect.get_info(product_name))

            case 5:
                print("Десерты:", end=' ')
                confect.print_keys()

                product_name = input("Введите название десерта: ")
                if product_name not in confect.data.keys():
                    raise KeyError

                quantity = int(input('Введите количество порций (одна порция - 100 грамм), которое вы хотите купить: '))
                if quantity * 100 > confect.get_quantity(product_name):
                    print("Введено недопустимое значение количества порций")
                    continue
                basket.add_dessert((product_name, [quantity, confect.get_price(product_name)]))
                confect.buy(product_name, quantity)
                # print(confect.data)

                print("Ваша корзина: ", basket)

                print("Стоимость вашей корзины: ", basket.calc_price())
                print()

            case 6:
                print("Ваша корзина: ", basket)

                print("Стоимость вашей корзины: ", basket.calc_price())

            case 7:
                exit()

            case _:
                print("Неверный выбор функции\n")

    except KeyError:
        print("\nНеверный ввод названия десерта\n")
    except ValueError:
        print("\nНеверный ввод\n")
