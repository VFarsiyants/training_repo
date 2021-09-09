# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

positive_integers = list(range(2, 100))
result = []

top = 9
bottom = 2


for i in range(bottom, top+1):
    count = len([item for item in positive_integers if item % i == 0])
    result += [(i, count)]

print('Numbers list:')
print(positive_integers)
for item in result:
    print(f'{item[1]} numbers are multiple of the {item[0]}')
