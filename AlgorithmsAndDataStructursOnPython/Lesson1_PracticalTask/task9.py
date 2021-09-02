# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

numbers = input('enter numbers separated by space: ').split()
numbers = sorted([int(number) for number in numbers])
print(f'Number in the middle is {numbers[1]}')
