from sys import argv
import os

edit_record_num = int(argv[1]) - 1
new_value = argv[2]

# edit_record_num = 1
# new_value = 'Измененная строка'

with open('bakery.csv', 'r+', encoding='utf-8') as f, open('bakery.temp', 'w', encoding='utf-8') as temp_f:
    i = 0
    for line in f:
        if i == edit_record_num:
            temp_f.write(new_value + '\n')
        else:
            temp_f.write(line)
        i += 1
os.remove('bakery.csv')
os.rename('bakery.temp', 'bakery.csv')

if i >= edit_record_num:
    print('Изменения внесены успешно')
else:
    print('Запись с номером ', edit_record_num + 1, 'отсутствует в файле\nФайл остается без изменений')

# для проверки работы скрипта python "edit_sale_task_6_7(6).py" 3 2430,7
