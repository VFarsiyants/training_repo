"""
2.	*(вместо 1) Написать скрипт, создающий из config.yaml стартер для проекта со следующей структурой:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html

Примечание: структуру файла config.yaml придумайте сами, его можно создать в любом текстовом редакторе «руками»
(не программно); предусмотреть возможные исключительные ситуации, библиотеки использовать нельзя.
"""
import os

# Считываем данные из файла
with open('config.yaml', 'r', encoding='utf-8') as f:
    raw_data = f.read().strip()
# Разбиваю данные в файле в итирируемый формат, определяю корневое имя файла
raw_data = raw_data.split('\n')
# Определяю имя главной папки
creation_path = raw_data.pop(0).strip(':')
source_name = creation_path
i = 0
# Защищаемся от повторного создания папки
while os.path.exists(creation_path):
    i += 1
    creation_path = source_name + str(i)
os.mkdir(creation_path)
last_folder_created_level = 0
# Через условия определяем все возможные пути файлов / папок и создаем сущности
for item in raw_data:
    current_entity_level = len(item.split('-')[0])
    if item.endswith(':') and last_folder_created_level < current_entity_level:
        creation_path = os.path.join(creation_path, item.split('- ')[-1].strip(':'))
        last_folder_created_level = current_entity_level
        os.mkdir(creation_path)
    elif item.endswith(':') and last_folder_created_level >= current_entity_level:
        creation_path = creation_path.split('\\')
        creation_path = os.path.join(*creation_path[:-(1 + last_folder_created_level - current_entity_level)],
                                     item.split('- ')[-1].strip(':'))
        last_folder_created_level = current_entity_level
        os.mkdir(creation_path)
    else:
        f = open(os.path.join(creation_path, item.split('- ')[-1]), 'w', encoding='utf-8')
        f.close()
