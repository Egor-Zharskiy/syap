# Дан кортеж целых чисел. Отсортировать его в порядке убывания.
# Вывести первый и последний элемент кортежа. – 1 балл
my_tuple = (5, 2, 9, 1, 7, 3)

sorted_tuple = tuple(sorted(my_tuple, reverse=True))

first_element = sorted_tuple[0]
last_element = sorted_tuple[-1]

print("Исходный кортеж:", my_tuple)
print(f"Отсортированный кортеж: {sorted_tuple}")
print(f"Первый элемент: {first_element}")
print(f"Последний элемент: {last_element}")
