# . Напишите функцию, которая будет принимать один аргумент. Если в
# функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то сумму после первого отрицательного элемента.
# Удалить все повторяющиеся элементы.
# Число – кол-во четных цифр.
# Строка – найти сумму всех чисел.
# Сделать проверку со всеми этими случаями

def even_digits(num):
    quantity = 0
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            quantity += 1
        num //= 10

    return quantity


def func(var):
    if isinstance(var, tuple):
        length = 0
        for el in var:
            if isinstance(el, str):
                length += len(el)
        return length

    elif isinstance(var, list):
        negative_pos = False
        res = 0
        for i in range(len(var)):
            if negative_pos:
                res += var[i]
            else:
                if var[i] < 0:
                    if not negative_pos:
                        negative_pos = True
                    else:
                        res += var[i]
        unique_var = list(set(var))
        print("Строка после удаления всех повторений: ", unique_var)
        # print('Сумма после первого отрицательного элемента:', res)
        return res

    elif isinstance(var, int):
        return even_digits(var)

    elif isinstance(var, str):
        summ = 0
        for el in var:
            if el.isdigit():
                summ += int(el)

        # print("Сумма всех чисел строки: ", summ)
        return summ


a = ("a", 'b', 'cde', 123)
b = [0, 20, 0, -3, 40, 0, 20, 0]
c = 24681039
d = "12344dsfkjsd"
print("Длина всех слов кортежа: ", func(a))
print("Сумма после первого отрицательного элемента", func(b))
print("Кол-во четных цифр: ", func(c))
print("Сумма всех чисел для строки: ", func(d))
