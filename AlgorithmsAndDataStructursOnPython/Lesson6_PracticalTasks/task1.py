"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех
уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей
ОС.
"""
import sys
# Задание 7 второго урока

# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.



n = 24 # int(input('Enter biggest positive integer number: '))
sum_of_numbers = sum([number for number in range(1, n + 1)])
print(f'Sum of positive integer numbers sequence until {n} is {sum_of_numbers}')
right_part = n * (n + 1) / 2
print(f'n * (n + 1) / 2 = {right_part}')
if right_part == sum_of_numbers:
    print(f'It\'s proved that 1 + 2 + 3 + ... + n = n(n+1)/2')
# подсчет выделения памяти
print('*'*100)
# for input 100 as n
print(sys.getsizeof(sum_of_numbers)) #28 int
print(sys.getsizeof(right_part)) #24 float

# Задание 5 первого урока

# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

letters = 'az' # input('Enter two latin letters: ').lower()
first_letter = letters[0]
second_letter = letters[1]
first_position = ord(first_letter) - 96
second_position = ord(second_letter) - 96

print(f'Letter "{first_letter}" position in alphabet is "{first_position}"')
print(f'Letter "{second_letter}" position in alphabet is "{second_position}"')
print(f'Between letters "{first_letter}" and "{second_letter}" are {abs(second_position - first_position) - 1} letters')
# подсчет выделения памяти
print('*'*100)
print(sys.getsizeof(letters))           # 51 string 2 symbols
print(sys.getsizeof(first_letter))      # 50 string 1 symbol
print(sys.getsizeof(second_letter))     # 50 string 1 symbol
print(sys.getsizeof(first_position))    # 28 int
print(sys.getsizeof(second_position))   # 28 int
print(sys.getsizeof(''))                # 49 empty string