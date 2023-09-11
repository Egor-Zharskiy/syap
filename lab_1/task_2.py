# Посчитать, сколько пар (стоят рядом) верхнего и нижнего регистра
# находится в веденном с клавиатуры слове. (Пример HjkLM- 1 пара
# нижнего, 1 пара верхнего), а также сколько согласных букв в слове.


def task(word):
    upper_kol = 0
    lower_kol = 0
    consonants_kol = 0
    index = 0

    while index < len(word) - 1:

        if word[index].islower() and word[index + 1].islower():
            lower_kol += 1
            index += 2

        elif word[index].isupper() and word[index + 1].isupper():
            upper_kol += 1
            index += 2

        else:
            index += 1

    for letter in word:
        if letter.lower() in 'bcdfghjklmnpqrstvwxyz':
            consonants_kol += 1

    print(f"Количество пар в верхнем регистре: {upper_kol}")
    print(f"Количество пар в нижнем регистре: {lower_kol}")
    print(f"Количество согласных букв в слове: {consonants_kol}")


w = input("Введите слово: ")
task(w)
