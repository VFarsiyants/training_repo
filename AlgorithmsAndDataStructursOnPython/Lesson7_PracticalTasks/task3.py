"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану. Медианой
называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в
другой – не больше медианы. Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то
используйте метод сортировки, который не рассматривался на уроках
"""
import random
import statistics


m = 20
list_len_gen = 2 * m + 1

numbers = [random.randint(0, 50) for _ in range(list_len_gen)]
print(numbers)
# for check
print('median by statistics.median', statistics.median(numbers))


def median(numbers_list):
    search_ind = len(numbers_list) // 2 + 1
    while len(numbers_list) > 2:
        pivot = random.randint(0, len(numbers_list) - 1)
        left = [number for number in numbers_list if number <= numbers_list[pivot]]
        right = [number for number in numbers_list if number > numbers_list[pivot]]
        if len(left) >= search_ind:
            numbers_list = left
        else:
            numbers_list = right
            search_ind = search_ind - len(left)
        if len(set(numbers_list)) == 1:
            return numbers_list[0]
    return max(numbers_list) if search_ind-1 else min(numbers_list)


print('*'*150)
print('median by function', median(numbers))



