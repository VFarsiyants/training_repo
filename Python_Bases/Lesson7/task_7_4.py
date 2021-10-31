"""
4.	Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер которых
не превышает этой границы, но больше предыдущей (начинаем с 0), например:
    {
      100: 15,
      1000: 3,
      10000: 7,
      100000: 2
    }
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
"""

import django
import os

# Выполняю данную задачу для фреймворка django

result = {}
list_of_sizes = []
root_dir = django.__path__[-1]
print(root_dir)
for root, dirs, files in os.walk(root_dir):
    for file in files:
        src = os.path.join(root, file)
        list_of_sizes.append(os.stat(src).st_size)
thresholds = [10**i for i in range(len(str(min(list_of_sizes))), 1 + len(str(max(list_of_sizes))))]
for threshold in thresholds:
    counter = 0
    for item in list_of_sizes:
        if 10 ** len(str(item)) == threshold:
            counter += 1
    result[threshold] = counter
print(result)