# Найти сумму нечетных цифр введенного натурального числа

def odd_digits(num):
    total_sum = 0
    while num > 0:
        digit = num % 10
        if digit % 2 != 0:
            total_sum += digit
        num //= 10

    print(f'Сумма нечетных цифр = {total_sum}')


try:
    number = int(input("Введите число: "))
    odd_digits(number)

except ValueError:
    print("Неверный введенный тип данных")
