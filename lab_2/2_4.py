# Напишите программу, демонстрирующую работу try\except\finally

class NegativeValue(Exception):
    pass


try:
    a = int(input("Введите делимое число > 0: "))
    if a <= 0:
        raise NegativeValue
    num = int(input("Введите делитель: "))
    res = a // num
except ValueError:
    print("Введен неверный формат ввода")
except ZeroDivisionError:
    print('Деление на ноль')
except NegativeValue:
    print("Первое введенное число должно быть больше 0")

else:
    print(f"Результат целочисленного деления {a} на {num} = ", res)

finally:
    print("Блок Finally")


print("Продолжение программы")
