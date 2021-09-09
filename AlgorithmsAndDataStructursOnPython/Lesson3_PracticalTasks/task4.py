# 4. Определить, какое число в массиве встречается чаще всего.

import random

length_list = 1000
numbers = [random.randint(-100, 100) for _ in range(length_list)]
print('Generated list:')
print(numbers)

# solution
most_frequent_number = numbers[0]
most_frequent_number_qty = numbers.count(most_frequent_number)
for item in set(numbers):
    frequency = numbers.count(item)
    if frequency > most_frequent_number_qty:
        most_frequent_number_qty = frequency
        most_frequent_number = item
print(f'The most frequent number in sequence is {most_frequent_number}')
