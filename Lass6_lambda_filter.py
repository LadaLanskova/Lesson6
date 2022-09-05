"""
Lamda и filter

Задача 3 к уроку 4

Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

Исходный код:
lst = list(map(int, input("Введите числа через пробел:\n").split()))
dct = {}
new_lst = []
for i in lst:
    a = lst.count(i)
    dct.update({i: a})

a = 0
keys = list(dct.keys())
for i in dct:
    if dct[i] == 1:
        new_lst.append(keys[a])
        a += 1
    else:
        a += 1

print(f"Список из неповторяющихся элементов: {new_lst}")
"""
lst = list(map(int, input("Введите числа через пробел:\n").split()))
new_lst = list(filter(lambda a: lst.count(a) == 1, lst))
print(f'Для последовательности {lst}, \n   список уникальных элементов => {new_lst}')
