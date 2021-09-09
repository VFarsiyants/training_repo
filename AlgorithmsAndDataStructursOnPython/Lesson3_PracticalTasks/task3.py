# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

length_list = 10
numbers = [random.randint(-100, 100) for _ in range(length_list)]
print('Generated list:')
print(numbers)

# solution
enumerate_numbers = list(enumerate(numbers))
max_index = max(enumerate_numbers, key=lambda x: x[1])[0]
min_index = min(enumerate_numbers, key=lambda x: x[1])[0]
# print(f'Maximum: {numbers[max_index]}, minimum: {numbers[min_index]}')
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

print('List with switched min and max')
print(numbers)
