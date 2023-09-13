# Дан двумерный массив и два числа: i и j. Поменяйте в массиве
# столбцы с номерами i и j и выведите результат.

def swap_columns(matrix, i, j):
    for row in matrix:
        row[i], row[j] = row[j], row[i]


def task():
    try:
        n = int(input("Введите количество строк матрицы: "))

        matrix = []
        print("Введите элементы матрицы: ")
        for i in range(n):
            row = list(map(int, input().split()))
            matrix.append(row)

        i, j = map(int, input("Введите номера столбцов, которые вы хотите поменять: ").split())

        swap_columns(matrix, i, j)

        # Вывод измененного массива

    except ValueError:
        print("Введено недопустимое значение")

    except IndexError:
        print("Введен неверный индекс")

    else:
        print("Результат: ")
        for row in matrix:
            print(*row)


task()
