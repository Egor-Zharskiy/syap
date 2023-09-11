# Дан список list=[1612,49,'hello',6,19, 'world’].
# Все числа этого списка проверить на чётность. Если число чётное, то
# посчитать сумму его цифр. Если нечётное, то заменить его на 1 в
# списке. Все слова: посчитать количество гласных и согласных.
# Вывести всё на экран.

def task(l):
    consonants_num = 0
    vowels_num = 0

    for i in range(len(l)):
        if isinstance(l[i], int):
            if l[i] % 2 == 0:
                total_sum = 0
                num = l[i]
                while num > 0:
                    digit = num % 10
                    total_sum += digit
                    num //= 10
                print(f"Сумма цифр для числа {l[i]} : {total_sum}")
            else:
                l[i] = 1

        elif isinstance(l[i], str):
            for letter in l[i]:
                if letter.upper() in 'BCDFGHJKLMNPQRSTVWXZ':
                    consonants_num += 1
                elif letter.upper() in 'AEIOU':
                    vowels_num += 1

    print(f"Список с замененными символами: {l}")
    print(f'Количество гласных: {vowels_num}')
    print(f"Количество согласных: {consonants_num}")


data = [1612, 49, 'hello', 6, 19, 'world']
print(data)
task(data)
