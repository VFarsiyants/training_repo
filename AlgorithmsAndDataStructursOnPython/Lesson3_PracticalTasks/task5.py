# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

import random

length_list = 10
numbers = [random.randint(-100, 100) for _ in range(length_list)]
print('Generated list:')
print(numbers)

#solution
max_negative_number = max([item for item in numbers if item < 0])
print(f'Maximum negative number in sequence is {max_negative_number}')
