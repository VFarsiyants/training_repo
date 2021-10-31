# 3.	Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом  — данные об их хобби. Известно, что при
# хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.
# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о
# хобби. Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
# чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи
# считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Фрагмент файла с данными о хобби  (hobby.csv):
# скалолазание,охота
# горные лыжи

# keys = []
# values = []
# with open('users.csv', 'r', encoding='utf-8') as f:
#     for line in f:
#         keys.append(" ".join(line.split(',')).strip())
# with open('hobby.csv', 'r', encoding='utf-8') as f:
#     for line in f:
#         values.append(line.strip())
# # print(keys)
# # print(values)
#
# result = {}
# for k in keys:
#     if keys.index(k) < len(values):
#         result[k] = values[keys.index(k)]
#     else:
#         result[k] = None

# print(result)

# with open('users_hobby.txt', 'w', encoding='utf-8') as f:
#     for k, v in result.items():
#         f.write(k + ': ' + str(v) + '\n')

# 4.	*(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём ОЗУ (разумеется, не нужно
# реально создавать такие большие файлы, это просто задел на будущее проекта). Только теперь не нужно создавать словарь
# с данными. Вместо этого нужно сохранить объединенные данные в новый файл (users_hobby.txt). Хобби пишем через
# двоеточие и пробел после ФИО:
# Иванов,Иван,Иванович: скалолазание,охота
# Петров,Петр,Петрович: горные лыжи

# 5.	**(вместо 4) Решить задачу 4 и реализовать интерфейс командной строки, чтобы можно было задать имя обоих
# исходных файлов и имя выходного файла. Проверить работу скрипта.

# Команда для проверки в терминале:
# python task_6_5(4_3).py users.csv hobby.csv users_hobby.txt

from sys import argv

users_file = argv[1]
hobby_file = argv[2]
result_file = argv[3]

with open(result_file, 'w', encoding='utf-8') as f:
    with open(users_file, 'r', encoding='utf-8') as f_users, open(hobby_file, 'r', encoding='utf-8') as f_hobby:
        for line in f_users:
            hobby_line = f_hobby.readline()
            f.write(" ".join(line.split(',')).strip() + ': ' + (hobby_line.strip() if hobby_line else 'None') + '\n')
print('Файл с именем', result_file, 'записан в рабочей директории')
