# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

matrix = []
matrix_rows = 5
matrix_lines = 5
for i in range(matrix_lines):
    matrix += [[]]
    for j in range(matrix_rows):
        matrix[i] += [random.randint(-100, 100)]
matrix_string = ''
for line in matrix:
    for number in line:
        matrix_string += f'{number:>4}   '
    else:
        matrix_string += '\n'
print(f'Generated matrix')
print(matrix_string)


# solution
rows = [[line[i] for line in matrix] for i in range(len(matrix))]
max_amongst_rows_minimums = max([min(row) for row in rows])

print(f'maximum amongst rows\' minimums is {max_amongst_rows_minimums}')
