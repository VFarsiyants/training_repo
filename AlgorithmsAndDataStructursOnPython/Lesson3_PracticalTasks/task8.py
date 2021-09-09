# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную
# матрицу.
matrix = []
matrix_rows = 5
matrix_lines = 4

for i in range(matrix_lines):
    matrix += [[]]
    for j in range(matrix_rows-1):
        matrix[i] += [int(input(f'Insert digit {j+1} in line {i+1} of matrix: '))]
    else:
        matrix[i] += [sum(matrix[i])]

matrix_string = ''
for line in matrix:
    for number in line:
        matrix_string += f'{number:>4}   '
    else:
        matrix_string += '\n'

print('The result matrix is: ')
print(matrix_string)
