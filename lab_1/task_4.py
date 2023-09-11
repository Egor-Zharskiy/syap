# Отсортируйте словарь по значению в порядке возрастания и убывания
def sort_dict(data):
    d = dict(sorted(data.items(), key=lambda x: x[1]))
    return d


def reverse_sort(data):
    d = dict(sorted(data.items(), key=lambda x: x[1], reverse=True))
    return d


var = {
    'key1': 42,
    'key2': 123,
    'key3': 7,
    'key4': 1000,
}
print("Исходный словарь:", var)
var1 = sort_dict(var)
var2 = reverse_sort(var)
print(var1, var2, sep='\n')
