"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
[0; 50]. Выведите на экран исходный и отсортированный массивы.
"""
import random

list_len_gen = 25
rounder = 2

number = random.random()
numbers = [round(random.randint(0, 50) * random.random(), rounder) for _ in range(list_len_gen)]
print('source list')
print(numbers)


def merge_sort(list_to_sort):
    list_len = len(list_to_sort)
    # base case, empty list and list with 1 item is always sorted
    if list_len == 1 or list_len == 0:
        return list_to_sort
    part_len = list_len // 2
    # divide list on two parts
    left, right = list_to_sort[:part_len], list_to_sort[part_len:]
    # sort parts by the same algorithm
    left = merge_sort(left)
    right = merge_sort(right)
    left_len = len(left)
    right_len = len(right)
    result = []
    l, r = 0, 0,
    # both lists sorted by ascending so we go by each item and decide correct position of digit in result
    # by comparing items from one list with current item from another list
    while l < left_len and r < right_len:
        if left[l] >= right[r]:
            result += [right[r]]
            r += 1
        else:
            result += [left[l]]
            l += 1
    if l < left_len:
        result += left[l:]
    if r < right_len:
        result += right[r:]
    return result


print('sorted list')
print(merge_sort(numbers))
