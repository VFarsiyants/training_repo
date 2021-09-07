# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами
# минимальный и максимальный элементы в сумму не включать.

import random

length_list = 10
numbers = [random.randint(-100, 100) for _ in range(length_list)]
print('Generated list:')
print(numbers)

# solution
enumerate_numbers = list(enumerate(numbers))
max_index = max(enumerate_numbers, key=lambda x: x[1])[0]
min_index = min(enumerate_numbers, key=lambda x: x[1])[0]

interval_top = max_index if max_index>min_index else min_index
interval_bottom = min_index if interval_top != min_index else max_index

print(f'Maximum: {numbers[max_index]}, minimum: {numbers[min_index]}')

sum_between_min_max = sum([numbers[i] for i in range(interval_bottom+1, interval_top)])

print(sum_between_min_max)
