"""
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать
исключение ValueError, если что-то не так, например:
def val_checker...
    ...

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

# >>> a = calc_cube(5)
125
# >>> a = calc_cube(-5)
Traceback (most recent call last):
  ...
    raise ValueError(msg)
ValueError: wrong val -5

Примечание: сможете ли вы замаскировать работу декоратора?
"""


def val_checker(func_to_check):
    def _val_checker(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            check_result = []
            argument_list = list(args) + list(kwargs.values())
            for item in argument_list:
                if not func_to_check(item):
                    check_result.append(item)
            if check_result:
                wrong_values = ', '.join(list(map(str, check_result)))
                msg = f'wrong values: {wrong_values}'
                raise ValueError(msg)
            return result

        return wrapper

    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


@val_checker(lambda x: x > 0)
def calc_difficult(x, y, z=0):
    return x ** 3 + y + z ** (1 / 3)


@val_checker(lambda x: x != 'bad word')
def say(x, y=None):
    return f'{y} {x}'


calc_result = calc_difficult(4, -3, -1)
print(calc_result)

# Примеры для проверки работы декоратора
# calc_result = calc_cube(5)
# print(calc_result)

# calc_result = calc_cube(-5)
# print(calc_result)
#

#
# print(say('You are', y='bad word'))
