# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых
# чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

num_sequence = input(f'Enter numbers divided by space for sequence: ')
digit = input(f'Enter digit to count in sequence: ')
print(f'{digit} is presented in number sequence {num_sequence.count(digit)} times')
