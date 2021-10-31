"""
5.	*(вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи те же,
а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
    {
      100: (15, ['txt']),
      1000: (3, ['py', 'txt']),
      10000: (7, ['html', 'css']),
      100000: (2, ['png', 'jpg'])
    }
Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.
Задачи со * предназначены для продвинутых учеников, которым мало сделать обычное задание.
"""

import django
import os
import json


def folder_summary(root_dir):
    result = {}
    list_of_sizes = []
    list_of_ext = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            src = os.path.join(root, file)
            list_of_sizes.append(os.stat(src).st_size)
            list_of_ext.append(file.split('.')[-1])
    thresholds = [10 ** i for i in range(len(str(min(list_of_sizes))), 1 + len(str(max(list_of_sizes))))]
    for threshold in thresholds:
        files_quantity = 0
        files_extensions_list = []
        for item_size, item_ext in zip(list_of_sizes, list_of_ext):
            if 10 ** len(str(item_size)) == threshold:
                files_quantity += 1
                if item_ext not in files_extensions_list:
                    files_extensions_list.append(item_ext)
        result[threshold] = (files_quantity, files_extensions_list)
    # Выводим результат
    for k, v in result.items():
        print(f'{k}: {v}')
    # Сохраняем в отдельный файл
    folder_name = root_dir.split('\\')[-1]
    with open(f'{folder_name}_summary.json', 'w', encoding='utf-8') as f:
        json.dump(result, f)
    print('-----------------------------------------------------------------')
    print(f'результат сохранен в файл {folder_name}_summary.json')


# Выполняю данную задачу для фреймворка django

folder_summary(django.__path__[-1])
