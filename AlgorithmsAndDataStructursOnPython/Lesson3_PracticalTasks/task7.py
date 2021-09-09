# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# # (оба являться минимальными), так и различаться.
import random

length_list = 10
numbers = [random.randint(-100, 100) for _ in range(length_list)]
print('Generated list:')
print(numbers)

#solution
numbers = sorted(numbers)
min1, min2 = numbers[:2]
print(f'Two minimum numbers from sequence are {min1} and {min2}')
