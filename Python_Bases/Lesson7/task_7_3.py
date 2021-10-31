"""
3.	Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать
скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
   |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html

Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая
решена, например, во фреймворке django.
"""

import os
import shutil

root_dir = 'my_project'
if not os.path.exists(root_dir):
    raise FileNotFoundError('Необходимо выполнить task_7_2.py')
templates_root_path = os.path.join(root_dir, 'templates')
source_templates_root_path = templates_root_path
i = 0
while os.path.exists(templates_root_path):
    i += 1
    templates_root_path = source_templates_root_path + str(i)
os.mkdir(templates_root_path)
for root, dirs, files in os.walk(root_dir):
    # print(root, dirs, files)
    for file in files:
        if file.endswith('.html'):
            templates_dir_path = os.path.join(templates_root_path, root.split('\\')[-1])
            if not os.path.exists(templates_dir_path):
                os.mkdir(templates_dir_path)
            filename_src = os.path.join(root, file)
            filename_dst = os.path.join(templates_dir_path, file)
            with open(filename_src, encoding='utf-8') as f_src, open(filename_dst, 'w', encoding='utf-8') as f_dst:
                shutil.copyfileobj(f_src, f_dst)
