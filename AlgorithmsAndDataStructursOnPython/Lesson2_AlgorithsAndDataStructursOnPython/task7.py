# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

n = int(input('Enter biggest positive integer number: '))
sum_of_numbers = sum([number for number in range(1, n + 1)])
print(f'Sum of positive integer numbers sequence until {n} is {sum_of_numbers}')
right_part = n * (n + 1) / 2
print(f'n * (n + 1) / 2 = {right_part}')
if right_part == sum_of_numbers:
    print(f'It\'s proved that 1 + 2 + 3 + ... + n = n(n+1)/2')
