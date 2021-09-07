# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями
# 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация
# начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.
import random

list_length = 100
numbers = [random.randint(0, 100) for _ in range(list_length)]
print('Generated list')
print(numbers)

#solution

even_index_list = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]
print('List of indexes of even elements')
print(even_index_list)

