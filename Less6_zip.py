"""
В ДЗ не было таких задач

Задача: Задайте два списка: фамилиии и имена сотрудников, и года их рождения.
Объедините списки в первый словарь, где ключем будет фамилия и имя сотрдуника, отсортированный по фамилии и имени.
Объедините списки во второй словарь, где ключем ,будет год рождения, отсортированный по году рождения.
"""


employee_years = [1981, 1969, 1975, 1992, 1985]
employee_names = ["Иванов Иван", "Петров Петров", "Сергеев Сергей", "Андреев Адрей", "Васильев Василий"]

zipped_dict1 = dict(sorted(dict(zip(employee_names, employee_years)).items()))
zipped_dict2 = dict(sorted(dict(zip(employee_years, employee_names)).items()))


print("Первый словарь: ", zipped_dict1)
print("Второй словарь: ", zipped_dict2)
