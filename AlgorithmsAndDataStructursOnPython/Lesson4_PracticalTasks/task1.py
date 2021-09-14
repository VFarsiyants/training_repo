# Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках практического задания первых
# трех уроков.

# Задачу будем решать для задачи 9 третьего урока.
# Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint
import cProfile
import timeit


def matrix_generation(matrix_rows, matrix_lines):
    matrix = []
    for i in range(matrix_lines):
        matrix += [[]]
        for j in range(matrix_rows):
            matrix[i] += [randint(-100, 100)]
    matrix_string = ''
    for line in matrix:
        for number in line:
            matrix_string += f'{number:>4}   '
        else:
            matrix_string += '\n'
    print(f'Generated matrix')
    print(matrix_string)
    return matrix


# matrix = matrix_generation(500, 500)
matrix = matrix_generation(1000, 1000)
# matrix = matrix_generation(2000, 2000)

# функция matrix_generation заменяет человеческий ввод и не не участвует в оценке сложности и скорости работы.
# входными данными является число строк и столбцов в матрице


# solution
def main():
    rows = [[line[i] for line in matrix] for i in range(len(matrix))]
    # операции генерации столбцов массива, выполняется n*m операций в зависимости, то есть O(n^2)
    # от числа строк и числа столбцов массива.
    max_amongst_rows_minimums = max([min(row) for row in rows])
    # здесь сначала опредаляется минимум в в кажом ряду массива, число операций равно число рядов
    # с поиском минммального значения т/е O(n^2), затем в полученном списке ищется максимум с операцией
    # соответствующей асимптоматике O(n)
    print(f'maximum amongst rows\' minimums is {max_amongst_rows_minimums}')
    # общая сложность алгоритма соотвествует O(n^2)


cProfile.run('main()')
# для PC на котором выполнялось ДЗ
# при matrix_generation(500, 500) сProfile выдает выполнение за 0.006 секунды
# при matrix_generation(1000, 1000) сProfile выдает выполнение за 0.025 секунды
# при matrix_generation(2000, 2000) сProfile выдает выполнение за 0.101 секунды

# видим что про увелечении n в два раза алгоритм отрабатывается в 4 раза дольше то есть сложность O(n^2)
# определена правильно
# из результата работы cProfile понятно что слабое место это поиск минимумов в рядах матрицы
