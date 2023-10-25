import numpy as np
import matplotlib.pyplot as plt

a_values = np.arange(3.5, 25.5, 1.5)  # значения a
x = 1.21  # согласно условию
y_values = np.arcsin(x / 3) + 1.2 * a_values  # список значений y

max_val = np.max(y_values)
min_val = np.min(y_values)
mean_val = np.mean(y_values)

print('Список аргументов функции: ', a_values)
print('Список значений функции: ', y_values)

print("Наибольшее значение функции: ", max_val)
print("Наименьшее значение функции: ", min_val)
print("Среднее значение функции: ", mean_val)

count = len(y_values)
sorted_vals = np.sort(y_values)
print('Отсортированные по возрастанию значения функции f(x): ', sorted_vals)

# построение графика
plt.plot(a_values, y_values, label='f(x)')
mean_line = np.full_like(a_values, mean_val)
plt.plot(a_values, mean_line, label='mean val')
plt.legend(loc='lower right')
plt.xlabel('x')
plt.ylabel('y')
plt.title("График функции f(x) + график среднего значения")
plt.grid(True)
plt.show()


