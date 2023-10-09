#  Создать вручную и заполнить несколькими строками текстовый
# файл, в котором каждая строка будет содержать данные о фирме: название,
# форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой
# компании, а также среднюю прибыль. Если фирма получила убытки, в расчёт
# средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и
# их прибылями, а также словарь со средней прибылью. Если фирма получила
# убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий
# файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit":
# 2000}]
# Подсказка: использовать менеджер контекста.

import json

firms_data = []
profit_data = []

# Чтение данных из файла
with open("firms.txt", "r") as file:
    for line in file:
        firm_info = line.strip().split()
        name, ownership, revenue, expenses = firm_info

        revenue = int(revenue)
        expenses = int(expenses)

        # Вычисляем прибыль фирмы
        profit = revenue - expenses

        if profit > 0:
            profit_data.append(profit)
        firms_data.append({name: profit})

average_profit = sum(profit_data) / len(profit_data) if profit_data else 0

firms_data.append({"average_profit": average_profit})

with open("output.json", "w") as json_file:
    json.dump(firms_data, json_file)

print(firms_data)
