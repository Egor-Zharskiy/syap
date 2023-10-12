# Создать классы «Транспортное средство», «Самолет», «Поезд»,
# «Автомобиль». Определить время и стоимость перевозки для указанных
# городов и расстояний. Вывести данные о наиболее быстрой и экономичной
# поездке. Предусмотреть метод записи информации в файл.


import json


class Transport:
    def __init__(self, name, speed, cost):
        self.name = name
        self.speed = speed
        self.cost_per_km = cost

    def calculate_time(self, distance):
        return distance / self.speed

    def calculate_cost(self, distance):
        return distance * self.cost_per_km


class Airplane(Transport):
    def __init__(self, name, speed, cost):
        super().__init__(name, speed, cost)


class Train(Transport):
    def __init__(self, name, speed, cost):
        super().__init__(name, speed, cost)


class Car(Train):
    def __init__(self, name, speed, cost):
        super().__init__(name, speed, cost)


class City:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance


def find_optimal(city):
    distance = city.distance
    transports = [Airplane('Самолет', 800, 500),
                  Car("Машина", 150, 50),
                  Train('Поезд', 200, 100)]

    min_cost = transports[0].calculate_cost(distance)
    min_time = transports[0].calculate_time(distance)
    min_name = transports[0].name
    cost_name = transports[0].name
    # min_cost + min_time
    for i in range(1, len(transports)):
        if transports[i].calculate_cost(distance) < min_cost:
            min_cost = transports[i].calculate_cost(distance)
            cost_name = transports[i].name
        if transports[i].calculate_time(distance) < min_time:
            min_time = transports[i].calculate_time(distance)
            min_name = transports[i].name

    return min_name, min_time, cost_name, min_cost


cities = [City("Slutsk", 100), City("Minsk", 88), City("Gomel", 350)]

while True:
    print("1 - Выбор города для поездки")
    print("2 - Запись информации в файл")
    choice = int(input())
    match choice:
        case 1:
            for j in range(len(cities)):
                print(f"{j + 1} - {cities[j].name}")

            try:
                n = int(input("Выберите город, в который нужно поехать: "))
                time_name, time, price_name, cost = find_optimal(cities[n - 1])
                print(f"Minimal time on {time_name}: {time} h")
                print(f"Minimal cost on {price_name}: {cost} BYN")

            except ValueError:
                print("Введите числовое значение")
            except IndexError:
                print("Неверный ввод индекса города")

        case 2:
            data = []
            for el in cities:
                transp1, time, transp2, cost = find_optimal(el)
                val = f"optimal time on {transp1} - {time}; optimal cost on {transp2} - {cost}"
                data.append({el.name: val})
                with open("information.json", "w") as file:
                    json.dump(data, file, ensure_ascii=False)
