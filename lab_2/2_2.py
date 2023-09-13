def even_digits(num):
    quantity = 0
    while num > 0:
        digit = num % 10
        if digit % 2 == 0:
            quantity += 1
        num //= 10

    print(f'Количество четных цифр = {quantity}')


# добавить проверку на пустые кортежи и списки
# возвращать значения из функции а не принтить

def func(var):
    if isinstance(var, tuple):
        length = 0
        for el in var:
            if isinstance(el, str):
                length += len(el)
        print(length)

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
        print('Сумма после первого отрицательного элемента:', res)

    elif isinstance(var, int):
        even_digits(var)

    elif isinstance(var, str):
        summ = 0
        for el in var:
            if el.isdigit():
                summ += int(el)

        print("Сумма всех чисел строки: ", summ)


# func(("a", 'b', 'cde', 123))
# func([0, 20, 0, -3, 40, 0, 20, 0])
# func(24681039)
func(list())
