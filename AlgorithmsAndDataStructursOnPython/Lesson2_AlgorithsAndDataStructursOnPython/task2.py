# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3
# четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = input('Enter positive integer number: ')
odd_digits_qty = sum([int(digit) & 1 for digit in number])
even_digits_qty = len(number) - odd_digits_qty
print(f'Quantity of even digits in number is {even_digits_qty}')
print(f'Quantity of odd digits in number is {odd_digits_qty}')

