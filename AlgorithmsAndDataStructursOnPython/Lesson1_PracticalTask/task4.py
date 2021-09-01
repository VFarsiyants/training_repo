# 4. Написать программу, которая генерирует в указанных пользователем границах:
#
# случайное целое число;
# случайное вещественное число;
# случайный символ.

# Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ
# от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f'
# включительно.

import random

minimum = int(input('Enter minimum value for integer number for generation: '))
maximum = int(input('Enter maximum number for integer number for generation: '))
random_int_number = random.randint(minimum, maximum)
print(random_int_number)

minimum = float(input('\nEnter minimum value for real number for generation: '))
maximum = float(input('Enter maximum number for real number for generation: '))
random_float_number = random.random() * (maximum - minimum)
print(random_float_number)

minimum = ord(input('\nEnter interval bottom letter for letter for generation: '))
maximum = ord(input('Enter top interval letter for letter for generation: '))
random_letter_ord = random.randint(minimum, maximum)
print(chr(random_letter_ord))
