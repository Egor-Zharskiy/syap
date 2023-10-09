# 2. Создать текстовый файл (не программно). Построчно записать
# названия ювелирных украшений и их стоимость (не менее 10 строк). Вывести
# на экран все украшения дешевле 100 рублей. Найти среднюю стоимость
# украшений.
# Пример файла:
# Кольцо 120
# Цепочка 800

# with open('decorations.txt', 'w') as f1:
#     while True:
#         line = input("Введите строку (пустая строка для завершения ввода): ")
#         if not line:
#             break
#         f1.write(line + '\n')

with open('decorations.txt', 'r') as file:
    lines = file.readlines()

results = []
avg = 0
kol = len(lines)

for line in lines:
    parts = line.strip().split()
    avg += int(parts[1])
    if int(parts[1]) < 100:
        name, price = parts[0], int(parts[1])
        results.append((name, price))

print("Средняя стоимость: ", avg / kol)

print("Украшения дешевле 100 рублей: ")
for name, price in results:
    print(f"{name}: {price} рублей")
