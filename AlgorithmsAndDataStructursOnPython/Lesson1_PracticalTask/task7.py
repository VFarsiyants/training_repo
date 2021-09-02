# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
# равнобедренным или равносторонним.

a = int(input('Enter length a of triangle side: '))
b = int(input('Enter length b of triangle side: '))
c = int(input('Enter length c of triangle side: '))
sides = [a, b, c]

big_side = max(sides)

if big_side < sum(sides) - big_side:
    unique_sizes = len(set(sides))
    if unique_sizes == 2:
        print('Sides can make isosceles triangle')
    elif unique_sizes == 1:
        print('Sides can make equilateral triangle')
    else:
        print('Sides can make scalene triangle')
else:
    print('Sides can\'t make triangle')
