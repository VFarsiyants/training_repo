# 4.	Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]
#
# Подсказка: использовать возможности python, изученные на уроке. Подумайте, как можно сделать оптимизацию
# кода по памяти, по скорости.
from time import perf_counter
import sys

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


# Буду пробовать решать двумя способами, через comprehensions и через конструктор генератора.
# Способ первый - через конструктор, сначала создаем функцию


def compare_nums_gen(input_list):
    for i in range(len(input_list) - 1):
        if input_list[i + 1] > input_list[i]:
            yield input_list[i + 1]


# Выполняем задачу - делаем вывод
print('Через конструктор генератора')
start = perf_counter()
result = compare_nums_gen(src)
print("память: ", sys.getsizeof(result), "результат: ", *result, "скорость: ", perf_counter() - start)
print('________________________________________________________________________________________________')
print('Через лист comprehension')
start = perf_counter()
result = [src[i + 1] for i in range(len(src) - 1) if src[i + 1] > src[i]]
print("память: ", sys.getsizeof(result), "результат: ", *result, "скорость: ", perf_counter() - start)

# На моем ПК исходя из условий задачи выйгрыш по памяти незначителен у конструктора, но comprehension побеждает по
# скорости
