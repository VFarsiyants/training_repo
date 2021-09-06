# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с
# клавиатуры.
n = int(input('Enter quantity of elements in progressive sequence 1 -0.5 0.25 -0.125 ... : '))
sum_sequence = sum([1 / ((-2)**i) for i in range(n)])
print(f'Sum of sequence elements is {sum_sequence}')
