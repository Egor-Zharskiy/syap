# 1. Создать программный файл F1 в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода данных
# будет свидетельствовать пустая строка. Скопировать из файла F1 в файл F2
# все строки, которые содержат только одно слово. Найти самое длинное слово
# в файле F2.

with open('F1.txt', 'w') as f1:
    while True:
        line = input("Введите строку (пустая строка для завершения ввода): ")
        if not line:
            break
        f1.write(line + '\n')

with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:
    for line in f1:
        # проверка на наличие в строке только одного слова
        if len(line.strip().split()) == 1:
            f2.write(line)

with open('F2.txt', 'r') as f2:
    lines = f2.readlines()
    max_word = max(lines, key=len)

print(f"Скопировано строк в F2: {len(lines)}")
print("Самое длинное слово в файле F2: ", max_word)
