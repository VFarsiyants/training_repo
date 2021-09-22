"""Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
[-100; 100]. Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
"""
from random import randint


list_len = 30
numbers = [randint(-100, 100) for _ in range(list_len)]


def bubble_sort(numbers_to_sort):
    sorted_flag = True
    n = len(numbers_to_sort)
    i = 0
    while n > 1:
        while i < n - 1:
            if numbers_to_sort[i] > numbers_to_sort[i + 1]:
                numbers_to_sort[i], numbers_to_sort[i + 1] = numbers_to_sort[i + 1], numbers_to_sort[i]
                sorted_flag = False
            i += 1
        if sorted_flag:
            return numbers
        sorted_flag = True
        i = 0
        n -= 1
    return numbers


print('source list')
print(numbers)
print('sorted list')
print(bubble_sort(numbers))
