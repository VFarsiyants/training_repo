"""
Написать декоратор для логирования типов позиционных аргументов функции, например:
def type_logger...
    ...
@type_logger
def calc_cube(x):
   return x ** 3

# >>> a = calc_cube(5)
5: <class 'int'>

Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения
функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора? Сможете
ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
calc_cube(5: <class 'int'>)
"""
from functools import wraps


def type_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_list = list(args) + list(kwargs.values())
        types = list(map(type, args_list))
        types = list(zip(args_list, types))
        result = func(*args, **kwargs)
        string = "".join([str(item[0]) + ': ' + str(item[1]) + ', ' for item in types]).strip(', ')
        print(string)
        print(f'{func.__name__}({string})')
        return result

    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


@type_logger
def calc_difficult(x, y, z=0):
    return x ** 3 + y + z * 2


calculation = calc_cube(2)
print(calculation)
calculation = calc_difficult(2, 3, z=5)
print(calculation)
