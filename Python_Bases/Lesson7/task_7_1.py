"""
1.	Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |--mainapp
   |--adminapp
   |--authapp

Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию
этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять
конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

"""

import os


def project_folder(main_folder: str, *args: str):
    i = 0
    source_name = main_folder
    while os.path.exists(main_folder):
        i += 1
        main_folder = source_name + str(i)
    os.mkdir(main_folder)
    for sub_folder in args:
        dir_path = os.path.join(main_folder, sub_folder)
        os.mkdir(dir_path)


project_folder('my_project', 'settings', 'mainapp', 'adminapp', 'authapp')
